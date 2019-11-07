#coding= utf-8
import time,math
# import numpy as np
import sys
# sys.path.append('C:\\Users\\apl\\Anaconda3\\Library\\bin')
sys.path.append('C:\\Users\\ap\\anaconda3\\Library\\bin')

import FreeCAD as App
import FreeCADGui as Gui
import Part, math

Gui.showMainWindow() ##只有showMainWindow 之后能够调用GUI的所有功能
App.newDocument("Unnamed")
App.setActiveDocument("Unnamed")
App.ActiveDocument=App.getDocument("Unnamed")
Gui.ActiveDocument=Gui.getDocument("Unnamed")
# Gui.activeDocument().activeView().viewDefaultOrientation()
Gui.activateWorkbench("PartWorkbench")
# Gui.showMainWindow() ##只有showMainWindow 之后能够调用GUI的所有功能
# doc = App.newDocument('Unnamed')
# box = Part.makeBox(0.1,0.1,0.1)
# Part.show(box)
# box = doc.addObject("Part::Box", "Shape")
x = 0
y = 0
z = 0
n_x = 0
n_y = 0
n_z = 0
r_x = 0
r_y = 0
r_z = 0
Rx=0
Ry=0
Rz=0
radius=5
box_l=10
cone_r=5
D_lable=" "
viewface=" "
D_face=" "
D_angel=0
special_points=[]
def make_line(p1,p2):
    object=Part.makeLine(p1,p2)
    Part.show(object)
    App.ActiveDocument.recompute()
    Gui.activeDocument().activeView().viewAxonometric()
    Gui.SendMsgToActiveView("ViewFit")
    return object

make_line((0,0,0),(30,0,0))
make_line((0,0,0),(0,30,0))
make_line((0,0,0),(0,0,30))

#绘制一个立方体
def make_cube():
    App.ActiveDocument.addObject("Part::Box","Box")
    App.ActiveDocument.ActiveObject.Label = "立方体"
    App.ActiveDocument.recompute()
    Gui.activeDocument().activeView().viewAxonometric()
    Gui.SendMsgToActiveView("ViewFit")
    # time.sleep(2)
    # App.getDocument("Unnamed").getObject("Box").Length = '5 mm'
    # App.ActiveDocument.recompute()
    # Gui.SendMsgToActiveView("ViewFit")

#绘制一个圆柱体
def make_cylinder():
    App.ActiveDocument.addObject("Part::Cylinder", "Cylinder")
    App.ActiveDocument.ActiveObject.Label = "圆柱体"
    App.ActiveDocument.recompute()
    Gui.activeDocument().activeView().viewAxonometric()
    Gui.SendMsgToActiveView("ViewFit")
#绘制一个球体
def make_sphere():
    obj=App.ActiveDocument.addObject("Part::Sphere", "Sphere")
    App.ActiveDocument.ActiveObject.Label = "球体"
    App.ActiveDocument.recompute()
    Gui.activeDocument().activeView().viewAxonometric()
    Gui.SendMsgToActiveView("ViewFit")
    # App.getDocument("Unnamed").getObject("Sphere").Placement = App.Placement(App.Vector(-13, 5, 5),
    #                                                                                App.Rotation(App.Vector(0, 0, 1), 0))
    # App.getDocument("Unnamed").getObject("Sphere").Radius = '3 mm'

    # time.sleep(4)
    # App.ActiveDocument.removeObject("球体")
    # App.getDocument("Unnamed").removeObject("Sphere")
    # App.getDocument("Unnamed").recompute()
    # Gui.SendMsgToActiveView("ViewFit")
    # time.sleep(5)
#绘制一个圆锥体
def make_cone():
    App.ActiveDocument.addObject("Part::Cone", "Cone")
    App.ActiveDocument.ActiveObject.Label = "圆锥体"
    App.getDocument("Unnamed").getObject("Cone").Radius1 = '5 mm'
    App.getDocument("Unnamed").getObject("Cone").Radius2 = '0 mm'
    App.ActiveDocument.recompute()
    Gui.activeDocument().activeView().viewAxonometric()
    Gui.SendMsgToActiveView("ViewFit")
    # time.sleep(3)


# #三维空间平移立体对象
# def move_object_3D(object_3D,x,y,z):
#     #FreeCAD.getDocument("Unnamed").getObject("Box").Placement = App.Placement(App.Vector(10,0,0),App.Rotation(App.Vector(0,0,1),0))
#     object_3D.Placement = App.Placement(App.Vector(x,y,z), App.Rotation(App.Vector(0, 0, 1), 0))


#平移对象

