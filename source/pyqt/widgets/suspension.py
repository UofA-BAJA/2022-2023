from PyQt5 import QtWidgets, QtCore

from widgets.tab import GeneralTab

from widgets.graph import GraphWidget, DataLine

from data.data_packager import DataPacket


class SuspensionWidget(GeneralTab):
    def __init__(self):
        super().__init__()

        self.tab_name = "SUSPENSION"
        self.layout = QtWidgets.QHBoxLayout(self)
        self.setLayout(self.layout)

        self.configbox()
        self.setup_graph()
        
        self.max = [-1, -1, -1, -1]
        self.min = [1000000, 1000000, 1000000, 1000000]
    def configbox(self):

        def make_nice_textbox(title) -> QtWidgets.QTextEdit:
            t =  QtWidgets.QTextEdit()
            t.setText(title)
            t.setReadOnly(True)
            t.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
            t.setFixedWidth(round(self.width() / 10))

            return t
        
        layout = QtWidgets.QHBoxLayout()

        summary_box = QtWidgets.QGridLayout()

        title_boxes = ["FRONT RIGHT", 
                       "FRONT LEFT", 
                       "BACK RIGHT", 
                       "BACK LEFT"]

        for index, title in enumerate(title_boxes):
            t = make_nice_textbox(title)

            summary_box.addWidget(t, 0, (index + 1) * 2, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

        self.max = make_nice_textbox("MAX")
        self.min = make_nice_textbox("MIN")
        self.avg = make_nice_textbox("AVG")

        spacer_height = 20
        spacer_width = round(self.width() / 3)

        verticalSpacerTop = QtWidgets.QSpacerItem(spacer_width, spacer_height)

        verticalSpacerBottom = QtWidgets.QSpacerItem(spacer_width, spacer_height)

        layout.addLayout(summary_box)
        #layout.addSpacerItem(verticalSpacerTop)
        
        #layout.addSpacerItem(verticalSpacerBottom)

        self.layout.addLayout(layout)


    def setup_graph(self):

        self.box_front_right_data = None
        self.box_front_left_data = None
        self.box_back_right_data = None
        self.box_back_left_data = None
        
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

    def updateData(self, data: data_packager):
        self.box_front_right_data = data.suspension.front_right
        self.box_front_left_data = data.suspension.front_left
        self.box_back_right_data = data.suspension.back_right
        self.box_back_left_data = data.suspension.back_left
        
        self.front_right.update(data.suspension.front_right)
        self.front_left.update(data.suspension.front_left)
        self.back_right.update(data.suspension.back_right)
        self.back_left.update(data.suspension.back_left)
        
        self.add_Data_to_summary_Box()

    def add_Data_to_summary_Box(self):
        if self.box_front_right_data > self.max[0]:
            self.max[0] = self.box_front_right_data
        if self.box_front_left_data > self.max[1]:
            self.max[1] = self.box_front_left_data
        if self.box_back_right_data > self.max[2]:
            self.max[2] = self.box_back_right_data
        if self.box_back_left_data > self.max[3]:
            self.max[3] = self.box_back_left_data
            
        self.max_list[0].setText(str(self.max[0]))
        self.max_list[1].setText(str(self.max[1]))
        self.max_list[2].setText(str(self.max[2]))
        self.max_list[3].setText(str(self.max[3]))
        
        if self.box_front_right_data < self.min[0]:
            self.min[0] = self.box_front_right_data
        if self.box_front_left_data < self.min[1]:
            self.min[1] = self.box_front_left_data
        if self.box_back_right_data < self.min[2]:
            self.min[2] = self.box_back_right_data
        if self.box_back_left_data < self.min[3]:
            self.min[3] = self.box_back_left_data
            
        self.min_list[0].setText(str(self.min[0]))
        self.min_list[1].setText(str(self.min[1]))
        self.min_list[2].setText(str(self.min[2]))
        self.min_list[3].setText(str(self.min[3]))
