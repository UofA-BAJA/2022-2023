import struct

from data.general_data_class import *

class DataPacket():

    def __init__(self, configuration: int) -> None:
        self.datatypes = []

        self.fill_datatypes_list(configuration=configuration)

    def fill_datatypes_list(self, configuration: int):

        configs = {
            1 : [
                FrontRightSuspension(),
                FrontLeftSuspension(),
                RearRightSuspension(),
                RearLeftSuspension(),
                FrontLeftRPM(),
                FrontRightRPM(),
                RearRPM(),
                Latitude(),
                Longitude(),
                Speed()
                ]
            }
        
        self.datatypes = configs[configuration]


class ByteMap():

    def __init__(self) -> None:
        self.byte_map = {}

    def add_datatype(self, datatype: GeneralData) -> None:

        if not self.byte_map:
            self.byte_map[datatype] = [1, datatype.byte_length]
        else:
            curr_max_index = 0

            for indices_list in self.byte_map.values():
                
                if indices_list[1] > curr_max_index:
                    curr_max_index = indices_list[1]

            self.byte_map[datatype] = [curr_max_index + 1, (curr_max_index + 1) + datatype.byte_length-1]

            

class DataPackager():
    specialByte = 252
    "GETS A SINGLE LINE FROM BUFFER AND THEN MAKES IT EASY FOR THE PROGRAMMER TO GET IT"
    def __init__(self) -> None:
        self._newpacket = ""

        


    def parse(self, byteArr: list):
        self.b = ByteMap()
        
        just_data_bytes = self.delete_esc_bytes(byteArr)

        byte_config_selector = ord(just_data_bytes[0])

        datapacket = DataPacket(byte_config_selector)

        for datatype in datapacket.datatypes:
            self.b.add_datatype(datatype)

        for datatype in datapacket.datatypes:
            self.fill_datapacket(datatype, just_data_bytes)
        
        

    def fill_datapacket(self, datatype: GeneralData, in_bytes: list):
        
        bytes_index = self.b.byte_map[datatype]

        print(f"LENGTH IS {len(in_bytes[bytes_index[0]: bytes_index[1] + 1])}")

        temp_bytes = bytes("".join(in_bytes[bytes_index[0]: bytes_index[1] + 1]), "utf-8")

        print(f"FOR {datatype} BYTE INDEX IS {bytes_index}")
        print(f"CONVERTED {in_bytes[bytes_index[0]: bytes_index[1] + 1]} to {temp_bytes}")
        datatype.value_as_real_num = struct.unpack(datatype.struct_format, temp_bytes )

        print(datatype.value_as_real_num)

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





    