# def move_object(object_lable,vector):
#     print("got data")
#     global x, y, z,D_lable
#     if D_lable!=object_lable:
#         x=0
#         y=0
#         z=0
#     n_x = x + vector[0]*4
#     n_y = y + vector[1]*4
#     n_z = z + vector[2]*4
#     App.getDocument("Unnamed").getObject(object_lable).Placement = App.Placement(App.Vector(-n_x,n_z,-n_y),App.Rotation(App.Vector(0,0,1),0))
#     # return n_x,n_y,n_z
#     # Gui.SendMsgToActiveView("ViewFit")
#     Gui.ActiveDocument.update()
#     # App.ActiveDocument.recompute()
#     # Gui.SendMsgToActiveView("ViewFit")#此行记得注释掉
#     x=n_x
#     y=n_y
#     z=n_z
#     D_lable = object_lable
#     return x,y,z
#

#平移对象，带有视角切换

#11/6之前的平移模型，配合旋转使用
# def move_object(object_lable,viewface,vector):
#     global x, y, z, D_lable, n_x, n_y, n_z
#     print(object_lable)
#     print("viewface:",viewface)
#
#     if D_lable!=object_lable:
#         x=0
#         y=0
#         z=0
#     if viewface=='Front':
#         n_x = x - vector[0]*4
#         n_y = y
#         n_z = z - vector[1]*4
#     elif viewface == 'Left':
#         n_x = x
#         n_y = y + vector[0]*4
#         n_z = z - vector[1]*4
#     elif viewface == 'Top':
#         n_x = x - vector[0]*4
#         n_y = y - vector[1]*4
#         n_z = z
#     elif viewface=='Axonometric':
#         n_x = x - vector[2] * 4
#         n_y = y - vector[0] * 4
#         n_z = z - vector[1] * 4
#     print(n_x,n_y,n_z)
#     App.getDocument("Unnamed").getObject(object_lable).Placement = App.Placement(App.Vector(n_x,n_y,n_z),
#                                                       App.Rotation(App.Vector(r_x, r_y, r_z),D_angel))
#     Gui.ActiveDocument.update()
#     Gui.SendMsgToActiveView("ViewFit")  ###测试使用，正常注释
#     x=n_x
#     y=n_y
#     z=n_z
#
#     D_lable = object_lable
#     return x,y,z,D_lable
# #旋转对象--11/6之前的模型
# #可以记录各轴的旋转量
# def rotate_object(object_lable,viewface,angel):
#     global D_face,D_angel,r_x, r_y, r_z
#     if D_face != viewface:
#         D_angel = 0
#     if viewface == 'Front':
#         print('front')
#         D_angel = D_angel - angel * 10
#         # r_x = 0
#         r_y = 1
#         # r_z = 0
#     elif viewface == 'Left':
#         print('left')
#         D_angel = D_angel - angel * 10
#         r_x = 1
#         # r_y = 0
#         # r_z = 0
#     elif viewface == 'Top':
#         print('top')
#         D_angel = D_angel + angel * 10
#         # r_x = 0
#         # r_y = 0
#         r_z = 1
#     elif viewface == 'Axonometric':
#         print('ax')
#         # r_x = 0
#         # r_y = 0
#         # r_z = 0
#         D_angel = D_angel - angel * 10
#     App.getDocument("Unnamed").getObject(object_lable).Placement = App.Placement(App.Vector(n_x, n_y, n_z),
#                                                       App.Rotation(App.Vector(r_x, r_y, r_z), D_angel))
#     Gui.ActiveDocument.update()
#     # Gui.SendMsgToActiveView("ViewFit") ###测试使用，正常注释
#     return D_angel


#缩放对象


#平移11/6
def move_object(object_lable,viewface,vector):
    global x, y, z, D_lable, n_x, n_y, n_z
    # vector=4*vector
    print(object_lable)
    print("viewface:",viewface)
    if D_lable!=object_lable:
        x=0
        y=0
        z=0
    if viewface=='Front':
        n_x = x - vector[0]
        n_y = y
        n_z = z - vector[1]
    elif viewface == 'Left':
        n_x = x
        n_y = y + vector[0]
        n_z = z - vector[1]
    elif viewface == 'Top':
        n_x = x - vector[0]
        n_y = y - vector[1]
        n_z = z
    elif viewface=='Axonometric':
        n_x = x - vector[2]
        n_y = y - vector[0]
        n_z = z - vector[1]
    print(n_x,n_y,n_z)
    App.getDocument("Unnamed").getObject(object_lable).Placement = App.Placement(
                            App.Vector(n_x,n_y,n_z),App.Rotation(Rx,Ry,Rz) ,App.Vector(0,0,0))
    Gui.ActiveDocument.update()
    # Gui.SendMsgToActiveView("ViewFit")  ###测试使用，正常注释
    x=n_x
    y=n_y
    z=n_z

    D_lable = object_lable
    return x,y,z,D_lable

