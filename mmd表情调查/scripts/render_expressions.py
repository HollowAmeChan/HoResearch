"""Render the saved project without overwriting it.

Blender arguments after --: --preview or --all [--model COLLECTION].
"""
import argparse
import csv
import json
import re
import sys
import time
import unicodedata
from pathlib import Path

import bpy
from mathutils import Vector

OUT = Path(__file__).resolve().parents[1]
CATALOG = OUT / "附录" / "HoTools_shapekey_catalog.csv"
MODELS = (
    ("Sour式初音", "Black_arm", "Black_mesh", "face", "01_Sour"),
    ("YYB式初音", "YYB Hatsune Miku default 1.0ver_arm", "YYB Hatsune Miku default 1.0ver_mesh", "face01", "02_YYB"),
    ("Appearance Miku", "Appearance Miku_arm", "Appearance Miku_mesh", "顔", "03_Appearance"),
    ("TDA式初音", "Tda式初音ミクV4X Ver1.00_arm", "Tda式初音ミクV4X Ver1.00_mesh", "face00.001", "04_TDA"),
)
CONTEXT_EXAMPLES = {
    "Sour式初音": (
        ("はちゅ目縦潰れ", "はちゅ目"),
        ("はちゅ目横潰れ", "はちゅ目"),
        ("犬歯", "あE"),
        ("歯無し", "あE"),
    ),
    "TDA式初音": (
        ("はちゅ目縦潰れ", "はちゅ目"),
        ("はちゅ目横潰れ", "はちゅ目"),
        ("歯無し上", "あ"),
        ("歯無し下", "あ"),
    ),
}


def save_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def safe_name(name):
    return re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", name).strip(" .") or "expression"


def reset_keys(mesh):
    keys = mesh.data.shape_keys
    if keys.animation_data:
        keys.animation_data_clear()
    for key in keys.key_blocks:
        key.value = 0.0
        key.mute = False
    mesh.show_only_shape_key = False
    mesh.active_shape_key_index = 0


def configure_scene():
    scene = bpy.context.scene
    scene.render.engine = "BLENDER_EEVEE_NEXT"
    scene.render.resolution_x = 512
    scene.render.resolution_y = 512
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGBA"
    scene.render.image_settings.color_depth = "8"
    scene.render.film_transparent = True
    scene.render.use_compositing = False
    scene.render.use_sequencer = False
    scene.render.image_settings.compression = 25
    scene.render.fps = 24
    scene.render.use_file_extension = True
    scene.eevee.taa_render_samples = 128
    scene.view_settings.view_transform = "Standard"
    scene.view_settings.look = "None"
    scene.view_settings.exposure = 0
    scene.view_settings.gamma = 1
    if scene.rigidbody_world:
        scene.rigidbody_world.enabled = False
    scene.frame_set(1)
    world = bpy.data.worlds.new("MMD_Reference_World")
    world.use_nodes = True
    world.node_tree.nodes.get("Background").inputs["Color"].default_value = (0.65, 0.65, 0.65, 1)
    world.node_tree.nodes.get("Background").inputs["Strength"].default_value = 0.7
    scene.world = world
    for obj in scene.objects:
        if obj.type in {"LIGHT", "CAMERA"}:
            obj.hide_render = True
    camera_data = bpy.data.cameras.new("MMD_Reference_Camera")
    camera_data.type = "ORTHO"
    camera_data.clip_start = 0.001
    camera_data.clip_end = 100
    camera = bpy.data.objects.new("MMD_Reference_Camera", camera_data)
    scene.collection.objects.link(camera)
    scene.camera = camera
    lights = []
    for name, power, size in (("Key", 35.0, 1.0), ("Fill", 18.0, 1.0)):
        data = bpy.data.lights.new("MMD_Reference_" + name, "AREA")
        data.energy = power
        data.shape = "DISK"
        data.size = size
        obj = bpy.data.objects.new(data.name, data)
        scene.collection.objects.link(obj)
        lights.append(obj)
    return scene, camera, lights


