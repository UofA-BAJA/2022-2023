from PyQt5 import QtWidgets

from graph import GraphWidget

class GPSWidget(QtWidgets.QWidget):
    def __init__(self):
        super(QtWidgets.QWidget, self).__init__()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)

        self.tab_name = "GPS"
        
        self.l = QtWidgets.QLabel()
        self.l.setText(f"This is the {self.tab_name} tab")
        self.layout.addWidget(self.l)