#旋转11/6
def rotate_object(object_lable,delta):
    print("----------------",delta)
    global Rx,Ry,Rz
    Rx = Rx + delta[0]
    Ry = Ry + delta[1]
    Rz = Rz + delta[2]
    App.getDocument("Unnamed").getObject(object_lable).Placement = App.Placement(App.Vector(0,0,0),
        App.Rotation(delta[0],delta[1],delta[2]),App.Vector(x+box_l/2,y+box_l/2,z+box_l/2)).multiply(App.getDocument("Unnamed").getObject(object_lable).Placement)
    App.ActiveDocument.recompute()
    # Gui.ActiveDocument.update()
    # Gui.SendMsgToActiveView("ViewFit")  ###测试使用，正常注释

def zoom_object(object_lable,scale):
    global radius,box_l,cone_r

    if object_lable == "Sphere":
        radius=radius * scale
        App.getDocument("Unnamed").getObject("Sphere").Radius = radius
        Gui.ActiveDocument.update()
        App.ActiveDocument.recompute()

    if object_lable == "Box":
        box_l = box_l * scale
        App.getDocument("Unnamed").getObject("Box").Length = box_l
        App.getDocument("Unnamed").getObject("Box").Width  = box_l
        App.getDocument("Unnamed").getObject("Box").Height = box_l
        Gui.ActiveDocument.update()
    if object_lable == "Cone":
        cone_r = cone_r * scale
        App.getDocument("Unnamed").getObject("Cone").Radius1 = cone_r
        App.getDocument("Unnamed").getObject("Cone").Radius2 = 0
        App.getDocument("Unnamed").getObject("Cone").Height = (cone_r*2)
        Gui.ActiveDocument.update()
        # Gui.SendMsgToActiveView("ViewFit")
    return radius,box_l,cone_r

#删除对象
def delete_object(object_lable):
    App.getDocument("Unnamed").removeObject(object_lable)
    Gui.ActiveDocument.update()
    App.getDocument("Unnamed").recompute()

#切换观测面
def change_viewface(viewface):
    global D_face
    if D_face != viewface:
        if viewface=='Front':
            print('front')
            Gui.activeDocument().activeView().viewFront()
            # Gui.activeDocument().update()
            # App.getDocument("Unnamed").recompute()
            Gui.SendMsgToActiveView("ViewFit")
            Gui.SendMsgToActiveView("ViewFit")
        elif viewface=='Left':
            print('left')
            Gui.activeDocument().activeView().viewLeft()
            # Gui.activeDocument().update()
            # App.getDocument("Unnamed").recompute()
            Gui.SendMsgToActiveView("ViewFit")
            Gui.SendMsgToActiveView("ViewFit")
        elif viewface=='Top':
            print('top')
            Gui.activeDocument().activeView().viewTop()
            # App.getDocument("Unnamed").recompute()
            # Gui.activeDocument().update()
            Gui.SendMsgToActiveView("ViewFit")
            Gui.SendMsgToActiveView("ViewFit")
        elif viewface=='Axonometric':
            print('ax')
            Gui.activeDocument().activeView().viewAxonometric()
            # App.getDocument("Unnamed").recompute()
            # Gui.activeDocument().update()
            Gui.SendMsgToActiveView("ViewFit")
            Gui.SendMsgToActiveView("ViewFit")
        D_face=viewface

    return  D_face

def keep_points(object_lable):
    if object_lable=='Box':
        special_points.append((n_x, n_y, n_z))
    elif object_lable==' ':
        special_points.append()


# make_cube()
# # make_sphere()
# # change_viewface(viewface='Axonometric')
# # time.sleep(3)
# # # make_sphere()
# i=1
# while i<10:
#     move_object("Box",'Axonometric',(-1,-1,-1))
#     rotate_object("Box", (-1,-1,-1))
#     i=i+1
#
# time.sleep(5)
#
# i=0
# while i<10:
#     rotate_object("Box",'Left',2)
#     i=i+1
# while i<20:
#     rotate_object("Box",'Left',-4)
#     i=i+1


# change_viewface(viewface='Top')
# time.sleep(3)
# change_viewface(viewface='Front')
# time.sleep(3)
# change_viewface(viewface='Left')
# time.sleep(3)
# change_viewface(viewface='Axonometric')
# time.sleep(3)
# make_sphere()
# i=1
# while i<10:
#     move_object("Box",(1,0,0))
#     i=i+1
# make_cube()
# time.sleep(3)
# make_sphere()
# make_sphere()
# App.getDocument("Unnamed").removeObject("Sphere")
# App.getDocument("Unnamed").recompute()
# Gui.SendMsgToActiveView("ViewFit")
# make_sphere()
# time.sleep(5)
# make_cone()
# time.sleep(5)