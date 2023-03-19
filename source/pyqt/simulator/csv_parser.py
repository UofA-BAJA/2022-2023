import os
import csv
import struct

class CSVParser:
    '''converts the csv to hex for the pyqt program to eat'''
    def __init__(self) -> None:
        self.csv_as_real_numbers = []

        self.encoded_data = []

    def open_file(self, filepath): 
        full_csv_path = os.path.abspath(os.getcwd()) + r"\source\pyqt\simulator\csvs" + "\\" + filepath
        #print(full_csv_path)
        
        with open(full_csv_path, mode ='r')as file:
   
            # reading the CSV file
            csvFile = csv.reader(file)
            
            header = next(csvFile)

            # displaying the contents of the CSV file
            for lines in csvFile:
                self.csv_as_real_numbers.append(lines)

    def encode_content(self):
        for row in self.csv_as_real_numbers:
            print(struct.pack(">b", row[0]))

    def get_line(self):
        pass
