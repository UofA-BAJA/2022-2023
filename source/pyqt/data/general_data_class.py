class GeneralData():

    def __init__(self) -> None:
        self.struct_format = ""

        self.order = []


class SuspensionData(GeneralData):

    def __init__(self) -> None:
        super().__init__()

        self.front_right = 0
        self.front_left = 0
        self.back_right = 0
        self.back_left = 0

        self.order = [self.front_right, self.front_left, self.back_right, self.back_left]
        self.struct_format = "h"

class GPSData(GeneralData):

    def __init__(self) -> None:
        super().__init__()

        self.latitude = 0
        self.longitude = 0
        self.speed = 0
        
        self.struct_format = "f"


class RPMData(GeneralData):

    def __init__(self) -> None:
        super().__init__()
        
        self.front_left = 0
        self.front_right = 0
        self.rear = 0
        
        self.struct_format = "h"
