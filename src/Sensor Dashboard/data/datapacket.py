import struct

from data.general_data_class import *


class DataPacket():

    def __init__(self) -> None:
        self.datatypes = []
        self.__byte_map = None

    @property
    def all_new_data(self) -> dict:
        '''returns a dict that is 
        {
            "sensor_name" : sensor_obj
        }'''

        new_data = {}

        for datatype in self.datatypes:

            if datatype.is_new:

                new_data[datatype.name] = datatype




        
    