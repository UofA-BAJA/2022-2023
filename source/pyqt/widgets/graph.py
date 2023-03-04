from PyQt5 import QtWidgets
import pyqtgraph as pg

class DataLine():

    def __init__(self, name) -> None:
        self.dataline_name = name

        self.x = [0 for x in range(100)]

        self.y = [0 for x in range(100)]

    def curveline(self, curve: pg.PlotCurveItem) -> None:
        self.curve_pbj = curve
        pass

    def update(self, value):

        self.y = self.y[1:]

        self.y.append(value)
        
        self.curve_pbj.setData(self.x, self.y)



class GraphWidget(pg.PlotWidget):
    num_of_datapoints = 100
    def __init__(self):
        super(GraphWidget, self).__init__()

        self.datalines = {}

    def add_dataline(self, d: DataLine):
        self.datalines[d.dataline_name] = d
    
    def setup(self):

        for dataline_obj in self.datalines.values():
            dateline_curve_obj = self.plot(dataline_obj.x, dataline_obj.y)
            dataline_obj.curveline(dateline_curve_obj)