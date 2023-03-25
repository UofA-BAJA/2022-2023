import struct

from data.general_data_class import *

class DataPacket():

    def __init__(self, configuration: int) -> None:
        self.datatypes = []

        self.data = {}

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

        def fill_dict(datatype: GeneralData):
            self.data[datatype.name] = datatype

        for datatype in self.datatypes:
            fill_dict(datatype)

    @property
    def front_right_suspension(self):
        return self.data[FrontRightSuspension().name].real_value

    @property
    def front_left_suspension(self):
        return self.data[FrontLeftSuspension().name].real_value
    
    @property
    def rear_right_suspension(self):
        return self.data[RearRightSuspension().name].real_value
    
    @property
    def rear_left_suspension(self):
        return self.data[RearLeftSuspension().name].real_value
    
    @property
    def front_right_rpm(self):
        return self.data[FrontRightRPM().name].real_value

    @property
    def front_left_rpm(self):
        return self.data[FrontLeftRPM().name].real_value
    
    @property
    def rear_rpm(self):
        return self.data[RearRPM().name].real_value
    
    @property
    def latitude(self):
        return self.data[Latitude().name].real_value
    
    @property
    def longitude(self):
        return self.data[Longitude().name].real_value
    
    @property
    def speed(self):
        return self.data[Speed().name].real_value
    
    def __repr__(self) -> str:
        temp = ""

        for datatype_name in self.data:
            temp += f"\n{datatype_name}: {self.data[datatype_name].real_value}"

        return temp
    
    @property
    def length_in_bytes(self):
        "TODO: ITERATE THROUGH DATATYPES.BYTES LENGTH AND ADD THEM UP"
        pass
        

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
        pass

    def parse(self, byteArr: list) -> DataPacket:
        self.b = ByteMap()
        
        just_data_bytes = self.delete_esc_bytes(byteArr)

        byte_config_selector = ord(just_data_bytes[0])

        datapacket = DataPacket(byte_config_selector)

        for datatype in datapacket.datatypes:
            self.b.add_datatype(datatype)

        for datatype in datapacket.datatypes:
            self.fill_datapacket(datatype, just_data_bytes)

        return datapacket
        
        

    def fill_datapacket(self, datatype: GeneralData, in_bytes: list):
        
        bytes_index = self.b.byte_map[datatype]

        print(f"LENGTH IS {len(in_bytes[bytes_index[0]: bytes_index[1] + 1])}")

        temp_bytes = None
        for i in range(bytes_index[0], bytes_index[1] + 1 ):
            if i == bytes_index[0]:
                temp_bytes = in_bytes[i]
            else:
                temp_bytes += in_bytes[i]

        #print(f"FOR {datatype} BYTE INDEX IS {bytes_index}")
        #print(f"CONVERTED {in_bytes[bytes_index[0]: bytes_index[1] + 1]} to {temp_bytes}")
        datatype.real_value = struct.unpack(datatype.struct_format, temp_bytes )[0]


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





    
