import struct
import json
import os

from data.general_data_class import *
from data.datapacket import DataPacket

class ByteMap():

    def __init__(self) -> None:
        self.byte_map = {}
        self.config_number = 0

    def add_datatype(self, datatype: GeneralDatatype) -> None:

        if not self.byte_map:
            self.byte_map[datatype] = [1, datatype.byte_length]
        else:
            curr_max_index = 0

            for indices_list in self.byte_map.values():
                
                if indices_list[1] > curr_max_index:
                    curr_max_index = indices_list[1]

            self.byte_map[datatype] = [curr_max_index + 1, (curr_max_index + 1) + datatype.byte_length-1]

    def create_byte_map(self, datatypes :list[GeneralDatatype]) -> dict[GeneralDatatype: [int, int]]:
        pass

            

class DataPackager():
    specialByte = 252
    "GETS A SINGLE LINE FROM BUFFER AND THEN MAKES IT EASY FOR THE PROGRAMMER TO GET IT"
    def __init__(self) -> None:
        
        json_data_path = os.path.abspath(os.getcwd()) + "\.config\data.json"

        self.json_dict = json.load(open(json_data_path))
        
        self.all_datatypes = self.create_all_datatypes()

        self.all_byte_maps = self.create_all_byte_maps()

        #print(self.all_datatypes)

    def create_all_datatypes(self) -> list[GeneralDatatype]:

        all_datatypes = []

        for datatype in self.json_dict["datatypes"]:
            all_datatypes.append(GeneralDatatype(datatype["sensor_name"], datatype["byte_length"], datatype["units"]))

        return all_datatypes
    
    def create_all_byte_maps(self) -> list[ByteMap]:
        all_byte_maps = []

        for data_configuration in self.json_dict["data_configurations"]:
            empty = ByteMap()

            empty.config_number =  data_configuration["configuration_number"]

            for datatype_name in data_configuration["datatype_order"]:
                
                for datatype in self.all_datatypes:
                    #print(datatype_name)
                    if datatype.name == datatype_name:
                        empty.add_datatype(datatype)
                        break

            all_byte_maps.append(empty)

        #print(all_byte_maps)

    def parse(self, byteArr: list) -> DataPacket:
        '''converts the bytes in to the datapacket'''
        pass
        
        

    def fill_datapacket(self, datatype: GeneralDatatype, in_bytes: list):
        
        bytes_index = self.b.byte_map[datatype]

        #print(f"LENGTH IS {len(in_bytes[bytes_index[0]: bytes_index[1] + 1])}")

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
    
    def validate_configuration(self, input_bytes) -> bool:
        '''if datapacket has a valid configuration number
        return true'''
        self.new_datapacket = DataPacket()

        configuration_number = input_bytes[0]

        matching_byte_map = None

        for bytemap in self.all_byte_maps:

            if bytemap.config_number == configuration_number:
                self.new_datapacket.datatypes.append(bytemap.byte_map.keys())
                break
                for datatype in bytemap.byte_map.keys():
                    self.new_datapacket.datatypes.append(datatype)

        if matching_byte_map is None:
            print(f"No byte map for config {configuration_number}")
            return False
        else: return True