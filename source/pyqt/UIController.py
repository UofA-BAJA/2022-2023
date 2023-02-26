import sys
from PyQt5 import QtCore, QtWidgets, QtSerialPort

from widgets.mainwidgets import App
from DataPackager import DataPackager

class UIController():
    def __init__(self) -> None:
        self.app = QtWidgets.QApplication(sys.argv)
        self.ex = App() 

    def set_screen_size(self, option: int = 0) -> None:
        screen_pixels = {
            0: [800, 480],
            1: [1600, 960],
            2: [2400, 1440],
            }
        width = screen_pixels[option][0]
        height = screen_pixels[option][1]
        self.ex.setGeometry(0, 0, width, height)

    def set_serial_port_obj(self, port: QtSerialPort.QSerialPort) -> None:
        pass

    def showUI(self) -> None:
        self.ex.show()
        sys.exit(self.app.exec_())

    def updategraphs(self) -> None:
        self.ex.tab_widget.diagnosticstab.hertz_graph

    def updatenumbers(self) -> None:
        #DataPackager.get_gps(x)

        #self.ex.tab_widget.diagnosticstab.hertz_graph.
        pass