
bl_info = {
    "name": "GLB Toolbox",
    "author": "Twiceeeec",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > Toolbox",
    "category": "Import-Export",
}

import bpy, os

def asset_dir():
    return os.path.join(os.path.dirname(__file__), "assets")

class TOOLBOX_OT_import(bpy.types.Operator):
    bl_idname = "toolbox.import_glb"
    bl_label = "Import GLB"

    file_name: bpy.props.StringProperty()

    def execute(self, context):
        path = os.path.join(asset_dir(), self.file_name)
        bpy.ops.import_scene.gltf(filepath=path)
        return {'FINISHED'}

class TOOLBOX_PT_panel(bpy.types.Panel):
    bl_label = "ToolBox"
    bl_idname = "TOOLBOX_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'ToolBox'

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.prop(scene, "toolbox_search", text="", icon='VIEWZOOM')

        search = scene.toolbox_search.lower()
        files = sorted([f for f in os.listdir(asset_dir()) if f.endswith(".glb")])

        for f in files:
            if search and search not in f.lower():
                continue
            op = layout.operator("toolbox.import_glb", text=f.replace(".glb",""), icon='MESH_CUBE')
            op.file_name = f

classes = (TOOLBOX_OT_import, TOOLBOX_PT_panel)

def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.Scene.toolbox_search = bpy.props.StringProperty(name="Search")

def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)
    del bpy.types.Scene.toolbox_search

if __name__ == "__main__":
    register()
