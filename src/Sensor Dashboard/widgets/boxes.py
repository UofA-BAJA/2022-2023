MAX_AMOUNT_OF_BOXES = 10
MAX_AMOUNT_OF_CHARS = 100

class Boxes():

    def __init__(self) -> None:
        self.all_boxes = {}

        self.target = 0

        for i in range(0, MAX_AMOUNT_OF_BOXES):
            self.all_boxes[i] = ""

    def update_box(self, input: str):
        """logic here"""
        
        if len(self.all_boxes[self.target]) > MAX_AMOUNT_OF_CHARS:
            
            if self.target == 9: 
                self.all_boxes[0] = ""
                

            else: self.all_boxes[self.target + 1] = ""

            self.target += 1

            if self.target == 10:
                self.target = 0

        self.all_boxes[self.target] += input

    def compress(self) -> list:
        temp = []
        big_str = ""

        if (self.target == MAX_AMOUNT_OF_BOXES - 1):
            for i in range(0,MAX_AMOUNT_OF_BOXES):
                big_str += self.all_boxes[i]
        else:        
            for i in range(self.target + 1, MAX_AMOUNT_OF_BOXES, 1):
                temp.append(i)
                big_str += self.all_boxes[i]

            for i in range(0, self.target + 1, 1):
                temp.append(i)
                big_str += self.all_boxes[i]

        #print(temp)
        return big_str
