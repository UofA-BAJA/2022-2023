import os

from PyQt5 import QtWidgets, QtCore, QtSerialPort

from widgets.graph import GraphWidget, DataLine
from widgets.tab import GeneralTab

MAX_SERIAL_TEXTBOX__CHAR_LENGTH = 10000

class SetupWidget(GeneralTab):
    serial_attempt = QtCore.pyqtSignal()
    open_file_attempt = QtCore.pyqtSignal()

    max_textbox_length = MAX_SERIAL_TEXTBOX__CHAR_LENGTH
    
    def __init__(self):
        super(QtWidgets.QWidget, self).__init__()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)

        self.tab_name = "SETUP"

        self.hertz_data = DataLine("Hertz")
        self.hertz_data.setPenColor()
        self.hertz_graph = GraphWidget()
        self.hertz_graph.add_dataline(self.hertz_data)
        self.hertz_graph.setup()

        top_tab = QtWidgets.QTabWidget()
        self.setup_serial_configure()
        self.setup_open_file()
        top_tab.addTab(self.serial_select_tab, "SERIAL")
        top_tab.addTab(self.file_select_tab, "FILE")
        self.layout.addWidget(top_tab)

        self.setup_text_monitors()

        
        self.layout.addWidget(self.hertz_graph)

    def setup_text_monitors(self) -> None:

        self.text_tab = QtWidgets.QTabWidget()

        self.raw_serial_monitor = QtWidgets.QTextEdit(
            readOnly=True
            )
        self.raw_serial_monitor.textChanged.connect(self.check_rawserial_box_length)

        self.data_monitor = QtWidgets.QTextEdit(readOnly=True)

        self.text_tab.addTab(self.raw_serial_monitor, "SERIAL")

        self.text_tab.addTab(self.data_monitor, "BUFFERED")

        self.layout.addWidget(self.text_tab)


    def setup_serial_configure(self) -> None:

        self.serial_select_tab = QtWidgets.QWidget()

        self.serial_select_layout = QtWidgets.QHBoxLayout()

        self.button = QtWidgets.QPushButton(
            text="Connect", 
            checkable=True,
        )
        self.button.clicked.connect(self.serial_attempt)

        self.cbox = QtWidgets.QComboBox()


        for s in QtSerialPort.QSerialPortInfo().availablePorts():
            self.cbox.addItem(s.portName())

        self.serial_select_layout.addWidget(self.button)
        self.serial_select_layout.addWidget(self.cbox)

        self.serial_select_tab.setLayout(self.serial_select_layout)

    def setup_open_file(self) -> None:

        self.file_select_tab = QtWidgets.QWidget()

        self.file_select_layout = QtWidgets.QHBoxLayout()

        self.open_file_button = QtWidgets.QPushButton(
            text="Open File", 
        )

        self.open_file_button.clicked.connect(self.open_file_attempt)

        self.file_cbox = QtWidgets.QComboBox()

        csv_path = os.path.abspath(os.getcwd()) + "\src\Sensor Dashboard\simulator\csvs"
        for csv in os.listdir(csv_path):
            self.file_cbox.addItem(csv)

        self.file_select_layout.addWidget(self.open_file_button)
        self.file_select_layout.addWidget(self.file_cbox)

        self.file_select_tab.setLayout(self.file_select_layout)



    @QtCore.pyqtSlot()
    def check_rawserial_box_length(self):
        
        if self.check_max_length(self.raw_serial_monitor.toPlainText()):
            self.raw_serial_monitor.clear()
            print("Serial Cleared")

    def check_max_length(self, text: str) -> bool:
        if len(text) > self.max_textbox_length:
            return True
        else:
            return False


    def updateData(self, difference) -> None:
        self.raw_serial_monitor.append("a")
        self.hertz_data.update(1/difference)