from data.general_data_class import *

class DataPacket():

    def __init__(self, configuration: int) -> None:
        self.datatypes = []

        self.data = {}

        self.fill_datatypes_list(configuration=configuration)

    def fill_datatypes_list(self, configuration: int):

        configs = {
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
        
        self.datatypes = configs[configuration]

        def fill_dict(datatype: GeneralDatatype):
            self.data[datatype.name] = datatype

        for datatype in self.datatypes:
            fill_dict(datatype)

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
        