from PyQt5 import QtSerialPort

class SerialHandler:
    '''this class is responsible for 
    starting the serial port
    giving the serial port data to the ui controller
    '''
    def __init__(self) -> None:
        self.serial_port = None
        self.newline_trigger = False

    def start_serial_port(self, serial_port_address_name) -> QtSerialPort.QSerialPort:
        self.serial_port = QtSerialPort.QSerialPort( #connect the arduino
            serial_port_address_name,
            baudRate=QtSerialPort.QSerialPort.BaudRate.Baud115200,
        )

    def start_reading_serial(self) -> None:

        pass
    

    
   