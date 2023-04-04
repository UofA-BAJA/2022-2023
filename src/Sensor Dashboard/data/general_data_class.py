class GeneralData():

    def __init__(self) -> None:
        self.struct_format = ""

        self.name = ""

        self.real_value = 0

    @property
    def byte_length(self):
        if (self.struct_format == "h"):
            return 2
        elif (self.struct_format == "f"):
            return 4
        else:
            return -1
    
    @property
    def exists(self):
        return bool(self.real_value)


class SuspensionData(GeneralData):

    def __init__(self) -> None:
        super().__init__()

        self.struct_format = "h"

class FrontRightSuspension(SuspensionData):

    def __init__(self) -> None:
        super().__init__()

        self.name = "front_right_suspension"

        self.exists
        

class FrontLeftSuspension(SuspensionData):

    def __init__(self) -> None:
        super().__init__()

        self.name = "front_left_suspension"

class RearRightSuspension(SuspensionData):

    def __init__(self) -> None:
        super().__init__()

        self.name = "rear_right_suspension"

class RearLeftSuspension(SuspensionData):

    def __init__(self) -> None:
        super().__init__()

        self.name = "rear_left_suspension"

        
        
class GPSData(GeneralData):

    def __init__(self) -> None:
        super().__init__()
        
        self.struct_format = "f"

class Latitude(GPSData):

    def __init__(self) -> None:
        super().__init__()

        self.name = "latitude"

class Longitude(GPSData):

    def __init__(self) -> None:
        super().__init__()

        self.name = "longitude"

class Speed(GPSData):

    def __init__(self) -> None:
        super().__init__()

        self.name = "speed"


class RPMData(GeneralData):

    def __init__(self) -> None:
        super().__init__()
        
        self.struct_format = "h"

class FrontLeftRPM(RPMData):

    def __init__(self) -> None:
        super().__init__()

        self.name = "front_left_rpm"

class FrontRightRPM(RPMData):

    def __init__(self) -> None:
        super().__init__()

        self.name = "front_right_rpm"


class RearRPM(RPMData):

    def __init__(self) -> None:
        super().__init__()

        self.name = "rear_rpm"
