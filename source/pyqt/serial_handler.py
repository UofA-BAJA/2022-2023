class SerialHandler():

    def __init__(self) -> None:
        self.x = []
        self.y = []

    def testing(self) -> None:

        self.x = [1,2,3,4]
        self.y = [1,2,3,4]

    def input_data(self, input: str) -> None:

        self.data = input.split(",")
        print(self.data)

    