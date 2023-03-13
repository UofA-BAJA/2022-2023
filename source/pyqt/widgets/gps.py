import sys
import random
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
        self.setup_GPS()

        self.master = []
        for cords in range(10):
            c = []
            for i in range(4):
                c.append(random.randint(0,400))
            
            self.master.append(c)
    
    def setup_GPS(self):
        #image_path = r"C:\Users\doria\Downloads\BAJA-MAP.png"
        self.image_path = r"/Users/man/Downloads/TheUofAmap.png"
        self.image = QtGui.QPixmap(self.image_path)
    
    
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

def main():
    app = QtWidgets.QApplication(sys.argv)
    gpswidget = GPSWidget()
    gpswidget.show()
    sys.exit(app.exec_())

   


        
