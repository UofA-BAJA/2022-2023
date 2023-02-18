class Hertz():
    def __init__(self, num_of_datapoints: int) -> None:
        self.x = [i for i in range(num_of_datapoints)]
        self.y = [0 for i in range(num_of_datapoints)]
        self.two_times = [.000000001,.0000000001]
        self.num_of_datapoints = num_of_datapoints

    def difference(self, times: list) -> int:
        difference = times[1] - times[0]
        return difference
    
    def inverse(self, input: int) -> float:
        inverse = 1/input
        return inverse
    
    def ShiftLeft_for_Hertz(self, list1, newVal):
        list1.pop(0)
        list1.append(newVal)
        return list1
