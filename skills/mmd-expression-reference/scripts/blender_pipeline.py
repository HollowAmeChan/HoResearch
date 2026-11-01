"""Blender-side worker; invoked by run.py, never inside a live user scene."""
import hashlib
import json
from pathlib import Path
import sys
import time

import addon_utils
import bpy
from mathutils import Vector

JOB = json.loads(Path(sys.argv[sys.argv.index("--") + 1]).read_text(encoding="utf-8"))
OUT = Path(JOB["output"])
PRIVATE = Path(JOB["private"])


def save_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")


def enable_mmd():
    sys.path.insert(0, JOB["addons"])
    bpy.utils.refresh_script_paths()
    addon_utils.enable("mmd_tools", default_set=False, persistent=False)
    import mmd_tools
    if not hasattr(bpy.types.Object, "mmd_root"):
        raise RuntimeError("mmd_tools 未成功注册。")
    return mmd_tools


def import_model():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)
    bpy.ops.mmd_tools.import_model(
        filepath=JOB["source"], types={"MESH", "ARMATURE", "MORPHS", "DISPLAY"},
        scale=0.08, clean_model=True, remove_doubles=False, rename_bones=True,
        log_level="WARNING", save_log=False,
    )
    from mmd_tools.core.model import Model
    roots = [o for o in bpy.context.scene.objects if getattr(o, "mmd_type", None) == "ROOT"]
    if len(roots) != 1:
        raise RuntimeError(f"导入后应有一个 MMD root，实际 {len(roots)}。")
    model = Model(roots[0])
    meshes = list(model.meshes())
    if not meshes or model.armature() is None:
        raise RuntimeError("导入器未生成有效网格和骨架。")
    missing = []
    for material in model.materials():
        if material and material.node_tree:
            for node in material.node_tree.nodes:
                if node.type == "TEX_IMAGE" and node.image:
                    image = node.image
                    if image.source == "FILE" and not image.packed_file and not Path(bpy.path.abspath(image.filepath)).is_file():
                        missing.append(image.name)
    if missing:
        raise RuntimeError("缺失贴图：" + ", ".join(sorted(set(missing))))
    return model, meshes


def bind_morphs(model):
    model.morph_slider.bind()
    control = model.morph_slider.placeholder(binded=True)
    if not control or not control.data.shape_keys:
        raise RuntimeError("mmd_tools morph slider 绑定失败。")
    control.hide_render = True
    keys = control.data.shape_keys.key_blocks
    morphs = []
    for kind in ("group", "vertex", "bone", "uv", "material"):
        for item in getattr(model.rootObject().mmd_root, kind + "_morphs"):
            if not keys.get(item.name):
                raise RuntimeError(f"未绑定 {kind} morph：{item.name}")
            morphs.append({"name": item.name, "type": kind, "category": str(item.category)})
    if len({m["name"] for m in morphs}) != len(morphs):
        raise RuntimeError("不同类型的 morph 名称冲突，不能用同一滑块冒充多个表情。")
    if Path(JOB["source"]).suffix.lower() == ".pmx":
        from mmd_tools.core import pmx
        raw = pmx.load(JOB["source"])
        expected = [m.name for m in raw.morphs]
        if len(expected) != len(morphs):
            raise RuntimeError(f"源 PMX 有 {len(expected)} 个 morph，已绑定 {len(morphs)} 个；不能标记全部完成。")
        by_name = {m["name"]: m for m in morphs}
        if set(expected) == set(by_name):
            morphs = [by_name[name] for name in expected]
    return control, morphs


