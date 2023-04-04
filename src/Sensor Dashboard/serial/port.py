from PyQt5 import QtWidgets, QtSerialPort, QtCore

from serial.buffer import Buffer


class Port:
    '''this class is responsible for 
    starting the serial port
    giving the serial port data to the buffer
    '''
    def __init__(self) -> None:
        pass   
        #self.setupPort(serial_port_address_name)
        

    def try_serial_port(self, address):
        self.qserial_port = QtSerialPort.QSerialPort( #connect the arduino
            address,
            baudRate = QtSerialPort.QSerialPort.BaudRate.Baud115200,      
        )

        return self.qserial_port


    

   