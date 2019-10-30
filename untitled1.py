# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 10:53:12 2019

@author: longhui
"""

import time
import numpy as np
import sys
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

#绘制一个立方体
def make_cube():
    App.ActiveDocument.addObject("Part::Box","Box")
    App.ActiveDocument.ActiveObject.Label = "立方体"
    App.ActiveDocument.recompute()
    Gui.SendMsgToActiveView("ViewFit")
    time.sleep(2) 
    Gui.activeDocument().activeView().viewAxonometric()
    time.sleep(1)
    i=10
    while i>5:
        i=i-1
        App.getDocument("Unnamed").getObject("Box").Length = i
        App.ActiveDocument.recompute()
        Gui.SendMsgToActiveView("ViewFit")
        time.sleep(0.1)
    time.sleep(3)

#绘制一个圆柱体
def make_cylinder():
    App.ActiveDocument.addObject("Part::Cylinder", "Cylinder")
    App.ActiveDocument.ActiveObject.Label = "圆柱体"
    App.ActiveDocument.recompute()
    Gui.SendMsgToActiveView("ViewFit")
#绘制一个球体
def make_sphere():
    App.ActiveDocument.addObject("Part::Sphere", "Sphere")
    App.ActiveDocument.ActiveObject.Label = "球体"
    App.ActiveDocument.recompute()
    Gui.SendMsgToActiveView("ViewFit")
    time.sleep(1)
    App.getDocument("Unnamed").getObject("Sphere").Placement = App.Placement(App.Vector(-13, 5, 5),
                                                                                   App.Rotation(App.Vector(0, 0, 1), 0))
    
    App.ActiveDocument.recompute()
    Gui.SendMsgToActiveView("ViewFit")
    time.sleep(1)
    sphere_r=5
    while sphere_r>3:
        sphere_r=sphere_r-1
        App.getDocument("Unnamed").getObject("Sphere").Radius = sphere_r
        App.ActiveDocument.recompute()
        Gui.SendMsgToActiveView("ViewFit")
    time.sleep(1)
    Gui.activeDocument().activeView().viewFront()
    Gui.SendMsgToActiveView("ViewFit")
    time.sleep(1)
    Gui.activeDocument().activeView().viewLeft()
    Gui.SendMsgToActiveView("ViewFit")
    time.sleep(1)
    Gui.activeDocument().activeView().viewTop()
    Gui.SendMsgToActiveView("ViewFit")
    time.sleep(1)
    time.sleep(3)
#绘制一个圆锥体
def make_cone():
    App.ActiveDocument.addObject("Part::Cone", "Cone")
    App.ActiveDocument.ActiveObject.Label = "圆锥体"
    App.ActiveDocument.recompute()
    Gui.SendMsgToActiveView("ViewFit")
    time.sleep(1)
    j=0
    while j<90:
        j=j+10
        App.getDocument("Unnamed").getObject("Cone").Placement = App.Placement(App.Vector(0, 0, 0),
                                                                                     App.Rotation(App.Vector(0, 1, 0), j))
        App.ActiveDocument.recompute()
        Gui.SendMsgToActiveView("ViewFit")
    time.sleep(1)
    conex=0
    coney=0
    conez=0
    while conex> -10:
        conex=conex-1
        App.getDocument("Unnamed").getObject("Cone").Placement = App.Placement(App.Vector(conex, coney, conez),
                                                                                     App.Rotation(App.Vector(0, 1, 0), j))
        App.ActiveDocument.recompute()
        Gui.SendMsgToActiveView("ViewFit")
    while coney<5:
        coney=coney+1
        App.getDocument("Unnamed").getObject("Cone").Placement = App.Placement(App.Vector(conex, coney, conez),
                                                                                     App.Rotation(App.Vector(0, 1, 0), j))
        App.ActiveDocument.recompute()
        Gui.SendMsgToActiveView("ViewFit")
    while conez<5:
        conez=conez+1
        App.getDocument("Unnamed").getObject("Cone").Placement = App.Placement(App.Vector(conex, coney, conez),
                                                                                     App.Rotation(App.Vector(0, 1, 0), j))
        App.ActiveDocument.recompute()
        Gui.SendMsgToActiveView("ViewFit")
    time.sleep(3)
#三维空间平移立体对象
def move_object_3D(object_3D,x,y,z):
    #FreeCAD.getDocument("Unnamed").getObject("Box").Placement = App.Placement(App.Vector(10,0,0),App.Rotation(App.Vector(0,0,1),0))
    object_3D.Placement = App.Placement(App.Vector(x,y,z), App.Rotation(App.Vector(0, 0, 1), 0))
#三维空间旋转对象

make_cube()
make_cone()
make_sphere()
