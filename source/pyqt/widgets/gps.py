import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from widgets.graph import GraphWidget
from widgets.tab import GeneralTab

class GPSWidget(GeneralTab):
    def __init__(self):
        super().__init__()

        image_path = r"/Users/man/Downloads/TheUofAmap.png"
        self.image = QtGui.QPixmap(image_path)
        
        
        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)

        self.tab_name = "GPS"

        self.l = QtWidgets.QLabel()
        self.layout.addWidget(self.l)

    def paintEvent(self, event):
        
        painter = QtGui.QPainter(self)
        painter.drawPixmap(self.rect(), self.image)

def main():
    app = QtWidgets.QApplication(sys.argv)
    gpswidget = GPSWidget()
    gpswidget.show()
    sys.exit(app.exec_())

   


        
