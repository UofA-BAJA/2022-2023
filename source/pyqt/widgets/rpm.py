from PyQt5 import QtWidgets


class RPMWidget(QtWidgets.QWidget):
    def __init__(self):
        super(QtWidgets.QWidget, self).__init__()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)

        self.tab_name = "RPMS"
        
        self.l = QtWidgets.QLabel()
        self.l.setText(f"This is the {self.tab_name} tab")
        self.layout.addWidget(self.l)