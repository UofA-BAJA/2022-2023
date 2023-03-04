from PyQt5 import QtWidgets, QtCore, QtSerialPort

from widgets.graph import GraphWidget, DataLine
from widgets.tab import GeneralTab



class SetupWidget(GeneralTab):
    serial_attempt = QtCore.pyqtSignal()

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

        self.raw_serial_monitor = QtWidgets.QTextEdit(readOnly=True)

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


    def updateData(self) -> None:
        self.raw_serial_monitor.append("a")