from PyQt5 import QtWidgets
import pyqtgraph as pg

class DataLine():

    def __init__(self, name) -> None:
        self.dataline_name = name

        self.x = [x for x in range(100)]

        self.y = [0 for x in range(100)]

        self.pen = None

    def curveline(self, curve: pg.PlotCurveItem) -> None:
        self.curve_pbj = curve
        pass

    def setPenColor(self, redVal=255, greenVal=255, blueVal=255) -> None:
        self.pen = pg.mkPen(color=(redVal, greenVal, blueVal))


    def update(self, value):
        self.y = self.y[1:]

        self.y.append(value)

        self.curve_pbj.setData(self.x, self.y)
        #print(f"x is {self.x} \ny is {self.y}")




class GraphWidget(pg.PlotWidget):
    num_of_datapoints = 100
    def __init__(self):
        super(GraphWidget, self).__init__()

        self.datalines = {}
        pg.setConfigOption('background', 'w')
        
        self.addLegend()

      

    def add_dataline(self, d: DataLine):
        self.datalines[d.dataline_name] = d
    


    def setup(self):

        for dataline_obj in self.datalines.values():
            dateline_curve_obj = self.plot(dataline_obj.x, dataline_obj.y, pen = dataline_obj.pen)
            
            dataline_obj.curveline(dateline_curve_obj)