# coding=UTF-8
import sys
sys.path.append('C:\\Users\\apl\\Anaconda3\\Library\\bin')#这里使用你自己的bin目录
import FreeCAD as app
import FreeCAD as App
import FreeCADGui as Gui
import FreeCADGui as gui
import Part,time
from FreeCAD import Base

# gui.showMainWindow() ##只有showMainWindow 之后能够调用GUI的所有功能
# App.newDocument("Unnamed")
# App.setActiveDocument("Unnamed")
# App.ActiveDocument=App.getDocument("Unnamed")
# Gui.ActiveDocument=Gui.getDocument("Unnamed")
# Gui.activateWorkbench("PartWorkbench")
# App.ActiveDocument.addObject("Part::Box","Box")
# App.ActiveDocument.ActiveObject.Label = "Box"
# App.ActiveDocument.recompute()
# Gui.SendMsgToActiveView("ViewFit")
# print ("1")
# time.sleep(3)
# App.getDocument("Unnamed").getObject("Box").Length = '2 mm'
# App.ActiveDocument.recompute()
# Gui.SendMsgToActiveView("ViewFit")
# print ("1")
# time.sleep(3)
# App.getDocument("Unnamed").getObject("Box").Length = '20 mm'
# App.ActiveDocument.recompute()
# Gui.SendMsgToActiveView("ViewFit")
# print ("1")
# time.sleep(3)
# gui.showMainWindow()

class FreecadDraw:
    def __init__(self, color, myWidth, myHeight, myThickness):
        global doc
        self.color = color
        self.width = myWidth
        self.height = myHeight
        self.thickness = myThickness

    def makeBottle1(self):
        aPnt1 = Base.Vector(-self.width / 2., 0, 0)
        aPnt2 = Base.Vector(-self.width / 2., -self.thickness / 4., 0)
        aPnt3 = Base.Vector(0, -self.thickness / 2., 0)
        aPnt4 = Base.Vector(self.width / 2., -self.thickness / 4., 0)
        aPnt5 = Base.Vector(self.width / 2., 0, 0)
        ## 上面定义5个点：只与myThickness,myWidth有关

        aArcOfCircle = Part.Arc(aPnt2, aPnt3, aPnt4)
        aSegment1 = Part.LineSegment(aPnt1, aPnt2)
        aSegment2 = Part.LineSegment(aPnt4, aPnt5)
        ## 上面构建2条线和一个圆弧： 线1： 1-2； 线2： 4-5； 圆弧：2-3-4

        aEdge1 = aSegment1.toShape()
        aEdge2 = aArcOfCircle.toShape()
        aEdge3 = aSegment2.toShape()
        aWire = Part.Wire([aEdge1, aEdge2, aEdge3])
        ## 由几何结构(line和circle)构造形状Shape:（Solid-Shell-Face-Wire-Edge-Vertex）

        aTrsf = Base.Matrix()
        ##  Matrix是变换到三维的一个常用工具，他包含了几乎所有的变换

        aTrsf.rotateZ(math.pi)  # rotate around the z-axis
        aMirroredWire = aWire.transformGeometry(aTrsf)  #
        myWireProfile = Part.Wire([aWire, aMirroredWire])
        myFaceProfile = Part.Face(myWireProfile)  # 将线变成了面
        aPrismVec = Base.Vector(0, 0, self.height)
        myBody = myFaceProfile.extrude(aPrismVec)
        #    myBody=myBody.makeFillet(myThickness/12.0,myBody.Edges)
        ##上面语句为，先180镜像，之后形成一个closed face，之后
        # 用extrude进行拉升 myHeight的高度
        # 随后使用makeFillet,扣除 myThickness/12.0 的厚度

        neckLocation = Base.Vector(0, 0, self.height)
        neckNormal = Base.Vector(0, 0, 1)
        myNeckRadius = self.thickness / 4.
        myNeckHeight = self.height / 10.
        myNeck = Part.makeCylinder(myNeckRadius, myNeckHeight, neckLocation, neckNormal)
        myBody = myBody.fuse(myNeck)
        #    myBody = myBody.makeFillet(myThickness/12.0,myBody.Edges)
        #    App.getDocument('Cube').addObject('Part::PartFeature','Shape') = myBody.toShape()
        #    Gui.getDocument("Cube").getObject("Shape").ShapeColor=color

        Part.show(myBody)
        Gui.getDocument("Bottle").getObject("Shape001").ShapeColor = self.color

    def Bottleshow(self):
        gui.showMainWindow()  ##只有showMainWindow 之后能够调用GUI的所有功能
        # doc = app.newDocument() for makeBottle1
        doc = App.newDocument('Bottle')
        box = Part.makeBox(10, 10, 10)
        Part.show(box)
        box = doc.addObject("Part::Box", "myBox")

