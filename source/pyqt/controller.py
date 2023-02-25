import sys
from PyQt5 import QtCore, QtWidgets, QtSerialPort

from widgets import App
from DataPackager import DataPackager

class UIController():
    def __init__(self) -> None:
        self.app = QtWidgets.QApplication(sys.argv)
        self.ex = App() 

    def set_screen_size(self, option: int = 0) -> None:
        self.ex.set_screen_size(option)

    def showUI(self) -> None:
        self.ex.show()
        sys.exit(self.app.exec_())

    def updategraphs(self) -> None:
        self.ex.tab_widget.diagnosticstab.hertz_graph

    def updatenumbers(self) -> None:
        #DataPackager.get_gps(x)

        #self.ex.tab_widget.diagnosticstab.hertz_graph.
        pass
