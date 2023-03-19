from data.general_data_class import GeneralData, SuspensionData, GPSData, RPMData

import re

class DataPackager():
    specialByte = 252
    "GETS A SINGLE LINE FROM BUFFER AND THEN MAKES IT EASY FOR THE PROGRAMMER TO GET IT"
    def __init__(self) -> None:
        self._newpacket = ""

        self.data_packet = DataPacket()



    def parse(self, byteArr: list):
        
        just_data_bytes = self.delete_esc_bytes(byteArr)

        byte_config_selector = ord(just_data_bytes[0])

        byte_config = self.choose_byte_config(byte_config_selector)

        self.data_packet.suspension.front_right = byte_config
        
    def choose_byte_config(self, config_num) -> None:

        pass

    def delete_esc_bytes(self, byteArr) -> list:
        r_bytes = []
        specialByteFlag = False

        for byteIndex, byte in enumerate(byteArr):

            if ord(byte) == self.specialByte:
                nextByte = byteArr[byteIndex + 1]

                r_bytes.append(bytes([ord(nextByte) ^ self.specialByte]))

                specialByteFlag = True
                continue

            if specialByteFlag:
                specialByteFlag = False
                continue

            r_bytes.append(byte)

        return r_bytes

class ByteConfiguration():

    def __init__(self) -> None:
        self.config = {}

        self.suspension = SuspensionData()
        self.rpms = RPMData()
        self.gps = GPSData()

    def set_bytes():
        pass

class DataPacket():

    def __init__(self) -> None:
        self.suspension = SuspensionData()

        self.gps = GPSData()

        self.rpm = RPMData()

    
