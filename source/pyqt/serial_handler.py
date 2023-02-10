class SerialHandler():

    def __init__(self, num_of_datapoints: int) -> None:
        self.x = [i for i in range(num_of_datapoints)]
        self.y = [0 for i in range(num_of_datapoints)]
        self.num_of_datapoints = num_of_datapoints

        self.temp_new_y = []
        self.temp_old_y = [0 for i in range(num_of_datapoints)]

    def testing(self) -> None:

        self.x = [1,2,3,4]
        self.y = [1,2,3,4]

    def input_data(self, input: str) -> None:

        str_data = input.split(",")
        raw_num_data = [float(x) for x in str_data]
        #print(raw_num_data)

        
        c = 1
        if (c < self.num_of_datapoints):
            if (len(self.temp_new_y) == self.num_of_datapoints): 
                c = 1
                self.temp_old_y = self.temp_new_y
                self.temp_new_y = []
                

            new_data_point = raw_num_data[0]

            self.temp_new_y.append(new_data_point)
            

            self.temp_old_y = self.temp_old_y[0:self.num_of_datapoints-len(self.temp_new_y)]

            c += 1

        full_y = self.temp_old_y + self.temp_new_y
        print(f"new y len: {len(self.temp_new_y)}, old y len {len(self.temp_old_y)}")
        self.y = full_y

        

    