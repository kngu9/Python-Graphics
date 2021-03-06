from TkinterMenuBar import *
from TkinterButtonGroup import *
from TkinterCanvas import *
from Controller import *
import math


class MyView:
    def __init__(self,rootWidget,controllerReference):



        self.controllerReference = controllerReference


        #Add Top Menu Bar | Not used in this project
        #MyTkinterMenuBar(rootWidget)

        #add a button group
        self.buttonGroupReference = MyButtonGroup(rootWidget,self)

        #Add the canvas
        self.canvasReference = MyCanvas(rootWidget,self)


    def loadFile(self, fileLocation):
        model = self.controllerReference.loadModel(fileLocation)
        self.controllerReference.loadCameraFromMultiFile("./input_files/cameras_04.txt")
        self.canvasReference.draw_Model(model,self.controllerReference.cameras)

    def draw_model(self):
        self.canvasReference.draw_Model(self.controllerReference.model,self.controllerReference.cameras)

    def rotate_call(self,rotationType,rotationSteps,rotationTheta):
        self.controllerReference.rotationCall(rotationType,self.canvasReference,int(rotationSteps),math.radians(int(rotationTheta)))


    def scale_call(self, steps,a_Scale,s_Scale,all_Scale,scale_Type):
        self.controllerReference.scaleCall(steps,a_Scale,s_Scale,all_Scale,scale_Type,self.canvasReference)

    def translation_call(self,x,y,z,steps):
        self.controllerReference.tranlslateCall(steps,x,y,z,self.canvasReference)

    def fly_call(self,x1,y1,z1,x2,y2,z2,steps):
        self.controllerReference.flyCall(x1,y1,z1,x2,y2,z2,steps,self.canvasReference)
