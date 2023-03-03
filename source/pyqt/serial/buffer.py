import re
from data.data_packager import DataPackager

class Buffer():

    def __init__(self) -> None:
        self._raw_input = ""

        self._buffer = ""

        self.start_char = "<"

        self.end_char = ">"

        self.datapackets = []

        self.dp = DataPackager()

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

        
        else: 
            #print(f"NO DATAPACKETS FOUND: {self._buffer}")
            pass

    def clear_buffer(self) -> None:

        for data in self.datapackets:

            self._buffer = self._buffer.replace(data, "")

        self._buffer = self._buffer.replace("\n", "")

    def add_to_datapacket(self, dp: re.finditer) -> None:

        for data in dp:
            temp = self.start_char + self._buffer[data.start(): data.end()] + self.end_char
            
            self.datapackets.append(temp)
            #print(f"DATA IS: {self._buffer[data.start(): data.end()]}")