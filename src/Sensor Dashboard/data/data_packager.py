import struct

from data.general_data_class import *

class DataPacket():

    def __init__(self, configuration: int) -> None:
        self.datatypes = []

        self.data = {}

        self.fill_datatypes_list(configuration=configuration)

    def fill_datatypes_list(self, configuration: int):

        self.configs = {
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
        
        self.datatypes = self.configs[configuration]

        def fill_dict(datatype: GeneralData):
            self.data[datatype.name] = datatype

        for datatype in self.datatypes:
            fill_dict(datatype)

    def get_all_valid_configurations(self) -> list:
        
        config_selection_keys = [config_num for config_num, config in self.configs]

        return config_selection_keys


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

        #print(f"length of input bytes {len(just_data_bytes)}")
        for datatype in datapacket.datatypes:
            
            self.fill_datapacket(datatype, just_data_bytes)

        return datapacket
        

    def fill_datapacket(self, datatype: GeneralData, in_bytes: list):
        
        bytes_index_list = self.b.byte_map[datatype]

        #print(f"FOR {datatype} BYTE INDEX IS {bytes_index_list} and CONVERTED {in_bytes[bytes_index_list[0]: bytes_index_list[1] + 1]} to {temp_bytes}")
        #print(f"THIS MIGHT WORK {b''.join(in_bytes[bytes_index_list[0]: bytes_index_list[1] + 1])}")

        matched_bytes_hex = in_bytes[bytes_index_list[0]: bytes_index_list[1] + 1] #gets the appropiate datatype byte indecies from in bytes

        match_bytes_bytearray = bytearray([ord(x) for x in matched_bytes_hex]) 
       
        #print(f"diff is old: {type(temp_bytes)} and new:{type(new_temp)} maybe this {bytearray(t)}")
        try:
            datatype.real_value = struct.unpack(datatype.struct_format, match_bytes_bytearray )[0]
        except struct.error:
            print(f"FAILED ON {match_bytes_bytearray} trying to match to {datatype.name}")
            print(f"LEN of inbytes is {len(in_bytes)}")

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
    
    def validate_data(self, byteArr: list) -> bool:
        '''True means data is good
        False means data is no good'''
        b = DataPacket(1)

        config_select_byte = byteArr[0]
        
        if ord(config_select_byte) not in b.configs.keys():
            print(f"BAD CONFIG KEY {config_select_byte}")
            return False
        
        config_length = 0
        for datatype in b.datatypes:
            config_length += datatype.byte_length
        
        if config_length+1 != len(byteArr):
            print(f"config length is {config_length} but data length is {len(byteArr)}")
            print(f"input is {byteArr}")

            return False
        
        
        return True