import random
import os

from PyQt5 import QtWidgets, QtGui, QtCore
from widgets.graph import GraphWidget
from widgets.tab import GeneralTab

class GPSWidget(GeneralTab):
    def __init__(self):
        super().__init__()
        
        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)
        self.counter = 0
        self.tab_name = "GPS"
        
        
        self.image_path = os.path.abspath(os.getcwd()) + r"\resources\gps\empty_Map.jpg"
        self.image = QtGui.QPixmap(self.image_path)

        self.num_of_points = 30
        self.master = []
        for index, cords in enumerate(range(self.num_of_points)):
            c = []
            if index == 0:
                for i in range(4):
                    c.append(random.randint(0,400))

            else:
                c.append(self.master[index-1][2])
                c.append(self.master[index-1][3])
                c.append(random.randint(0,400))
                c.append(random.randint(0,400))
            
            self.master.append(c)
        
    
    
    def paintEvent(self, event):
        self.updateData()
        
    
    def updateData(self) -> None:
        print("fvfvv")
        self.painter = QtGui.QPainter(self)
        self.painter.drawPixmap(self.rect(), self.image)

        
        pen = QtGui.QPen()
        pen.setWidth(5)

        self.painter.setPen(pen)
        
            
        for i in self.master:
            if self.master.index(i) > self.counter:
                break
            else:
                 self.painter.drawLine(i[0], i[1], i[2], i[3])

        '''
        if self.counter > 10:
            self.painter.drawLine(random.random() , random.random(), 100 , 100)

        if self.counter > 70:
            self.painter.drawLine(random.random(),random.random() , 100 , 100)
        '''
        
        self.painter.end()
        #data = r"/Users/man/Downloads/GPS-visualization-Python-main/data.csv"
        #return super().updateData()
        self.counter += .1

   


        
