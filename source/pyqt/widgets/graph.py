from PyQt5 import QtWidgets
import pyqtgraph as pg

class GraphWidget(pg.PlotWidget):
    num_of_datapoints = 100
    def __init__(self, y_plots):
        super(GraphWidget, self).__init__()

        self.x = [0 for x in range(self.num_of_datapoints)]

        self.y = []
        for i in range(y_plots):
            self.y.append([0 for x in range(self.num_of_datapoints)])
        

    def setup(self):
        self.curves = []
        for i in range(len(self.y)):
            self.curves.append(self.plot(self.x, self.y[i]))

        print(self.curves)
        
    def appendY(self, datapoint):

        for i in range(len(self.y)):
            self.y[i] = self.y[i][1:]
            self.y[i].append(datapoint)

    def update(self):
        for curve in self.curves:
            self.update_data_line(curve)

    def update_data_line(self, curve: pg.PlotDataItem) -> None:

        curve.setData(self.x, self.y[0])