def replace_materials(model):
    """Retain the mmd_shader interface and drivers; replace its internal shader."""
    converted = {}
    materials = []
    for mat in model.materials():
        if not mat or not mat.node_tree:
            continue
        shader = mat.node_tree.nodes.get("mmd_shader")
        if shader is None or shader.type != "GROUP":
            raise RuntimeError(f"材质 {mat.name} 没有可适配的 mmd_shader，停止而不是丢弃原材质。")
        old = shader.node_tree
        if old.name not in converted:
            group = old.copy()
            group.name = "MMDShaderDev.ReferenceToon"
            group.nodes.clear()
            nodes, links = group.nodes, group.links
            inputs = nodes.new("NodeGroupInput")
            output = nodes.new("NodeGroupOutput")
            for name in ("Diffuse Color", "Base Tex", "Base Tex Fac", "Alpha", "Base Alpha"):
                if inputs.outputs.get(name) is None:
                    raise RuntimeError(f"MMD 材质接口缺少 {name}。")
            base = nodes.new("ShaderNodeMixRGB")
            base.blend_type = "MULTIPLY"
            links.new(inputs.outputs["Base Tex Fac"], base.inputs[0])
            links.new(inputs.outputs["Diffuse Color"], base.inputs[1])
            links.new(inputs.outputs["Base Tex"], base.inputs[2])
            diffuse = nodes.new("ShaderNodeBsdfDiffuse")
            diffuse.inputs["Color"].default_value = (1, 1, 1, 1)
            rgb = nodes.new("ShaderNodeShaderToRGB")
            links.new(diffuse.outputs[0], rgb.inputs[0])
            ramp = nodes.new("ShaderNodeValToRGB")
            ramp.color_ramp.interpolation = "CONSTANT"
            ramp.color_ramp.elements[0].position = 0.0
            ramp.color_ramp.elements[0].color = (0.6, 0.6, 0.6, 1)
            ramp.color_ramp.elements[1].position = 0.45
            ramp.color_ramp.elements[1].color = (1, 1, 1, 1)
            links.new(rgb.outputs["Color"], ramp.inputs[0])
            shaded = nodes.new("ShaderNodeMixRGB")
            shaded.blend_type = "MULTIPLY"
            shaded.inputs[0].default_value = 1
            links.new(base.outputs[0], shaded.inputs[1])
            links.new(ramp.outputs["Color"], shaded.inputs[2])
            emission = nodes.new("ShaderNodeEmission")
            links.new(shaded.outputs[0], emission.inputs["Color"])
            tex_alpha = nodes.new("ShaderNodeMixRGB")
            links.new(inputs.outputs["Base Tex Fac"], tex_alpha.inputs[0])
            tex_alpha.inputs[1].default_value = (1, 1, 1, 1)
            links.new(inputs.outputs["Base Alpha"], tex_alpha.inputs[2])
            alpha = nodes.new("ShaderNodeMath")
            alpha.operation = "MULTIPLY"
            links.new(inputs.outputs["Alpha"], alpha.inputs[0])
            links.new(tex_alpha.outputs[0], alpha.inputs[1])
            transparent = nodes.new("ShaderNodeBsdfTransparent")
            mix = nodes.new("ShaderNodeMixShader")
            links.new(alpha.outputs[0], mix.inputs[0])
            links.new(transparent.outputs[0], mix.inputs[1])
            links.new(emission.outputs[0], mix.inputs[2])
            links.new(mix.outputs[0], output.inputs[0])
            converted[old.name] = group
        shader.node_tree = converted[old.name]
        mat.surface_render_method = "DITHERED"
        materials.append(mat.name)
    return materials


def japanese_name(bone):
    return getattr(getattr(bone, "mmd_bone", None), "name_j", "") or bone.name


def find_head(rig):
    if JOB["head_bone"]:
        bone = rig.pose.bones.get(JOB["head_bone"])
        if bone:
            return bone
        raise RuntimeError(f"找不到指定头骨 {JOB['head_bone']}。")
    for name in ("頭", "Head", "head"):
        bone = rig.pose.bones.get(name)
        if bone:
            return bone
    bone = next((b for b in rig.pose.bones if japanese_name(b) == "頭"), None)
    if bone:
        return bone
    raise RuntimeError("找不到頭 / Head 头骨，不能把世界原点当作脸部。")


