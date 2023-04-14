class GeneralData():

    def __init__(self) -> None:
        self.struct_format = ""

        self.name = ""

        self._real_value = 0

        self.min_value = 0
        self.max_value = 0

        self.previous_value = 0

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
    
    @property
    def real_value(self):
        return self._real_value
    
    @real_value.setter
    def real_value(self, input_value):
        self._real_value = input_value

        self.previous_value = input_value

    
   
    def value_in_range(self, input_value) -> bool:
        
        if self.min_value > input_value or self.max_value < input_value:
            return False
        
        return True


class SuspensionData(GeneralData):

    def __init__(self) -> None:
        super().__init__()

        self.struct_format = "h"

        self.max_value = 1024
        self.min_value = 0

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
        
class GPSData(GeneralData):

    def __init__(self) -> None:
        super().__init__()
        
        self.struct_format = "f"

        self.min_value = -50
        self.max_value = 200

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

        self.min_value = -1

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
