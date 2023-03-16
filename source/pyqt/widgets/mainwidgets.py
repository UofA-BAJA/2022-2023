import sys

from PyQt5 import QtCore, QtWidgets, QtSerialPort
import time

from widgets.tab import GeneralTab
from widgets.setup import SetupWidget
from widgets.gps import GPSWidget
from widgets.rpm import RPMWidget
from widgets.suspension import SuspensionWidget
from widgets.analysis import AnalysisWidget

from serial.port import Port
from serial.buffer import Buffer

from data.data_packager import DataPackager

SCREEN_SCALAR = 2

# Creating the main window
class App(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 - QTabWidget'
    
        self.setWindowTitle(self.title)

        self.tab_widget = MyTabWidget()
        self.setCentralWidget(self.tab_widget)

        

        self.buffer = Buffer()

        self.data_package = DataPackager()

        self.tab_widget.setuptab.serial_attempt.connect(self.setupSerial)

        self.new_time = time.time()

        
    def setupSerial(self):
        #print(self.tab_widget.setuptab.cbox.currentText())
        print("entered setupserial func")
        serial_port_obj = Port()
        serial = serial_port_obj.try_serial_port(self.tab_widget.setuptab.cbox.currentText())

        if serial.open(QtCore.QIODevice.ReadWrite):
           
            print(f"Successfully connected to serial port {self.tab_widget.setuptab.cbox.currentText()}")
            self.serial = serial

            
            serial.readyRead.connect(self.buffering)
        else:
            serial.close()

        
        # for each_tab in self.tab_widget.all_tabs:
        #     self.tab_widget.setupSerial(each_tab, self.serial_port)

    def buffering(self):
        #print("readyRead Called")

        raw_text = self.serial.readAll().data().decode()

        self.tab_widget.setuptab.raw_serial_monitor.append(raw_text)

        self.buffer.raw_input = raw_text

        for d in self.buffer.datapackets:
            self.tab_widget.setuptab.data_monitor.append(d)

        self.data_package.parse_packets(self.buffer.datapackets)

        
        if (self.data_package.complete_new_packet_flag):
            self.updating()
        else: 
            #print(f"NOT READY: {self.data_package}")
            pass
            

    def updating(self):
        '''this is where you update everything'''
        n = time.time()
        diff = n - self.new_time

        self.new_time = n

        #print(f"READY: {self.data_package}")
        #print(1 / diff)
        self.tab_widget.setuptab.updateData(diff)
        self.tab_widget.suspensiontab.updateData(self.data_package)
        self.tab_widget.rpmstab.updateData(self.data_package)
        self.tab_widget.gpstab.update()

        



  

# Creating tab widgets
class MyTabWidget(QtWidgets.QTabWidget):
    def __init__(self):
        super(QtWidgets.QWidget, self).__init__()
        
        self.setuptab = SetupWidget()
        self.rpmstab = RPMWidget()
        self.suspensiontab = SuspensionWidget()
        self.gpstab = GPSWidget()
        self.analysistab= AnalysisWidget()

        self.all_tabs = [self.setuptab, self.rpmstab, self.suspensiontab, self.gpstab, self.analysistab]

        for tab_number, tab in enumerate(self.all_tabs):
            self.addTab(tab, tab.tab_name)

            
       
    def setupSerial(self, tab: GeneralTab, serial_port: Port) -> None:

        tab.set_serial(serial_port)

    def updateTabs(self, tab: GeneralTab, datapackage: DataPackager) -> None:

        tab.updateData(datapackage)
                
screen_scalar = {0 : [800, 480],
                1 : [1600, 960],
                2 : [2400, 1440]}
def setupApp(screen_scalar_select) -> App:
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    ex.setFixedWidth(screen_scalar[screen_scalar_select][0])
    ex.setFixedWidth(screen_scalar[screen_scalar_select][1])

    return ex, app

def showapp(ex: App, app: QtWidgets.QApplication):
    ex.show()

    sys.exit(app.exec_())



