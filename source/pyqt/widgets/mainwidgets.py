from PyQt5 import QtCore, QtWidgets, QtSerialPort
from widgets.diagnostics import DiagnosticsWidget
from widgets.gps import GPSWidget
from widgets.home import HomeWidget
from widgets.rpm import RPMWidget
from widgets.suspension import SuspensionWidget



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
       
    
        self.setWindowTitle(self.title)
  
        self.tab_widget = MyTabWidget()
        self.setCentralWidget(self.tab_widget)
  
 
        
   
  
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



