from PyQt5 import QtWidgets, QtGui
from widgets.graph import GraphWidget
from widgets.tab import GeneralTab

class GPSWidget(GeneralTab):
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)

        self.tab_name = "GPS"
        
        self.l = QtWidgets.QLabel()
        self.l.setText(f"This is the {self.tab_name} tab")
        self.layout.addWidget(self.l)

        p = QtGui.QPainter()

        x = QtGui.QPixmap('/Users/man/Downloads/TheUofAmap.png')

        y = p.drawPixmap(self.rect(), x)

        self.layout.addWidget(y)

        

    