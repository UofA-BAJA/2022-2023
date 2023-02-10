import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtChart import QChart, QLineSeries, QValueAxis
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("PyQt Window with Graphs and Buttons")

central_widget = QWidget()
layout = QVBoxLayout()

def generate_data():
    # generate random data for the graph
    data = [random.randint(0, 100) for i in range(10)]
    return data

def update_graph():
    # update the data in the graph
    series.clear()
    data = generate_data()
    for i in range(len(data)):
        series.append(i, data[i])

# create a line graph
chart = QChart()
chart.setTitle("Random Data")

series = QLineSeries()
data = generate_data()
for i in range(len(data)):
    series.append(i, data[i])

chart.addSeries(series)

# set the x and y axis labels
axis_x = QValueAxis()
axis_x.setTitleText("X-Axis")
axis_x.setRange(0, 10)
chart.addAxis(axis_x, Qt.AlignBottom)
series.attachAxis(axis_x)

axis_y = QValueAxis()
axis_y.setTitleText("Y-Axis")
axis_y.setRange(0, 100)
chart.addAxis(axis_y, Qt.AlignLeft)
series.attachAxis(axis_y)

layout.addWidget(chart)

# create a button to update the data in the graph
update_button = QPushButton("Update")
update_button.clicked.connect(update_graph)
layout.addWidget(update_button)

central_widget.setLayout(layout)
window.setCentralWidget(central_widget)

window.show()
sys.exit(app.exec_())
