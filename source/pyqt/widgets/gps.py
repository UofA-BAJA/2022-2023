import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from widgets.graph import GraphWidget
from widgets.tab import GeneralTab

class GPSWidget(GeneralTab):
    def __init__(self):
        super().__init__()
        
        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)

        self.tab_name = "GPS"
        self.setup_GPS()

    def setup_GPS(self):
        image_path = r"C:\Users\doria\Downloads\BAJA-MAP.png"
        self.image = QtGui.QPixmap(image_path)

    def paintEvent(self, event):
        
        painter = QtGui.QPainter(self)
        painter.drawPixmap(self.rect(), self.image)

def main():
    app = QtWidgets.QApplication(sys.argv)
    gpswidget = GPSWidget()
    gpswidget.show()
    sys.exit(app.exec_())

   


        
