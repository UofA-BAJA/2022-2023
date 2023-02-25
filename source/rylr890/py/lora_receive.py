import serial.tools.list_ports
import serial

# Print COMs
print("Available COM ports:")
for port in serial.tools.list_ports.comports():
    print(f"{port.device} - {port.description}")

# Prompt to select a COM port
port = input("Enter the COM port to use: ")

# Open serial port
ser = serial.Serial(port, 115200)

# LoRa module address 1
ser.write(b'AT+ADDRESS=1\r\n')
response = ser.readline().decode().strip()
print(response)

# receive mode
ser.write(b'AT+MODE=0\r\n')
response = ser.readline().decode().strip()
print(response)

# read from LoRa module
while True:
    response = ser.readline().decode().strip()
    if len(response) > 0:
        print(response)