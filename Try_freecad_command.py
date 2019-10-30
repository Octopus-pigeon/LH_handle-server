#coding= utf-8
import time
# import numpy as np
import sys
# sys.path.append('C:\\Users\\apl\\Anaconda3\\Library\\bin')
sys.path.append('C:\\Users\\ap\\anaconda3\\Library\\bin')

import FreeCAD as App
import FreeCADGui as Gui
import Part, math
from FreeCAD import Base
Shape_number=["","001","002","003","004","005","006","007","008","009",]
Gui.showMainWindow() ##只有showMainWindow 之后能够调用GUI的所有功能
App.newDocument("Unnamed")
App.setActiveDocument("Unnamed")
App.ActiveDocument=App.getDocument("Unnamed")
Gui.ActiveDocument=Gui.getDocument("Unnamed")
# Gui.activeDocument().activeView().viewDefaultOrientation()
Gui.activateWorkbench("PartWorkbench")
Gui.activeDocument().activeView().viewAxonometric()

#画一个回转面
def make_face():
    V1 = Base.Vector(0,10,0)
    V2 = Base.Vector(30,10,0)
    V3 = Base.Vector(30,-10,0)
    V4 = Base.Vector(0,-10,0)
    VC1 = Base.Vector(-10,0,0)
    C1 = Part.Arc(V1,VC1,V4)
    # and the second one
    VC2 = Base.Vector(40,0,0)
    C2 = Part.Arc(V2,VC2,V3)
    L1 = Part.LineSegment(V1,V2)
    # and the second one
    L2 = Part.LineSegment(V3,V4)
    S1 = Part.Shape([C1,L1,C2,L2])
    W = Part.Wire(S1.Edges)
    P = W.extrude(Base.Vector(0,0,10))
    Part.show(P)
    App.ActiveDocument.recompute()
    Gui.SendMsgToActiveView("ViewFit")
    Gui.SendMsgToActiveView("ViewFit")
    return P

# 画一个圆，makeCircle(radius): Makes a circle with a given radius
def make_circle():
    r=10
    object=Part.makeCircle(r)
    Part.show(object)
    App.ActiveDocument.recompute()
    Gui.SendMsgToActiveView("ViewFit")
    Gui.SendMsgToActiveView("ViewFit")
    return object

# 画一条线，makeLine((x1,y1,z1),(x2,y2,z2)): Makes a line from two points
def make_line():
    p1=(0,0,0)
    p2=(5,5,5)
    object=Part.makeLine(p1,p2)
    Part.show(object)
    App.ActiveDocument.recompute()
    Gui.SendMsgToActiveView("ViewFit")
    Gui.SendMsgToActiveView("ViewFit")
    return object

#画一个多边形，makePolygon(list): Makes a polygon from a list of points
def make_polygon():
    object= Part.makePolygon([Base.Vector(0, 5, 0), Base.Vector(0, 0, 0), Base.Vector(5, 0, 0)])
    Part.show(object)
    App.ActiveDocument.recompute()
    Gui.SendMsgToActiveView("ViewFit")
    Gui.SendMsgToActiveView("ViewFit")
    return object


# 画一个平面，makePlane(length,width): Makes a plane with length and width
def make_plane():
    l=5
    w=10
    object=Part.makePlane(l,w)
    Part.show(object)
    App.ActiveDocument.recompute()
    Gui.SendMsgToActiveView("ViewFit")
    Gui.SendMsgToActiveView("ViewFit")
    return object

#画一个六面体，makeBox(l,w,h): Makes a box located in p and pointing into the direction d with the dimensions (l,w,h)
def make_box():
    l=10
    w=10
    h=10
    object = Part.makeBox(l,w,h)
    Part.show(object)
    App.ActiveDocument.recompute()
    Gui.SendMsgToActiveView("ViewFit")
    Gui.SendMsgToActiveView("ViewFit")
    return object

#画一个圆台，makeCone(radius1,radius2,height): Makes a cone with the given radii and height
def make_cone():
    r1=5
    r2=0
    h=10
    object=Part.makeCone(r1,r2,h)
    Part.show(object)
    App.ActiveDocument.recompute()
    Gui.SendMsgToActiveView("ViewFit")
    Gui.SendMsgToActiveView("ViewFit")
    return object

# 画一个圆柱，makeCylinder(radius,height): Makes a cylinder with a given radius and height.
def make_cylinder():
    r=5
    h=10
    object=Part.makeCylinder(r,h)
    Part.show(object)
    App.ActiveDocument.recompute()
    Gui.SendMsgToActiveView("ViewFit")
    Gui.SendMsgToActiveView("ViewFit")
    return object

#画一个球体，makeSphere(radius): Makes a sphere with a given radius
def make_sphere():
    r=10
    object=Part.makeSphere(r)
    Part.show(object)
    App.ActiveDocument.recompute()
    Gui.SendMsgToActiveView("ViewFit")
    Gui.SendMsgToActiveView("ViewFit")
    return object

#画一个圆环，makeTorus(radius1,radius2): Makes a torus with the given radii
def make_torus():
    r1=10
    r2=2
    object=Part.makeTorus(r1,r2)
    Part.show(object)
    App.ActiveDocument.recompute()
    Gui.SendMsgToActiveView("ViewFit")
    Gui.SendMsgToActiveView("ViewFit")
    return object

#平移对象
def move_object(myshape,shape_number):
    App.getDocument("Unnamed").removeObject("Shape"+shape_number)
    App.getDocument("Unnamed").recompute()
    # Gui.SendMsgToActiveView("ViewFit")
    # Gui.SendMsgToActiveView("ViewFit")
    myshape.translate(Base.Vector(1, 0, 0))
    myshape.rotate(Base.Vector(0, 0, 0),Base.Vector(0, 0, 1),9)
    Part.show(myshape)
    App.getDocument("Unnamed").recompute()
    Gui.SendMsgToActiveView("ViewFit")
    # Gui.SendMsgToActiveView("ViewFit")

#绕Z轴旋转对象
def rotate_object(myshape,shape_number):
    App.getDocument("Unnamed").removeObject("Shape"+shape_number)
    App.getDocument("Unnamed").recompute()
    myshape.rotate(Base.Vector(0, 0, 0),Base.Vector(0, 0, 1),1)
    Part.show(myshape)
    App.getDocument("Unnamed").recompute()

obj=make_box()
i=0
n=1
while i<10:
    move_object(obj,Shape_number[0])
    # rotate_object(obj,Shape_number[0])
    i=i+1
obj1=make_sphere()
while n<10:
    move_object(obj1,Shape_number[1])
    n=n+1
obj2=make_box()
myMat = Base.Matrix()
myMat.scale(3,0,0)
myShape = obj2.transformGeometry(myMat)
Part.show(myShape)


App.ActiveDocument.recompute()
Gui.SendMsgToActiveView("ViewFit")
Gui.SendMsgToActiveView("ViewFit")
time.sleep(3)
# global myShape
# myShape = make_box()
# App.getDocument("Unnamed").removeObject("Shape")
# App.getDocument("Unnamed").recompute()
# myShape.translate(Base.Vector(20,0,0))
# Part.show(myShape)
# App.getDocument("Unnamed").removeObject("Shape")
# App.ActiveDocument.recompute()
# myShape.translate(Base.Vector(20,0,0))
# Part.show(myShape)
# App.ActiveDocument.recompute()
# time.sleep(1)