def setup_model(scene, camera, lights, spec):
    collection_name, arm_name, mesh_name, face_material, folder = spec
    rig = bpy.data.objects[arm_name]
    mesh = bpy.data.objects[mesh_name]
    # Isolate geometry, retaining original material nodes and armature constraints.
    for obj in scene.objects:
        if obj.type == "MESH":
            obj.hide_render = obj != mesh
    for collection in bpy.data.collections:
        if collection.name in {m[0] for m in MODELS}:
            collection.hide_render = collection.name != collection_name
        elif collection.name.startswith("RigidBody"):
            collection.hide_render = True
    for layer in scene.view_layers:
        layer.use = layer == bpy.context.view_layer
        def show_collections(lc):
            if lc.name == collection_name:
                lc.exclude = False
                lc.hide_viewport = False
            for child in lc.children:
                show_collections(child)
        show_collections(layer.layer_collection)
    rig.hide_set(False)
    mesh.hide_set(False)
    reset_keys(mesh)
    bpy.context.view_layer.update()
    head = rig.pose.bones.get("頭")
    if head is None:
        raise RuntimeError(f"No 頭 bone: {collection_name}")
    head_position = rig.matrix_world @ head.head
    up = (rig.matrix_world.to_3x3() @ (head.tail - head.head)).normalized()
    # Eye bones point toward the front even where the head bone has different roll.
    eye_bones = [rig.pose.bones.get(n) for n in ("目.L", "目.R")]
    eyes = [b for b in eye_bones if b is not None]
    forward = sum((rig.matrix_world.to_3x3() @ (b.tail - b.head) for b in eyes), Vector()) if eyes else Vector((0, -1, 0))
    forward -= up * forward.dot(up)
    forward.normalize()
    indices = set()
    material_indices = {i for i, m in enumerate(mesh.data.materials) if m and m.name == face_material}
    for poly in mesh.data.polygons:
        if poly.material_index in material_indices:
            indices.update(poly.vertices)
    if not indices:
        raise RuntimeError(f"Face material missing: {collection_name}, {face_material}")
    coords = [mesh.matrix_world @ mesh.data.vertices[i].co for i in indices]
    low = Vector(tuple(min(v[i] for v in coords) for i in range(3)))
    high = Vector(tuple(max(v[i] for v in coords) for i in range(3)))
    target = (low + high) * 0.5
    target.x = head_position.x
    height = high.z - low.z
    width = high.x - low.x
    scale = max(height * 1.22, width * 1.32, 0.2)
    camera.location = target + forward * max(scale * 4.0, 1.2)
    camera.rotation_euler = (target - camera.location).to_track_quat("-Z", "Y").to_euler()
    camera.data.ortho_scale = scale
    right = forward.cross(up).normalized()
    for light, offset in zip(lights, ((-0.35, 0.7, 0.4), (0.4, 0.65, 0.1))):
        light.location = target + right * offset[0] + forward * offset[1] + up * offset[2]
        light.rotation_euler = (target - light.location).to_track_quat("-Z", "Y").to_euler()
    folder_path = OUT / "images" / folder
    folder_path.mkdir(parents=True, exist_ok=True)
    metadata = {
        "collection": collection_name, "armature": arm_name, "mesh": mesh_name,
        "head_bone": "頭", "head_world": list(head_position),
        "face_material": face_material, "face_bounds": [list(low), list(high)],
        "camera_location": list(camera.location), "camera_target": list(target),
        "orthographic_scale": scale, "folder": folder,
        "source_shape_key_names": [k.name for k in mesh.data.shape_keys.key_blocks],
        "expressions": [],
    }
    print("MMD_SETUP", json.dumps(metadata, ensure_ascii=False), flush=True)
    return mesh, folder_path, metadata


def render_one(scene, mesh, key, path, context_weights=None):
    reset_keys(mesh)
    if key is not None:
        key.slider_max = max(1.0, key.slider_max)
        key.value = 1.0
    for name, weight in (context_weights or {}).items():
        mesh.data.shape_keys.key_blocks[name].value = weight
    mesh.data.update()
    bpy.context.view_layer.update()
    scene.render.filepath = str(path)
    bpy.ops.render.render(write_still=True)
    print("MMD_RENDERED", str(path), flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--preview", action="store_true")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--contexts", action="store_true")
    parser.add_argument("--model")
    args = parser.parse_args(sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else [])
    scene, camera, lights = configure_scene()
    for spec in MODELS:
        if args.model and args.model != spec[0]:
            continue
        if args.contexts and spec[0] not in CONTEXT_EXAMPLES:
            continue
        mesh, folder, metadata = setup_model(scene, camera, lights, spec)
        if args.contexts:
            metadata_path = OUT / (spec[4] + "_renders.json")
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
            metadata["context_examples"] = []
            for primary, context_name in CONTEXT_EXAMPLES[spec[0]]:
                path = folder / ("context_" + safe_name(primary + "+" + context_name) + ".png")
                render_one(scene, mesh, mesh.data.shape_keys.key_blocks[primary], path, {context_name: 1.0})
                baseline = next(e["path"] for e in metadata["expressions"] if e["name"] == context_name)
                metadata["context_examples"].append({
                    "name": primary, "context_weights": {context_name: 1.0},
                    "primary_value": 1.0, "baseline_path": baseline,
                    "path": path.relative_to(OUT).as_posix(),
                })
            save_json(metadata_path, metadata)
            continue
        start = time.time()
        render_one(scene, mesh, None, folder / "000_基准.png")
        metadata["neutral"] = (folder / "000_基准.png").relative_to(OUT).as_posix()
        if args.all:
            keys = [k for k in mesh.data.shape_keys.key_blocks if k != mesh.data.shape_keys.reference_key and not k.name.startswith("mmd_sdef_")]
            for i, key in enumerate(keys, 1):
                path = folder / f"{i:03d}_{safe_name(key.name)}.png"
                if not path.exists():
                    render_one(scene, mesh, key, path)
                metadata["expressions"].append({
                    "index": i, "name": key.name, "value": 1.0,
                    "path": path.relative_to(OUT).as_posix(),
                })
                save_json(OUT / (spec[4] + "_renders.json"), metadata)
        metadata["seconds"] = round(time.time() - start, 2)
        save_json(OUT / (spec[4] + "_renders.json"), metadata)
    print("MMD_COMPLETE", flush=True)


main()
