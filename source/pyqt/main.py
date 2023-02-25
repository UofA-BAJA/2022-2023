import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, QLabel

SCREEN_WIDTH_PIXELS = 800
SCREEN_HEIGHT_PIXELS = 480

# Creating the main window
class App(QMainWindow):
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
class MyTabWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
  
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
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
        self.tab1.layout = QVBoxLayout(self)
        self.l = QLabel()
        self.l.setText("This is the first tab")
        self.tab1.layout.addWidget(self.l)
        self.tab1.setLayout(self.tab1.layout)
  
        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

class HomeWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        self.tab_name = "HOME"
        
        self.l = QLabel()
        self.l.setText(f"This is the {self.tab_name} tab")
        self.layout.addWidget(self.l)

        

class RPMWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        self.tab_name = "RPMS"
        
        self.l = QLabel()
        self.l.setText(f"This is the {self.tab_name} tab")
        self.layout.addWidget(self.l)

class SuspensionWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        self.tab_name = "SUSPENSION"
        
        self.l = QLabel()
        self.l.setText(f"This is the {self.tab_name} tab")
        self.layout.addWidget(self.l)

class GPSWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        self.tab_name = "GPS"
        
        self.l = QLabel()
        self.l.setText(f"This is the {self.tab_name} tab")
        self.layout.addWidget(self.l)

class DiagnosticsWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        self.tab_name = "DIAGNOSTICS"
        
        self.l = QLabel()
        self.l.setText(f"This is the {self.tab_name} tab")
        self.layout.addWidget(self.l)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())