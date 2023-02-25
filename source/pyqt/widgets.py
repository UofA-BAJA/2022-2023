import sys
from PyQt5 import QtCore, QtWidgets, QtSerialPort
import pyqtgraph as pg

SCREEN_WIDTH_PIXELS = 800
SCREEN_HEIGHT_PIXELS = 480

# Creating the main window
class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 - QTabWidget'
        self.left = 0
        self.top = 0
        self.width = SCREEN_WIDTH_PIXELS
        self.height = SCREEN_HEIGHT_PIXELS
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
  
        self.tab_widget = MyTabWidget(self)
        self.setCentralWidget(self.tab_widget)
  
        self.show()
  
# Creating tab widgets
class MyTabWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(QtWidgets.QWidget, self).__init__(parent)
        self.layout = QtWidgets.QVBoxLayout(self)
  
        # Initialize tab screen
        self.tabs = QtWidgets.QTabWidget()
        self.tab1 = QtWidgets.QWidget()
        self.tab2 = QtWidgets.QWidget()
        self.tab3 = QtWidgets.QWidget()
        self.hometab = HomeWidget(self)
        self.rpmstab = RPMWidget(self)
        self.suspensiontab = SuspensionWidget(self)
        self.gpstab = GPSWidget(self)
        self.diagnosticstab = DiagnosticsWidget(self)

        all_tabs = [self.hometab, self.rpmstab, self.suspensiontab, self.gpstab, self.diagnosticstab]
        #self.tabs.resize(300, 200)
  
      

        for tab in all_tabs:
            self.tabs.addTab(tab, tab.tab_name)
  
        # Create first tab
        self.tab1.layout = QtWidgets.QVBoxLayout(self)
        self.l = QtWidgets.QLabel()
        self.l.setText("This is the first tab")
        self.tab1.layout.addWidget(self.l)
        self.tab1.setLayout(self.tab1.layout)
  
        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

class HomeWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(QtWidgets.QWidget, self).__init__(parent)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)

        self.tab_name = "HOME"
        
        self.l = QtWidgets.QLabel()
        self.l.setText(f"This is the {self.tab_name} tab")
        self.layout.addWidget(self.l)

        

class RPMWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(QtWidgets.QWidget, self).__init__(parent)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)

        self.tab_name = "RPMS"
        
        self.l = QtWidgets.QLabel()
        self.l.setText(f"This is the {self.tab_name} tab")
        self.layout.addWidget(self.l)

class SuspensionWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(QtWidgets.QWidget, self).__init__(parent)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)

        self.tab_name = "SUSPENSION"
        
        self.l = QtWidgets.QLabel()
        self.l.setText(f"This is the {self.tab_name} tab")
        self.layout.addWidget(self.l)

class GPSWidget(QWidget):
    def __init__(self, parent):
        super(QtWidgets.QWidget, self).__init__(parent)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)

        self.tab_name = "GPS"
        
        self.l = QtWidgets.QLabel()
        self.l.setText(f"This is the {self.tab_name} tab")
        self.layout.addWidget(self.l)

        self.suspension_graph = pg.PlotWidget()

class DiagnosticsWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(QtWidgets.QWidget, self).__init__(parent)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)

        self.tab_name = "DIAGNOSTICS"
        
        self.l = QtWidgets.QLabel()
        self.l.setText(f"This is the {self.tab_name} tab")
        self.layout.addWidget(self.l)

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
            'COM3',
            baudRate=QtSerialPort.QSerialPort.BaudRate.Baud115200,
            readyRead=self.receive
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())