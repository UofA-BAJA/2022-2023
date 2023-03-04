from PyQt5 import QtWidgets

from widgets.tab import GeneralTab

class SuspensionWidget(GeneralTab):
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)

        self.tab_name = "SUSPENSION"
        
        self.l = QtWidgets.QLabel()
        self.l.setText(f"This is the {self.tab_name} tab")
        self.layout.addWidget(self.l)