def framing(rig, meshes, head):
    position = rig.matrix_world @ head.head
    up = (rig.matrix_world.to_3x3() @ (head.tail - head.head)).normalized()
    length = (rig.matrix_world @ head.tail - position).length
    if length < 0.001:
        raise RuntimeError("头骨长度无效。")
    eyes = [b for b in rig.pose.bones if japanese_name(b) in {"左目", "右目"} or b.name in {"目.L", "目.R", "左目", "右目"}]
    forward = sum((rig.matrix_world.to_3x3() @ (b.tail - b.head) for b in eyes), Vector()) if eyes else Vector((0, -1, 0))
    forward = (forward - up * forward.dot(up)).normalized()
    right = forward.cross(up).normalized()
    face_candidates = []
    head_points = []
    bone_names = {head.name} | {b.name for b in head.children_recursive if not any(s in japanese_name(b).lower() for s in ("髪", "hair", "ツイン"))}
    for mesh in meshes:
        groups = {g.index for g in mesh.vertex_groups if g.name in bone_names}
        points = {}
        for vertex in mesh.data.vertices:
            if any(g.group in groups and g.weight > 0.3 for g in vertex.groups):
                p = mesh.matrix_world @ vertex.co
                d = p - position
                if abs(d.dot(right)) < 1.15 * length and -0.7 * length < d.dot(up) < 1.65 * length and abs(d.dot(forward)) < 1.7 * length:
                    points[vertex.index] = p
                    head_points.append(p)
        for i, mat in enumerate(mesh.data.materials):
            if not mat or not any(t in mat.name.lower() for t in ("face", "顔", "脸", "顏")):
                continue
            indices = {v for poly in mesh.data.polygons if poly.material_index == i for v in poly.vertices}
            coords = [points[v] for v in indices if v in points]
            if not coords:
                continue
            h = max((p - position).dot(up) for p in coords) - min((p - position).dot(up) for p in coords)
            w = max((p - position).dot(right) for p in coords) - min((p - position).dot(right) for p in coords)
            if h > length * 0.4 and w > length * 0.5:
                face_candidates.append((h * w, coords))
    coords = max(face_candidates, key=lambda x: x[0])[1] if face_candidates else head_points
    if not coords:
        raise RuntimeError("无法从脸部材质或头骨权重获取有效取景范围。")
    bounds = [(min((p - position).dot(axis) for p in coords), max((p - position).dot(axis) for p in coords)) for axis in (right, forward, up)]
    target = position + sum((axis * ((lo + hi) / 2) for axis, (lo, hi) in zip((right, forward, up), bounds)), Vector())
    target += right * JOB["target_offset"][0] + forward * JOB["target_offset"][1] + up * JOB["target_offset"][2]
    scale = JOB["ortho_scale"] or max((bounds[0][1] - bounds[0][0]) * 1.32, (bounds[2][1] - bounds[2][0]) * 1.22)
    return target, scale, forward, up, right


def setup_scene(model, meshes):
    scene = bpy.context.scene
    rig = model.armature()
    head = find_head(rig)
    bpy.context.view_layer.update()
    target, scale, forward, up, right = framing(rig, meshes, head)
    scene.render.engine = "BLENDER_EEVEE_NEXT"
    scene.eevee.taa_render_samples = JOB["samples"]
    scene.render.resolution_x = scene.render.resolution_y = JOB["size"]
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGBA"
    scene.render.film_transparent = True
    scene.render.use_compositing = scene.render.use_sequencer = False
    scene.view_settings.view_transform = "Standard"
    scene.view_settings.look = "None"
    world = bpy.data.worlds.new("ReferenceWorld")
    world.use_nodes = True
    world.node_tree.nodes["Background"].inputs["Color"].default_value = (0.65, 0.65, 0.65, 1)
    world.node_tree.nodes["Background"].inputs["Strength"].default_value = 0.7
    scene.world = world
    camera = bpy.data.objects.new("ReferenceCamera", bpy.data.cameras.new("ReferenceCamera"))
    scene.collection.objects.link(camera)
    camera.data.type = "ORTHO"
    camera.data.ortho_scale = scale
    camera.data.clip_start = 0.001
    camera.data.clip_end = 100
    camera.location = target + forward * max(scale * 4, 1.2)
    camera.rotation_euler = (target - camera.location).to_track_quat("-Z", "Y").to_euler()
    scene.camera = camera
    for name, power, offset in (("Key", 35, (-0.35, 0.7, 0.4)), ("Fill", 18, (0.4, 0.65, 0.1))):
        light = bpy.data.objects.new(name, bpy.data.lights.new(name, "AREA"))
        light.data.energy = power
        light.data.size = 1.0
        scene.collection.objects.link(light)
        light.location = target + right * offset[0] + forward * offset[1] + up * offset[2]
        light.rotation_euler = (target - light.location).to_track_quat("-Z", "Y").to_euler()
    for obj in scene.objects:
        if obj.type == "MESH":
            obj.hide_render = obj not in meshes
    return scene, {"bone": head.name, "japanese_name": japanese_name(head), "head_position": list(rig.matrix_world @ head.head), "target": list(target), "orthographic_scale": scale, "camera_location": list(camera.location), "framing_source": "face material or head-weighted vertices"}


