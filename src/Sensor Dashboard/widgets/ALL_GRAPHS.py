from PyQt5 import QtWidgets, QtCore

from widgets.tab import GeneralTab

from widgets.graph import GraphWidget, DataLine

from data import data_packager

class All_data_graphs(GeneralTab):
    def __init__(self):
        super().__init()
        self.tab_name = "All Graphs"
        self.layout = QtWidgets.QHBoxLayout(self)
        self.setLayout(self.layout)
        
    def configBox(self):
        pass