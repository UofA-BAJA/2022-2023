from PyQt5 import QtWidgets, QtCore, QtSerialPort
from widgets.graph import GraphWidget

class DiagnosticsWidget(QtWidgets.QWidget):
    def __init__(self):
        super(QtWidgets.QWidget, self).__init__()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)

        self.tab_name = "DIAGNOSTICS"
        
        self.l = QtWidgets.QLabel()
        self.l.setText(f"This is the {self.tab_name} tab")
        self.layout.addWidget(self.l)

        self.hertz_graph = GraphWidget(self)

        self.message_le = QtWidgets.QLineEdit()
   
        self.send_btn = QtWidgets.QPushButton(
            text="Send",
            clicked=self.send
        )
        self.output_te = QtWidgets.QTextEdit(readOnly=True)
        self.button = QtWidgets.QPushButton(
            text="Connect", 
            checkable=True,
            toggled=self.on_toggled
        )

        self.serial = QtSerialPort.QSerialPort( #connect the arduino
            'COM6',
            baudRate=QtSerialPort.QSerialPort.BaudRate.Baud115200,
            readyRead=self.receive
        )

        self.layout.addWidget(self.output_te)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.hertz_graph)

    @QtCore.pyqtSlot()
    def send(self):
        self.serial.write(self.message_le.text().encode())

    @QtCore.pyqtSlot(bool)
    def on_toggled(self, checked):
        self.button.setText("Disconnect" if checked else "Connect")
        if checked:
            if not self.serial.isOpen():
                if not self.serial.open(QtCore.QIODevice.ReadWrite):
                    self.button.setChecked(False)
        else:
            self.serial.close()

    @QtCore.pyqtSlot()
    def receive(self):
        
        text = self.serial.readLine().data().decode()
        text = text.rstrip('\r\n')

        self.output_te.append(f"newline read: {text}")