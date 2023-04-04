import os
import csv
import struct

class CSVParser:
    '''converts the csv to hex for the pyqt program to eat
    nom nom
    :)
    '''
    def __init__(self) -> None:
        self.csv_as_real_numbers = []

        self.encoded_data = []

        self.line_counter = 0

    def open_file(self, filepath): 
        full_csv_path = os.path.abspath(os.getcwd()) + r"\src\Sensor Dashboard\simulator\csvs" + "\\" + filepath
        #print(full_csv_path)
        
        with open(full_csv_path, mode ='r')as file:
   
            # reading the CSV file
            csvFile = csv.reader(file)
            
            header = next(csvFile)

            # displaying the contents of the CSV file
            for lines in csvFile:
                self.csv_as_real_numbers.append(lines)

    def encode_content(self):
        '''ARDUINO IS LITTLE ENDIAN'''
        for row in self.csv_as_real_numbers:
            emt = []
            emt.append(struct.pack("B", 250))
            emt.append(struct.pack("b", int(row[0])))

            for index in range(1, 8):
                temp = struct.pack("<h", int(row[index]))
                for b in temp: emt.append(bytes([b]))


            for index in range(8,11):
                temp =  struct.pack("<f", float(row[index]))
                #print(temp)
                for b in temp: emt.append(bytes([b]))

            emt.append(struct.pack("B", 251))

            self.encoded_data.append(emt)

    def get_line(self) -> list:
        #print(f"NEW DATALINE IS {self.encoded_data[self.line_counter]}")
        if (self.line_counter > len(self.encoded_data)):
            self.line_counter = 0
        
        temp = self.encoded_data[self.line_counter]

        self.line_counter += 1

        return temp

