import bpy
from bpy.types import Menu

class SculptMaskClear(bpy.types.Operator):
    '''Clears the current mask.'''
    bl_idname = "sculpt.mask_clear"
    bl_label = "Clear Mask"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.paint.mask_flood_fill(mode='VALUE', value=0)
        return {'FINISHED'}

class SculptMaskInvert(bpy.types.Operator):
    '''Clears the current mask.'''
    bl_idname = "sculpt.mask_invert"
    bl_label = "Clear Mask"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.paint.mask_flood_fill(mode='INVERT')
        return {'FINISHED'}

class SculptMaskHide(bpy.types.Operator):
    '''Hides parts of the mesh with a mask.'''
    bl_idname = "sculpt.mask_hide"
    bl_label = "Hide Mask"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.paint.hide_show(action='HIDE', area='MASKED')
        return {'FINISHED'}

class SculptMaskShow(bpy.types.Operator):
    '''Hides parts of the mesh with a mask.'''
    bl_idname = "sculpt.mask_show"
    bl_label = "Hide Mask"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.paint.hide_show(action='SHOW', area='ALL')
        return {'FINISHED'}

class SculptMaskLasso(bpy.types.Operator):
    '''Hides parts of the mesh with a mask.'''
    bl_idname = "sculpt.mask_lasso"
    bl_label = "Hide Mask"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.paint.mask_lasso_gesture()
        return {'FINISHED'}

class SculptMaskBorder(bpy.types.Operator):
    '''Hides parts of the mesh with a mask.'''
    bl_idname = "sculpt.mask_border"
    bl_label = "Hide Mask"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.view3d.select_border()
        return {'FINISHED'}


class PieSculptMaskStandard(Menu):
    bl_idname = "pie.maskstandard"
    bl_label = "Mask Tools"

    def draw(self, context):
        print("Drawing Pie")
        layout = self.layout
        pie = layout.menu_pie()
        # 4 - LEFT
        pie.operator("sculpt.mask_lasso", text="Lasso Mask")
        # 6 - RIGHT
        pie.operator("sculpt.mask_clear", text="Clear Mask")
        # 2 - BOTTOM
        pie.operator("sculpt.mask_invert", text="Invert Mask")
        # 8 - TOP
        pie.operator("sculpt.mask_border", text="Rectangle Mask")
        # 7 - TOP - LEFT
        # 1 - BOTTOM - LEFT
        pie.operator("sculpt.mask_hide", text="Hide Mask")
        # 9 - TOP - RIGHT
        pie.operator("sculpt.mask_show", text="Show All")
        # 3 - BOTTOM - RIGHT
