import numpy as np
from matplotlib import pyplot as plt 

DATA_FILE_PATH = r"C:\Users\alexr\Documents\Baja\fast datalogging\DATA\testing\AvrAdc02.csv"

MICROSECONDS = 10**(-6)

REF_VOLTAGE = 5

ADC_RESOLUTION = 1024

with open(DATA_FILE_PATH) as f:
    first = next(f)
    data_reading_rate_hz = 1 / (float(first.split(",")[1]) * MICROSECONDS)
    #print(data_reading_rate_hz)
    second = next(f)
    col_names = [x for x in second.split(",")]

    arr = np.genfromtxt(f, delimiter=",")

    num_of_rows = arr.shape[0]
    num_of_cols = arr.shape[1]


rows_arr = np.arange(num_of_rows).reshape(num_of_rows, 1)

temp_time_array = rows_arr / np.full((num_of_rows, 1), data_reading_rate_hz)

adc_resolution_array = np.full((num_of_rows, num_of_cols), REF_VOLTAGE / ADC_RESOLUTION)

temp_voltage_array = arr / adc_resolution_array

analog_read_data_with_time = np.hstack((temp_time_array, arr)).transpose()
voltage_data_with_time = np.hstack((temp_time_array, temp_voltage_array)).transpose()

#print(temp_time_array)

fig, (ax1, ax2) = plt.subplots(2)

for i in range(1,5):
    ax1.plot(analog_read_data_with_time[0], analog_read_data_with_time[i], label=str(col_names[i-1]))
ax1.legend()
ax1.set_xlabel('Time (s)')  # Add an x-label to the axes.
ax1.set_ylabel('Analog Value From Arduino')  # Add a y-label to the axes.
ax1.set_title("Time vs Analog Value")
plt.show()
