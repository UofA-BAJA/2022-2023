class SerialHandler():

    def __init__(self, num_of_datapoints: int) -> None:
        self.x = [i for i in range(num_of_datapoints)]
        self.y = [0 for i in range(num_of_datapoints)]
        self.y1 = [0 for i in range(num_of_datapoints)]
        self.y2 = [0 for i in range(num_of_datapoints)]
        self.y3 = [0 for i in range(num_of_datapoints)]
        self.num_of_datapoints = num_of_datapoints

        self.temp_new_y = []
        self.temp_old_y = [0 for i in range(num_of_datapoints)]

    def input_data(self, input: str) -> None:
        str_data = input.split(",")
        raw_num_data = [float(x) for x in str_data]
        return raw_num_data

    def ShiftLeft(self, list1, newVal):
        list1.pop(0)
        list1.append(newVal)
        return list1