class GeneralData():

    def __init__(self) -> None:
        self.data_list = {}

        self.delimiting_letter = ""

        self.empty = True

    def organize_split(self, l : list) -> None:
        pass

    def update_regex(self):
        self.regex_match = f"(?<={self.delimiting_letter})(.*)(?={self.delimiting_letter})"

    def clear(self):
        for item in self.data_list:
            self.data_list[item] = -1


class SuspensionData(GeneralData):

    def __init__(self) -> None:
        super().__init__()
        
        self.delimiting_letter = "S"

        self.data_map = {
            "front_right" : 0,
            "front_left" : 0,
            "back_right" : 0,
            "back_left" : 0,
        }

        self.update_regex()


    def organize_split(self, l : list) -> None:
        for idx, val in enumerate(self.data_list):
            self.data_list[val] = int(l[idx])

    @property
    def front_right(self):
        return self.data_list["front_right"]
    
    @property
    def front_left(self):
        return self.data_list["front_left"]
    
    @property
    def back_right(self):
        return self.data_list["back_right"]
    
    @property
    def back_left(self):
        return self.data_list["back_left"]


class GPSData(GeneralData):

    def __init__(self) -> None:
        super().__init__()

        self.delimiting_letter = "G"

        self.data_list = {
            "latitude" : 0,
            "longitude" : 0
        }

        self.update_regex()

    def organize_split(self, l : list) -> None:
        for idx, val in enumerate(self.data_list):
            self.data_list[val] = float(l[idx])

    @property
    def latitude(self):
        return self.data_list["latitude"]
    
    @property
    def longitude(self):
        return self.data_list["longitude"]


class RPMData(GeneralData):

    def __init__(self) -> None:
        super().__init__()

        self.delimiting_letter = "R"

        self.data_list = {
            "front_right" : 0,
            "front_left" : 0,
            "back" : 0,
        }

        self.update_regex()

    def organize_split(self, l : list) -> None:

        for idx, val in enumerate(self.data_list):
            self.data_list[val] = float(l[idx])

    @property
    def front_right(self):
        return self.data_list["front_right"]
    
    @property
    def front_left(self):
        return self.data_list["front_left"]
    
    @property
    def back(self):
        return self.data_list["back"]

class ByteMap:

    def __init__(self) -> None:
        self.h = {}

    def add_datatype(self, datatype: str) -> None:

        self.h[datatype] = []

    def set_bytes_for_datatype(self, datatype: str, byte_indices: list) -> None:
        
        self.h[datatype] = byte_indices
