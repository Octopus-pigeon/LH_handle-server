#coding= utf-8
import time
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
# Gui.activateWorkbench("PartWorkbench")


r_r=5
box_l=10
cone_r=5
x = 0
y = 0
z = 0
D_lable=" "
def make_line(p1,p2):
    object=Part.makeLine(p1,p2)
    Part.show(object)
    App.ActiveDocument.recompute()
    Gui.activeDocument().activeView().viewAxonometric()
    Gui.SendMsgToActiveView("ViewFit")
    return object

make_line((-30,0,0),(30,0,0))
make_line((0,-30,0),(0,30,0))
make_line((0,0,-30),(0,0,30))
#绘制一个立方体
def make_cube():
    App.ActiveDocument.addObject("Part::Box","Box")
    App.ActiveDocument.ActiveObject.Label = "立方体"
    App.ActiveDocument.recompute()
    Gui.SendMsgToActiveView("ViewFit")
    # time.sleep(2)
    # App.getDocument("Unnamed").getObject("Box").Length = '5 mm'
    # App.ActiveDocument.recompute()
    # Gui.SendMsgToActiveView("ViewFit")
    Gui.activeDocument().activeView().viewAxonometric()

#绘制一个球体
def make_sphere():
    obj=App.ActiveDocument.addObject("Part::Sphere", "Sphere")
    App.ActiveDocument.ActiveObject.Label = "球体"
    App.ActiveDocument.recompute()
    Gui.SendMsgToActiveView("ViewFit")

def make_cone():
    App.ActiveDocument.addObject("Part::Cone", "Cone")
    App.ActiveDocument.ActiveObject.Label = "圆锥体"
    App.getDocument("Unnamed").getObject("Cone").Radius1 = '5 mm'
    App.getDocument("Unnamed").getObject("Cone").Radius2 = '0 mm'
    App.getDocument("Unnamed").getObject("Cone").Height = '10 mm'
    App.ActiveDocument.recompute()
    Gui.SendMsgToActiveView("ViewFit")

def move_object(object_lable,vector):
    print("got data")
    print(vector)
    global x, y, z,D_lable
    if D_lable!=object_lable:
        x=0
        y=0
        z=0
    n_x = x + vector[0]*4
    n_y = y + vector[1]*4
    n_z = z + vector[2]*4
    print(n_x,n_y,n_z)
    App.getDocument("Unnamed").getObject(object_lable).Placement = App.Placement(App.Vector(-n_x,n_z,-n_y),App.Rotation(App.Vector(0,0,1),0))
    # return n_x,n_y,n_z
    # Gui.SendMsgToActiveView("ViewFit")
    Gui.ActiveDocument.update()
    # App.ActiveDocument.recompute()
    # Gui.SendMsgToActiveView("ViewFit")
    x=n_x
    y=n_y
    z=n_z
    D_lable=object_lable
    return x,y,z,D_lable

#缩放对象
def zoom_object(object_lable,scale):
    global r_r,box_l,cone_r

    if object_lable=="Sphere":
        r_r=r_r*(1+scale)
        print(r_r)
        App.getDocument("Unnamed").getObject("Sphere").Radius = r_r
        Gui.ActiveDocument.update()
        App.ActiveDocument.recompute()
    elif object_lable == "Box":
        box_l = box_l* (1 + scale)
        App.getDocument("Unnamed").getObject("Box").Length = box_l
        App.getDocument("Unnamed").getObject("Box").Width  = box_l
        App.getDocument("Unnamed").getObject("Box").Height = box_l
        Gui.ActiveDocument.update()
    elif object_lable == "Cone":
        cone_r = cone_r * (1 + scale)
        App.getDocument("Unnamed").getObject("Cone").Radius1 = cone_r
        App.getDocument("Unnamed").getObject("Cone").Radius2 = 0
        App.getDocument("Unnamed").getObject("Cone").Height = (cone_r*2)
        Gui.ActiveDocument.update()
        # Gui.SendMsgToActiveView("ViewFit")
    return r_r,box_l,cone_r
def delete_object(object_lable):
    App.getDocument("Unnamed").removeObject(object_lable)
    Gui.ActiveDocument.update()
    App.getDocument("Unnamed").recompute()
make_sphere()
# make_cube()
# i=0
# print(time)
# while i<10:
#     move_object("Box",[0,1,2])
#     i+=1
#     # time.sleep(0.1)
# j=0
# while j<10:
#     move_object("Sphere", [1, 2, 0])
#     j+=1
# # f_com.make_cube()
# print(time)
# time.sleep(3)
a=0
k=0.1
make_cube()
while a<10:
    zoom_object("Sphere",k)
    move_object("Sphere", [1,0, 0])
    a+=1

make_cone()
delete_object("Box")
time.sleep(3)