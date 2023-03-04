from pyqt import QtWidgets


from serial.port import Port


class GeneralTab(QtWidgets.QWidget):

    def __init__(self) -> None:
        super(QtWidgets.QWidget, self).__init__()
        self.tab_name = "EMPTY"

    def updateData(self) -> None:
        pass

    def set_serial(self, serial_port: Port) -> None:
        self.serial_port = serial_port
        


    