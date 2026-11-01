import bpy
import json
from pathlib import Path

OUT = Path(__file__).resolve().parents[1]
scene = bpy.context.scene


def point(v):
    return [round(float(x), 6) for x in v]


data = {
    "blender": bpy.app.version_string,
    "source": bpy.data.filepath,
    "engine": scene.render.engine,
    "frame": scene.frame_current,
    "world": scene.world.name if scene.world else None,
    "collections": [],
    "armatures": [],
    "meshes": [],
    "materials": [],
    "node_groups": [],
    "images": [],
}
for col in bpy.data.collections:
    data["collections"].append({
        "name": col.name,
        "hide_render": col.hide_render,
        "objects": [o.name for o in col.objects],
        "children": [c.name for c in col.children],
    })
for obj in scene.objects:
    if obj.type == "ARMATURE":
        bones = []
        for bone in obj.pose.bones:
            if any(t in bone.name for t in ("頭", "首", "目", "Head", "head", "Eye", "eye")):
                bones.append({
                    "name": bone.name,
                    "head": point(obj.matrix_world @ bone.head),
                    "tail": point(obj.matrix_world @ bone.tail),
                    "axes": [point(obj.matrix_world.to_3x3() @ bone.matrix.to_3x3().col[i]) for i in range(3)],
                })
        data["armatures"].append({
            "name": obj.name,
            "collections": [c.name for c in obj.users_collection],
            "location": point(obj.location),
            "rotation": point(obj.rotation_euler),
            "scale": point(obj.scale),
            "bones_count": len(obj.pose.bones),
            "head_bones": bones,
        })
    elif obj.type == "MESH":
        keys = obj.data.shape_keys
        data["meshes"].append({
            "name": obj.name,
            "collections": [c.name for c in obj.users_collection],
            "parent": obj.parent.name if obj.parent else None,
            "armatures": [m.object.name for m in obj.modifiers if m.type == "ARMATURE" and m.object],
            "bounds": [point(obj.matrix_world @ __import__("mathutils").Vector(v)) for v in obj.bound_box],
            "vertices": len(obj.data.vertices),
            "shape_keys": [k.name for k in keys.key_blocks] if keys else [],
            "nonzero_keys": {k.name: k.value for k in keys.key_blocks if k.value != 0.0} if keys else {},
            "drivers": [d.data_path for d in keys.animation_data.drivers] if keys and keys.animation_data else [],
            "materials": [m.name if m else None for m in obj.data.materials],
            "hide_render": obj.hide_render,
            "modifiers": [{"name": m.name, "type": m.type, "render": m.show_render} for m in obj.modifiers],
        })
for mat in bpy.data.materials:
    data["materials"].append({
        "name": mat.name,
        "nodes": [
            {
                "name": n.name,
                "type": n.bl_idname,
                "group": n.node_tree.name if getattr(n, "node_tree", None) else None,
            }
            for n in mat.node_tree.nodes
        ] if mat.node_tree else [],
    })
for group in bpy.data.node_groups:
    data["node_groups"].append({
        "name": group.name,
        "types": sorted(set(n.bl_idname for n in group.nodes)),
    })
for img in bpy.data.images:
    if img.type != "RENDER_RESULT":
        data["images"].append({
            "name": img.name,
            "path": img.filepath,
            "packed": bool(img.packed_file),
            "size": list(img.size),
            "resolved": bpy.path.abspath(img.filepath),
        })
(OUT / "scene_inventory.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print("MMD_INVENTORY", json.dumps({
    "armatures": data["armatures"],
    "meshes": [{"name": m["name"], "keys": len(m["shape_keys"]), "parent": m["parent"], "collections": m["collections"]} for m in data["meshes"]],
    "node_types": sorted({n["type"] for m in data["materials"] for n in m["nodes"]}),
}, ensure_ascii=False), flush=True)
