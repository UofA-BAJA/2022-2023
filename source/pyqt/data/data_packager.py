import struct

from data.general_data_class import GeneralData, SuspensionData, GPSData, RPMData

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


    def choose_byte_config(self, config_num) -> dict:
        bc = ByteConfiguration(self.data_packet)

        return bc.match_config(config_num)

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

class DataPacket():

    def __init__(self) -> None:
        self.suspension = SuspensionData()

        self.gps = GPSData()

        self.rpm = RPMData()

class ByteConfiguration():

    def __init__(self, datapacket: DataPacket) -> None:
        self.config = {}

        self.datapacket = datapacket
    

    def config_1(self) -> list:
        '''has all data in this byte config'''
        s = ByteMap(self.datapacket.suspension, 1)
        r = ByteMap(self.datapacket.rpm, s.endIndex + 1)
        g = ByteMap(self.datapacket.rpm, r.endIndex + 1)

        config_1 = [s, r, g]

        return config_1
    
    def match_config(self, selection: int) -> dict:

        if selection == 1:
            return self.config_1()

class ByteMap:

    def __init__(self, datatype : GeneralData, startIndex: int) -> None:
        self.datatype = datatype
        self.startIndex = startIndex

    @property
    def endIndex(self):
        if self.datatype == DataPacket().suspension:
            return self.startIndex + 7
        elif self.datatype == DataPacket().gps:
            return self.startIndex + 11
        elif self.datatype == DataPacket().rpm:
            return self.startIndex + 5
        
    @property
    def struct_format(self):
        return self.datatype.struct_format



    