def valid_png(path):
    if not path.exists():
        return False
    try:
        image = bpy.data.images.load(str(path), check_existing=False)
        valid = list(image.size) == [JOB["size"], JOB["size"]]
        bpy.data.images.remove(image)
        return valid
    except RuntimeError:
        return False


def main():
    started = time.time()
    mmd = enable_mmd()
    model, meshes = import_model()
    control, morphs = bind_morphs(model)
    materials = replace_materials(model)
    scene, camera = setup_scene(model, meshes)
    settings = {k: JOB[k] for k in ("source_sha256", "material_profile", "head_bone", "ortho_scale", "target_offset", "samples", "size")}
    settings.update(blender=bpy.app.version_string, mmd_tools=str(mmd.bl_info["version"]))
    settings["blender_build"] = bpy.app.build_hash.decode("utf-8", errors="replace")
    settings["pipeline_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    settings["texture_sha256"] = {
        image.name: hashlib.sha256(Path(bpy.path.abspath(image.filepath)).read_bytes()).hexdigest()
        for image in bpy.data.images
        if image.source == "FILE" and Path(bpy.path.abspath(image.filepath)).is_file()
    }
    signature = hashlib.sha256(json.dumps(settings, sort_keys=True).encode()).hexdigest()
    manifest_path = OUT / "manifest.json"
    if manifest_path.exists():
        previous = json.loads(manifest_path.read_text(encoding="utf-8"))
        if previous["signature"] != signature:
            raise RuntimeError("输出目录已有其他输入或设置的结果；请更换 --output / --model-id，避免混用旧图。")
    manifest = {
        "schema": 1, "source_filename": Path(JOB["source"]).name,
        "source_sha256": JOB["source_sha256"], "signature": signature,
        "settings": settings, "camera": camera, "material_profile": JOB["material_profile"],
        "material_limitations": "Reference Toon; not HoToon; sphere/toon textures and specular are not replicated.",
        "converted_materials": materials, "source_morph_count": len(morphs),
        "all_morphs": morphs, "expressions": [], "neutral": "images/000_neutral.png",
        "complete": False, "validation_errors": [],
    }
    image_dir = OUT / "images"
    image_dir.mkdir(exist_ok=True)
    # Stamp the task before the first PNG, so a failed first morph cannot leave
    # an unsigned neutral image that a different job would silently reuse.
    save_json(manifest_path, manifest)
    sliders = control.data.shape_keys.key_blocks
    def render(name, path):
        for key in list(sliders)[1:]:
            key.value = 0
        if name:
            sliders[name].value = 1
        bpy.context.view_layer.update()
        scene.frame_set(scene.frame_current)
        bpy.context.view_layer.update()
        if not valid_png(path):
            scene.render.filepath = str(path)
            bpy.ops.render.render(write_still=True)
        if not valid_png(path):
            raise RuntimeError("输出 PNG 无效：" + str(path))
        print("MMD_REFERENCE_RENDERED", name or "neutral", str(path), flush=True)
    render(None, OUT / manifest["neutral"])
    if JOB["preview"]:
        by_name = {m["name"]: m for m in morphs}
        selected = [by_name[n] for n in ("まばたき", "あ", "笑い") if n in by_name] or morphs[:3]
    else:
        selected = morphs
    for entry in selected:
        index = morphs.index(entry) + 1
        filename = f"{index:03d}_{hashlib.sha256(entry['name'].encode()).hexdigest()[:12]}.png"
        path = image_dir / filename
        render(entry["name"], path)
        manifest["expressions"].append({**entry, "index": index, "value": 1.0, "path": path.relative_to(OUT).as_posix()})
        save_json(manifest_path, manifest)
    for key in list(sliders)[1:]:
        key.value = 0
    bpy.context.view_layer.update()
    bpy.ops.file.pack_all()
    bpy.ops.wm.save_as_mainfile(filepath=str(PRIVATE / "working.blend"))
    manifest["complete"] = not JOB["preview"] and len(manifest["expressions"]) == len(morphs)
    manifest["seconds"] = round(time.time() - started, 2)
    save_json(manifest_path, manifest)
    print("MMD_REFERENCE_COMPLETE", manifest["complete"], flush=True)


main()
