from PyQt5 import QtWidgets, QtSerialPort, QtCore
import re

class SerialHandler:
    '''this class is responsible for 
    starting the serial port
    giving the serial port data to the ui controller
    '''
    def __init__(self, serial_port_address_name) -> None:
        self.address = serial_port_address_name
        
        self.dv = DataValidator()
        #self.setupPort(serial_port_address_name)

    def setupPort(self) -> None:
        self.serial_port = QtSerialPort.QSerialPort( #connect the arduino
            self.address,
            baudRate = QtSerialPort.QSerialPort.BaudRate.Baud115200,         
        )

        self.serial_port.readyRead.connect(self.readPort)


    def readPort(self) -> None:
        
        self.raw_input = self.serial_port.readAll().data().decode()
        
        self.update()
        #print(self.dv._raw_input)
    
    def setUIController(self, c) -> None:
        self.c = c

    def update(self) -> None:
        
        self.c.newSerialInput =  self.raw_input

        self.dv.raw_input = self.raw_input
        for data in self.dv.datapackets:
            self.c.newDataPacket = data


class DataValidator():

    def __init__(self) -> None:
        self._raw_input = ""

        self._buffer = ""

        self.start_char = "<"

        self.end_char = ">"

        self.datapackets = []


    @property
    def raw_input(self): 
        return self._raw_input
    
    @raw_input.setter
    def raw_input(self, new):
        self._raw_input = new

        
        self._buffer += new
        #print(f"\n\nBUFFER UPDATE :{self._buffer}")

        self.process_buffer()


    def process_buffer(self):
        self.datapackets = []

        pattern=r"(?<=\<)(.*?)(?=\>)"

        string=self._buffer

        datapackets_flag = re.search(pattern=pattern, string=string)
       
        datapackets = re.finditer(pattern=pattern, string=string)

        if datapackets_flag is not None:
            
            self.add_to_datapacket(datapackets)

            self.clear_buffer()

            #print(f"DATAPACKETS :{self.datapackets}")
            #print(f"PROCEESSED BUFFER :{self._buffer}")

        
        else: print(f"NO DATAPACKETS FOUND: {self._buffer}")

    def clear_buffer(self) -> None:

        for data in self.datapackets:

            self._buffer = self._buffer.replace(data, "")

        self._buffer = self._buffer.replace("\n", "")

    def add_to_datapacket(self, dp: re.finditer) -> None:

        for data in dp:
            temp = self.start_char + self._buffer[data.start(): data.end()] + self.end_char
            self.datapackets.append(temp)
            #print(f"DATA IS: {self._buffer[data.start(): data.end()]}")


    

   