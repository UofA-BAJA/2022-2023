import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from widgets.graph import GraphWidget
from widgets.tab import GeneralTab



class GPSWidget(GeneralTab):
    def __init__(self):
        super().__init__()

        
        
        self.tab_name = "GPS"
        
        self.l = QtWidgets.QLabel()
        self.l.setText("This is the {self.tab_name} tab")
        
        self.layout.addWidget(self.l)
        
        image_path = r"/Users/man/Downloads/TheUofAmap.png"
        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)

        self.image = QtGui.QPixmap(image_path)

    def paintEvent(self, event):

        painter = QtGui.QPainter(self)
        #p = QtGui.QPainter()
        
        #pixmap = QtGui.QPixmap('TheUofAmap.png')

        painter.drawPixmap(self.rect(), pixmap)
        #y = p.drawPixmap(self.rect(), x)

        #self.layout.addWidget(y)

def main():
    app = QtWidgets.QApplication(sys.argv)
    GPSWidget= GPSWidget()
    GPSWidget.show
    sys.exit(app.exec_())

   


        
