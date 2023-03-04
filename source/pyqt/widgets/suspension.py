from PyQt5 import QtWidgets

from widgets.tab import GeneralTab

from widgets.graph import GraphWidget, DataLine


class SuspensionWidget(GeneralTab):
    def __init__(self):
        super().__init__()

        self.tab_name = "SUSPENSION"
        self.layout = QtWidgets.QHBoxLayout(self)
        self.setLayout(self.layout)

        self.configbox()
        self.setup_graph()

    def configbox(self):
        self.config_tab = QtWidgets.QTabWidget()

        layout = QtWidgets.QGridLayout()

        layout.addWidget(self.config_tab)
        


        self.layout.addLayout(layout)


    def setup_graph(self):
        self.front_right = DataLine("front_right")
        self.suspension_graph = GraphWidget()
        self.suspension_graph.add_dataline(self.front_right)
        self.suspension_graph.setup()

        self.layout.addWidget(self.suspension_graph)
