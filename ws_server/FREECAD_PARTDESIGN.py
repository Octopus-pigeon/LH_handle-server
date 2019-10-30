#coding= utf-8
import time
# import numpy as np
import sys
sys.path.append('C:\\Users\\apl\\Anaconda3\\Library\\bin')
import FreeCAD as App
import FreeCADGui as Gui
import Part, math
# import PartDesignGui
Gui.showMainWindow()
App.newDocument("Unnamed")
App.setActiveDocument("Unnamed")
App.ActiveDocument=App.getDocument("Unnamed")
Gui.ActiveDocument=Gui.getDocument("Unnamed")

Gui.activateWorkbench("PartDesignWorkbench")
App.activeDocument().addObject('PartDesign::Body','Body')
Gui.activeView().setActiveObject('pdbody', App.activeDocument().Body)
Gui.Selection.clearSelection()
Gui.Selection.addSelection(App.ActiveDocument.Body)
App.ActiveDocument.recompute()
App.activeDocument().Body.newObject('Sketcher::SketchObject','Sketch')
App.activeDocument().Sketch.Support = (App.activeDocument().XY_Plane, [''])
App.activeDocument().Sketch.MapMode = 'FlatFace'
App.ActiveDocument.recompute()
Gui.activeDocument().setEdit('Sketch')
Gui.activateWorkbench('SketcherWorkbench')
ActiveSketch = App.ActiveDocument.getObject('Sketch')
tv = Show.TempoVis(App.ActiveDocument)
time.sleep(3)
if ActiveSketch.ViewObject.HideDependent:
    objs = tv.get_all_dependent(ActiveSketch)
    objs = filter(lambda x: not x.TypeId.startswith("TechDraw::"), objs)
    objs = filter(lambda x: not x.TypeId.startswith("Drawing::"), objs)
    tv.hide(objs)
if ActiveSketch.ViewObject.ShowSupport:
    tv.show([ref[0] for ref in ActiveSketch.Support if not ref[0].isDerivedFrom("PartDesign::Plane")])
if ActiveSketch.ViewObject.ShowLinks:
    tv.show([ref[0] for ref in ActiveSketch.ExternalGeometry])
tv.hide(ActiveSketch)
ActiveSketch.ViewObject.TempoVis = tv
del(tv)

ActiveSketch = App.ActiveDocument.getObject('Sketch')
if ActiveSketch.ViewObject.RestoreCamera:
    ActiveSketch.ViewObject.TempoVis.saveCamera()
time.sleep(3)
App.ActiveDocument.Sketch.addGeometry(Part.LineSegment(App.Vector(-20.419970,-0.182321,0),App.Vector(0.000000,0.000000,0)),False)
App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('PointOnObject',0,1,-1))
App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Coincident',0,2,-1,1))
App.ActiveDocument.recompute()
App.ActiveDocument.Sketch.addGeometry(Part.LineSegment(App.Vector(0.000000,-0.000000,0),App.Vector(-0.121547,16.591223,0)),False)
App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Coincident',1,1,0,2))
App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('PointOnObject',1,2,-2))
App.ActiveDocument.recompute()
App.ActiveDocument.Sketch.addGeometry(Part.Circle(App.Vector(-20.419970,0.000000,0),App.Vector(0,0,1),10),True)
App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Coincident',2,3,0,1))
App.ActiveDocument.Sketch.addGeometry(Part.Circle(App.Vector(-19.546864,6.216301,0),App.Vector(0,0,1),10),True)
App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Radius',2,1.000000))
App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Equal',2,3))
App.ActiveDocument.Sketch.addGeometry(Part.Circle(App.Vector(-14.198776,13.509148,0),App.Vector(0,0,1),10),True)
App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Equal',2,4))
App.ActiveDocument.Sketch.addGeometry(Part.Circle(App.Vector(-7.027479,15.818548,0),App.Vector(0,0,1),10),True)
App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Equal',2,5))
App.ActiveDocument.Sketch.addGeometry(Part.Circle(App.Vector(0.000000,16.591223,0),App.Vector(0,0,1),10),True)
App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Equal',2,6))
App.ActiveDocument.Sketch.addConstraint(Sketcher.Constraint('Coincident',6,3,1,2))
App.ActiveDocument.Sketch.addGeometry(Part.BSplineCurve([App.Vector(-20.42,0),App.Vector(-19.5469,6.2163),App.Vector(-14.1988,13.5091),App.Vector(-7.02748,15.8185),App.Vector(0,16.5912)],None,None,False,3,None,False),False)
conList = []
conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint',2,3,7,0))
conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint',3,3,7,1))
conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint',4,3,7,2))
conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint',5,3,7,3))
conList.append(Sketcher.Constraint('InternalAlignment:Sketcher::BSplineControlPoint',6,3,7,4))
App.ActiveDocument.Sketch.addConstraint(conList)
time.sleep(3)
App.ActiveDocument.Sketch.exposeInternalGeometry(7)
App.ActiveDocument.recompute()
Gui.getDocument('_________').resetEdit()
ActiveSketch = App.ActiveDocument.getObject('Sketch')
tv = ActiveSketch.ViewObject.TempoVis
if tv:
        tv.restore()
ActiveSketch.ViewObject.TempoVis = None
del(tv)
time.sleep(3)
Gui.activateWorkbench('PartDesignWorkbench')
App.getDocument('_________').recompute()
App.activeDocument().Body.newObject("PartDesign::Revolution","Revolution")
App.activeDocument().Revolution.Profile = App.activeDocument().Sketch
App.activeDocument().Revolution.ReferenceAxis = (App.activeDocument().Sketch,['V_Axis'])
App.activeDocument().Revolution.Angle = 360.0
Gui.activeDocument().hide("Sketch")
App.ActiveDocument.recompute()
Gui.activeDocument().setEdit('Revolution', 0)
Gui.Selection.clearSelection()
Gui.ActiveDocument.Revolution.ShapeColor=Gui.ActiveDocument.Body.ShapeColor
Gui.ActiveDocument.Revolution.LineColor=Gui.ActiveDocument.Body.LineColor
Gui.ActiveDocument.Revolution.PointColor=Gui.ActiveDocument.Body.PointColor
Gui.ActiveDocument.Revolution.Transparency=Gui.ActiveDocument.Body.Transparency
Gui.ActiveDocument.Revolution.DisplayMode=Gui.ActiveDocument.Body.DisplayMode
Gui.activeDocument().hide("Sketch")
App.ActiveDocument.Revolution.Angle = 360.000000
App.ActiveDocument.Revolution.ReferenceAxis = (App.ActiveDocument.Sketch, ["V_Axis"])
App.ActiveDocument.Revolution.Midplane = 0
App.ActiveDocument.Revolution.Reversed = 0
App.ActiveDocument.recompute()
Gui.activeDocument().resetEdit()
time.sleep(3)