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
        self.front_right.setPenColor()

        self.front_left = DataLine("front_left")
        self.front_left.setPenColor(255, 0, 0)

        self.back_right = DataLine("back_right")
        self.back_right.setPenColor(255, 0, 255)

        self.back_left = DataLine("back_left")
        self.back_left.setPenColor(0, 0, 255)

        self.suspension_graph = GraphWidget()
        self.suspension_graph.add_dataline(self.front_right)
        self.suspension_graph.add_dataline(self.front_left)
        self.suspension_graph.add_dataline(self.back_right)
        self.suspension_graph.add_dataline(self.back_left)
        self.suspension_graph.setup()

        self.layout.addWidget(self.suspension_graph)

    def updateData(self, data):
        self.front_right.update(data.suspension.front_right)
        self.front_left.update(data.suspension.front_left)
        self.back_right.update(data.suspension.back_right)
        self.back_left.update(data.suspension.back_left)
