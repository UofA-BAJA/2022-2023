import numpy as np

DATA_FILE_PATH = r"C:\Users\alexr\Documents\Baja\fast datalogging\DATA\testing\AvrAdc02.csv"

with open(DATA_FILE_PATH) as f:
    first = next(f)
    data_reading_rate_hz = 1 / (float(first.split(",")[1]) * 10**(-6))
    #print(data_reading_rate_hz)
    second = next(f)
    pin4, pin5, pin6, pin7 = [x for x in second.split(",")]

    arr = np.genfromtxt(f, delimiter=",") # no skiprows here

num_of_rows = np.arange(arr.shape[0]).reshape(arr.shape[0], 1)

temp_time_array = num_of_rows / np.full((arr.shape[0], 1), data_reading_rate_hz)

data_with_time = np.hstack((temp_time_array, arr))

print(temp_time_array)

print(data_with_time)