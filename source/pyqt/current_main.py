from PyQt5 import QtCore, QtWidgets, QtSerialPort
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

from serial_handler import SerialHandler


class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        #alex is stupid haha
        super(Widget, self).__init__(parent)

        self.graph = pg.PlotWidget()
        pen = pg.mkPen(color=(255, 0, 0))
        pen2 = pg.mkPen(color=(0, 255, 0))
        pen3 = pg.mkPen(color=(0, 0, 255))
        pen4 = pg.mkPen(color=(255, 0, 255))
        self.serial_handler = SerialHandler(num_of_datapoints = 100)
        self.data_line =  self.graph.plot(self.serial_handler.x, self.serial_handler.y, pen = pen)
        self.data_line_2 = self.graph.plot(self.serial_handler.x, self.serial_handler.y1, pen = pen2)
        self.data_line_3 = self.graph.plot(self.serial_handler.x, self.serial_handler.y2, pen = pen3)
        self.data_line_4 = self.graph.plot(self.serial_handler.x, self.serial_handler.y3, pen = pen4)
        #self.serial_handler.testing()

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
        lay = QtWidgets.QVBoxLayout(self)
        hlay = QtWidgets.QHBoxLayout()
        hlay.addWidget(self.message_le)
        hlay.addWidget(self.send_btn)
        hlay.addWidget(self.graph)
        lay.addLayout(hlay)
        lay.addWidget(self.output_te)
        lay.addWidget(self.button)

        
        self.serial = QtSerialPort.QSerialPort( #connect the arduino
            'COM6',
            baudRate=QtSerialPort.QSerialPort.BaudRate.Baud115200,
            readyRead=self.receive
        )

    @QtCore.pyqtSlot()
    def receive(self):
        while self.serial.canReadLine():
            text = self.serial.readLine().data().decode()
            text = text.rstrip('\r\n')

            four_new_y_values = self.serial_handler.input_data(text)
            
            self.serial_handler.y = self.serial_handler.ShiftLeft(self.serial_handler.y, four_new_y_values[0])
            self.serial_handler.y1 = self.serial_handler.ShiftLeft(self.serial_handler.y1, four_new_y_values[1])
            self.serial_handler.y2 = self.serial_handler.ShiftLeft(self.serial_handler.y2, four_new_y_values[2])
            self.serial_handler.y3 = self.serial_handler.ShiftLeft(self.serial_handler.y3, four_new_y_values[3])

            self.output_te.append(text)

            self.data_line.setData(self.serial_handler.x,self.serial_handler.y)
            self.data_line_2.setData(self.serial_handler.x,self.serial_handler.y1)
            self.data_line_3.setData(self.serial_handler.x,self.serial_handler.y2)
            self.data_line_4.setData(self.serial_handler.x,self.serial_handler.y3)

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

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())