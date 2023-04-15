import struct

from data.general_data_class import *


class DataPacket():

    def __init__(self) -> None:
        self.__byte_map = None

        self.data = {}



    def fill_data(self, datatype_name, value):

        self.data[datatype_name] = value

    




        
    