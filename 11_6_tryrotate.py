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
D_lable=" "
x=0
y=0
z=0
Rx=0
Ry=0
Rz=0
radius=5
box_l=10
cone_r=5

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
    Gui.SendMsgToActiveView("ViewFit")

#平移
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
    Gui.SendMsgToActiveView("ViewFit")  ###测试使用，正常注释
    x=n_x
    y=n_y
    z=n_z

    D_lable = object_lable
    return x,y,z,D_lable

#旋转
def rotate_object(object_lable,delta):

    global Rx,Ry,Rz
    Rx = Rx + delta[0]
    Ry = Ry + delta[1]
    Rz = Rz + delta[2]
    App.getDocument("Unnamed").getObject(object_lable).Placement = App.Placement(App.Vector(0,0,0),
        App.Rotation(delta[0],delta[1],delta[2]),App.Vector(x+box_l/2,y+box_l/2,z+box_l/2)).multiply(App.getDocument("Unnamed").getObject(object_lable).Placement)
    App.ActiveDocument.recompute()
    Gui.ActiveDocument.update()
    Gui.SendMsgToActiveView("ViewFit")  ###测试使用，正常注释

#缩放

def zoom_object(object_lable, scale):
    global radius, box_l, cone_r

    if object_lable == "Sphere":
        radius = radius * scale
        App.getDocument("Unnamed").getObject("Sphere").Radius = radius
        Gui.ActiveDocument.update()
        App.ActiveDocument.recompute()

    if object_lable == "Box":
        box_l = box_l * scale
        App.getDocument("Unnamed").getObject("Box").Length = box_l
        App.getDocument("Unnamed").getObject("Box").Width = box_l
        App.getDocument("Unnamed").getObject("Box").Height = box_l
        Gui.ActiveDocument.update()
    if object_lable == "Cone":
        cone_r = cone_r * scale
        App.getDocument("Unnamed").getObject("Cone").Radius1 = cone_r
        App.getDocument("Unnamed").getObject("Cone").Radius2 = 0
        App.getDocument("Unnamed").getObject("Cone").Height = (cone_r * 2)
        App.ActiveDocument.recompute()
        Gui.ActiveDocument.update()
        Gui.SendMsgToActiveView("ViewFit")  ###测试使用，正常注释
    return radius, box_l, cone_r

def test():
    make_cube()
    move_object("Box", 'Axonometric', (-10, -10, -10))
    # rotate_object("Box", (-10, -10, 0))
    i=1
    while i<10:
        # move_object("Box",'Axonometric',(-1,-1,-1))
        zoom_object("Box",1.1)
        rotate_object("Box", (10,10,0))
        i=i+1

    pla=App.getDocument("Unnamed").getObject("Box").Placement
    print(pla)

    ev = App.getDocument("Unnamed").getObject("Box").Shape.Vertexes
    for e in ev:
        print(e.X,e.Y,e.Z,)
    time.sleep(5)

test()