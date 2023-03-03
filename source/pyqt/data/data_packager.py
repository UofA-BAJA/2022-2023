from data.general_data_class import GeneralData, SuspensionData, GPSData, RPMData

import re

import time

class DataPackager():
    "GETS A SINGLE LINE FROM BUFFER AND THEN MAKES IT EASY FOR THE PROGRAMMER TO GET IT"
    def __init__(self) -> None:
        self._newpacket = ""

        self.suspension = SuspensionData()

        self.gps = GPSData()

        self.rpm = RPMData()

        self.data_classes = [self.suspension, self.gps, self.rpm]

        self.diff = time.time()

    def parse_packets(self, newpacket: list):
        new_packet_size = len(newpacket)

        if new_packet_size == 0:
            return
        else: 
            self.diff = time.time() - self.diff
            print(self.diff)       
        #print(f"NEW PACKET: {newpacket}")

        for packet in newpacket:

           for dataclass in self.data_classes:
               
               self.match_dataclass(dataclass, packet)

    def match_dataclass(self, dc: GeneralData, packet: str) -> None:

        text = re.search(dc.regex_match, packet)
      
        if text is not None:
            individual_nums_as_str = re.split(',',text.group())

            dc.organize_split(individual_nums_as_str)

        else: dc.empty = True