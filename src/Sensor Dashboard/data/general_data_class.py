class GeneralDatatype():

    def __init__(self, name, byte_length, units, value_range) -> None:

        self.name = name

        self.byte_length = byte_length

        self.units = units

        self.__value = None

        self.is_new = False

        self.maximum_value = value_range[1]

        self.minimum_value = value_range[0]

    @property
    def struct_format(self) -> str:
        if (self.byte_length == 2):
            return "h"
        elif (self.byte_length == 4):
            return "f"
        else:
            return -1
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, new_value):
        self.__value = new_value

        self.is_new = True


class SuspensionData(GeneralDatatype):

    def __init__(self) -> None:
        super().__init__()

        self.struct_format = "h"

class FrontRightSuspension(SuspensionData):

    def __init__(self) -> None:
        super().__init__()

        self.name = "front_right_suspension"
        

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

        
        
class GPSData(GeneralDatatype):

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


class RPMData(GeneralDatatype):

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
