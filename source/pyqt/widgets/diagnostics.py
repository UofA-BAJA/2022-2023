from PyQt5 import QtWidgets, QtCore, QtSerialPort
from widgets.graph import GraphWidget

class DiagnosticsWidget(QtWidgets.QWidget):
    def __init__(self):
        super(QtWidgets.QWidget, self).__init__()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)

        self.tab_name = "DIAGNOSTICS"

        self.hertz_graph = GraphWidget(self)

        self.message_le = QtWidgets.QLineEdit()
   
        self.raw_serial_monitor = QtWidgets.QTextEdit(readOnly=True)
        raw_serial_monitor_l = QtWidgets.QLabel()
        raw_serial_monitor_l.setText(f"Serial Monitor")

        self.data_monitor = QtWidgets.QTextEdit(readOnly=True)
        data_monitor_l = QtWidgets.QLabel()
        data_monitor_l.setText(f"Data Packet Monitor")

        self.button = QtWidgets.QPushButton(
            text="Connect", 
            checkable=True,
            toggled=self.on_toggled
        )

        self.serial = None

        self.layout.addWidget(self.raw_serial_monitor)
        self.layout.addWidget(self.data_monitor)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.hertz_graph)

    @QtCore.pyqtSlot(bool)
    def on_toggled(self, checked):
        self.button.setText("Disconnect" if checked else "Connect")
        if checked:
            if not self.serial.isOpen():
                if not self.serial.open(QtCore.QIODevice.ReadWrite):
                    self.button.setChecked(False)
        else:
            self.serial.close()

    def update_serial_monitor(self, input_text: str) -> None:
        self.output_te.append(input_text)