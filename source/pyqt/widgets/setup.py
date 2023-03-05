from PyQt5 import QtWidgets, QtCore, QtSerialPort

from widgets.graph import GraphWidget, DataLine
from widgets.tab import GeneralTab



class SetupWidget(GeneralTab):
    serial_attempt = QtCore.pyqtSignal()

    max_textbox_length = 10000
    def __init__(self):
        super(QtWidgets.QWidget, self).__init__()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)

        self.tab_name = "SETUP"

        self.hertz_data = DataLine("Hertz")
        self.hertz_graph = GraphWidget()
        self.hertz_graph.add_dataline(self.hertz_data)
        self.hertz_graph.setup()

        self.setup_serial_configure()
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

        self.config_layout = QtWidgets.QHBoxLayout()

        self.button = QtWidgets.QPushButton(
            text="Connect", 
            checkable=True,
        )
        self.button.clicked.connect(self.serial_attempt)

        self.cbox = QtWidgets.QComboBox()


        for s in QtSerialPort.QSerialPortInfo().availablePorts():
            self.cbox.addItem(s.portName())

        self.config_layout.addWidget(self.button)
        self.config_layout.addWidget(self.cbox)


        self.layout.addLayout(self.config_layout)

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


    def updateData(self) -> None:
        self.raw_serial_monitor.append("a")