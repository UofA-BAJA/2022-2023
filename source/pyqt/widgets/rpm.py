from PyQt5 import QtWidgets

from widgets.tab import GeneralTab
from widgets.graph import GraphWidget, DataLine

from data.data_packager import DataPacket

from widgets.graph import GraphWidget, DataLine


class RPMWidget(GeneralTab):
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.layout)

        self.tab_name = "RPMS"

        self.setup_graph()
        
        # self.l = QtWidgets.QLabel()
        # self.l.setText(f"This is the {self.tab_name} tab")
        # self.layout.addWidget(self.l)
    def setup_graph(self):
        self.rpmData_right = DataLine("RMP_Front_Right")
        self.rpmData_right.setPenColor(255,0,0)

        self.rpmData_left = DataLine("RPM_Front_Left")
        self.rpmData_left.setPenColor(0,255,0)
        
        self.rpmData_back = DataLine("RPM_Back")
        self.rpmData_back.setPenColor(0,0,255)

        self.rpmGrapgh = GraphWidget()
        self.rpmGrapgh.add_dataline(self.rpmData_right)
        self.rpmGrapgh.add_dataline(self.rpmData_left)
        self.rpmGrapgh.add_dataline(self.rpmData_back)

        self.rpmGrapgh.setup()
        self.layout.addWidget(self.rpmGrapgh)


    def updateData(self, data: DataPacket) -> None:
        self.rpmData_right.update(data.front_right_rpm)
        self.rpmData_left.update(data.front_left_rpm)
        self.rpmData_back.update(data.rear_rpm)
        