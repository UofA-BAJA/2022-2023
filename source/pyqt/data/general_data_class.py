class GeneralData():

    def __init__(self) -> None:
        self.data_list = {}

        self.delimiting_letter = ""

        self.empty = True

    def organize_split(self, l : list) -> None:
        pass

    def update_regex(self):
        self.regex_match = f"(?<={self.delimiting_letter})(.*)(?={self.delimiting_letter})"


class SuspensionData(GeneralData):

    def __init__(self) -> None:
        super().__init__()
        
        self.delimiting_letter = "S"

        
        self.front_right = 0
        self.front_left = 0
        self.back_right = 0
        self.back_left = 0

        self.data_list = {
            "front_right" : self.front_right,
            "front_left" : self.front_left,
            "back_right" : self.back_right,
            "back_left" : self.back_left,
        }

        self.update_regex()


    def organize_split(self, l : list) -> None:
        for idx, val in enumerate(self.data_list):
            self.data_list[val] = int(l[idx])


class GPSData(GeneralData):

    def __init__(self) -> None:
        super().__init__()

        self.delimiting_letter = "G"

        self.lat = 0
        self.lon = 0

        self.data_list = {
            "latitude" : self.lat,
            "longitude" : self.lon
        }

        self.update_regex()

    def organize_split(self, l : list) -> None:
        for idx, val in enumerate(self.data_list):
            self.data_list[val] = float(l[idx])


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

    