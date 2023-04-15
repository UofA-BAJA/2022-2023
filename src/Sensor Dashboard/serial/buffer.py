import re
from data.data_packager import DataPackager
from PyQt5 import QtSerialPort

class Buffer():
    startMarker = 250
    endMarker = 251


    def __init__(self) -> None:
        self._raw_input = ""

        self._buffer = []

        self.raw_output = []

        self.datapackets = []

        self.raw_bytes_rcvd = 0

        self.full = False
             

    def set_serial(self, serial: QtSerialPort) -> None:
        self.serial = serial

    @property
    def raw_input(self): 
        return self._raw_input
    
    @raw_input.setter
    def raw_input(self, new):
        self._raw_input = new

        self.full = False
        
        self._buffer += new

        startIndex = endIndex = 0

        for byteIndex, byte in enumerate(self._buffer):

            if ord(byte) == self.startMarker:
                startIndex = byteIndex

            if ord(byte) == self.endMarker and byteIndex > startIndex:
                endIndex = byteIndex
                break

        if not endIndex:
            #print(f"IN BUFFER: {self._buffer} NO START AND STOP FOUND")
            return

        #print(f"START INDEX IS {startIndex}, END INDEX IS {endIndex}")
        
        self.raw_output = [b for b in self._buffer[startIndex + 1:endIndex]]
        
        del self._buffer[startIndex: endIndex + 1]
        
        self.full = True
        #print(self.raw_output)
            
