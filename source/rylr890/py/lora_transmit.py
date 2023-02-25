import serial.tools.list_ports

# print serial ports
print("Available COM Ports:")
for port in serial.tools.list_ports.comports():
    print(f"{port.device} - {port.description}")

# user select port
selected_port = input("Enter the name of the COM port to use: ")
ser = serial.Serial(selected_port, 115200)

# user input transmittd string thing
while True:
    transmit_str = input("Enter the string to transmit: ")

    #send
    command = f"AT+SEND=1,{len(transmit_str)},{transmit_str}\r\n"
    ser.write(command.encode())

    #print
    response = ser.readline().decode().strip()
    print(response)
