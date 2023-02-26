import sys
from PyQt5 import QtCore, QtWidgets, QtSerialPort
import pyqtgraph as pg



SCREEN_SCALAR = 2
'''
SCREEN SCALAR LETS YOU CHOOSE HOW BIG THE WINDOW IS WHILE DEVELOPING
    width, height
0 = 800, 480
1 = 1600, 960
2 = 2400, 1440
'''
# Creating the main window
class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 - QTabWidget'
        self.left = 0
        self.top = 0
    
        self.setWindowTitle(self.title)
  
        self.tab_widget = MyTabWidget()
        self.setCentralWidget(self.tab_widget)
  
    def set_screen_size(self, screen_size):
        screen_pixels = {
            0: [800, 480],
            1: [1600, 960],
            2: [2400, 1440],
            }
        width = screen_pixels[screen_size][0]
        height = screen_pixels[screen_size][1]
        self.setGeometry(self.left, self.top, width, height)
   
  
# Creating tab widgets
class MyTabWidget(QtWidgets.QTabWidget):
    def __init__(self):
        super(QtWidgets.QWidget, self).__init__()
        
        self.hometab = HomeWidget()
        self.rpmstab = RPMWidget()
        self.suspensiontab = SuspensionWidget()
        self.gpstab = GPSWidget()
        self.diagnosticstab = DiagnosticsWidget()

        all_tabs = [self.hometab, self.rpmstab, self.suspensiontab, self.gpstab, self.diagnosticstab]

        for tab in all_tabs:
            self.addTab(tab, tab.tab_name)
  
     
class HomeWidget(QtWidgets.QWidget):
    def __init__(self):
        super(QtWidgets.QWidget, self).__init__()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)

        self.tab_name = "HOME"
        
        self.l = QtWidgets.QLabel()
        self.l.setText(f"This is the {self.tab_name} tab")
        self.layout.addWidget(self.l)

        

class RPMWidget(QtWidgets.QWidget):
    def __init__(self):
        super(QtWidgets.QWidget, self).__init__()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)

        self.tab_name = "RPMS"
        
        self.l = QtWidgets.QLabel()
        self.l.setText(f"This is the {self.tab_name} tab")
        self.layout.addWidget(self.l)

class SuspensionWidget(QtWidgets.QWidget):
    def __init__(self):
        super(QtWidgets.QWidget, self).__init__()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)

        self.tab_name = "SUSPENSION"
        
        self.l = QtWidgets.QLabel()
        self.l.setText(f"This is the {self.tab_name} tab")
        self.layout.addWidget(self.l)

class GPSWidget(QtWidgets.QWidget):
    def __init__(self):
        super(QtWidgets.QWidget, self).__init__()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)

        self.tab_name = "GPS"
        
        self.l = QtWidgets.QLabel()
        self.l.setText(f"This is the {self.tab_name} tab")
        self.layout.addWidget(self.l)

        self.suspension_graph = pg.PlotWidget()

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



        

class GraphWidget(pg.PlotWidget):
    all_graph_instances = []
    def __init__(self, parent=None):
        super(GraphWidget, self).__init__(parent)

        self.__class__.all_graph_instances.append(self)

        self.updated = False


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    ex.set_screen_size(SCREEN_SCALAR)
    ex.show()
    
    sys.exit(app.exec_())