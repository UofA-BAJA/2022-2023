import numpy as np

DATA_FILE_PATH = r"C:\Users\alexr\Documents\Baja\fast datalogging\DATA\testing\AvrAdc02.csv"

with open(DATA_FILE_PATH) as f:
    first = next(f)
    data_reading_rate_hz = 1 / (float(first.split(",")[1]) * 10**(-6))
    #print(data_reading_rate_hz)
    second = next(f)
    pin4, pin5, pin6, pin7 = [x for x in second.split(",")]
    arr = np.genfromtxt(f, delimiter=",") # no skiprows here

print(arr.shape[0])
timestamped = np.array(np.arange(arr.shape[0]), arr)