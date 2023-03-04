import serial.tools.list_ports
import serial
import time

# Print available serial ports
print("Available COM Ports:")
for port in serial.tools.list_ports.comports():
    print(f"{port.device} - {port.description}")

# Prompt user to select port
selected_port = input("Enter the name of the COM port to use: ")
ser = serial.Serial(selected_port, 115200, timeout=1)

# Loop for AT commands
while True:
    command = input("Enter an AT command (or 'ready' to begin transmitting): ")
    if command.lower() == "ready":
        break

    # send the at command
    command += "\r\n"
    ser.write(command.encode())

    # response
    response = ser.readline().decode().strip()
    print(response)

# string to transmit
while True:
    transmit_str = input("Enter the string to transmit: ")

    # Send string
    command = f"AT+SEND=1,{len(transmit_str)},{transmit_str}\r\n"
    ser.write(command.encode())

    # response
    response = ser.readline().decode().strip()
    print(response)
