import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from widgets.graph import GraphWidget
from widgets.tab import GeneralTab



class GPSWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
      
        image_path = r"/Users/man/Downloads/TheUofAmap.png"
        self.image = QtGui.QPixmap(image_path)
        self.data = r"/Users/man/Downloads/GPS-visualization-Python-main/data.csv"

    def paintEvent(self, event):

        pen = QtGui.QPen()
        pen.setWidth(2)

        painter = QtGui.QPainter(self)
        painter.drawPixmap(self.rect(), self.image)

        painter.setPen(pen)
        painter.drawLine(45 , 16, 100 , 100)

        
        #print(self.image)
        

def main():
    app = QtWidgets.QApplication(sys.argv)
    gpswidget = GPSWidget()
    gpswidget.show()
    sys.exit(app.exec_())

main()
    


