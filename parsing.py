import math as m
import csv
import os

A_ARM_RADIUS = 7.71
#from the drivers perspective
FR = "front_right"
FL = "front_left" 
BR = "back_right"
BL = "back_left"

READ_FILE_PATH = r"C:\Users\alexr\Documents\Baja\imu_raw_data\POOPEE7.TXT"

OUTPUT_FOLDER_PATH = r"C:\Users\alexr\Documents\Baja\imu_processed_data\endurace_first_5m"

TIMEFRAME_INITIAL_MS = 0
TIMEFRAME_FINAL_MS = 250000

column_id = {
    #labels columns in given csv
    1 : FR,
    2 : FL,
    3 : BR,
    4: BL
}

def read_csv_from_file(file_path = ''):

    return_data = []

    with open(file_path, "r", newline='') as f:
        # create the csv writer
        reader = csv.reader(f)

        for index, row in enumerate(reader):

            if index == 0:
                continue

            temp_row_list = []
            for element in row:

                if element != "":

                    if element == row[0]:
                        time = int(element)

                        if (time < TIMEFRAME_INITIAL_MS):
                            continue

                        if (time > TIMEFRAME_FINAL_MS):
                            break

                        temp_row_list.append(int(element))

                    else: temp_row_list.append(float(element))
                    
            if temp_row_list:
                return_data.append(temp_row_list)

        # write a row to the csv file

    return return_data

def split_columns(list = []):
    """
    This function takes a list and splits into seperate colums.
    The columns are represented as a list of lists.
    Each list is a column, and each sublis, represents the column data.
    Args:
        list: list of lists to split apart
    Return Value:
        return_list: list of lists representing the columns
    """

    # iterate through readings
    #initial_data = [float(item) for item in contents[0].split(',') if any(item) and item != '\n']
    print(list[0])
    return_list = []
    for item in list[0]:
        return_list.append([])

    for i in range(len(return_list)):
        for item in list:
            print(item)
            return_list[i].append(item[i])
    
    return return_list

def time_column(column = []):
    new_data = []
   
    initial_data = int(column[0])
    for index in range(len(column) - 1):
        new_data.append((int(column[index]) - initial_data)/1000)
    
    return new_data

def angle_to_displacment(column = []):
    return_list = []
    
    for element in column:
        
        displacment = m.sin(m.radians(element))*A_ARM_RADIUS
        return_list.append(displacment)

    return return_list

def merge_columns(columns = []):
    '''changes list of columns to list of rows'''
    temp_dict = {}

    for col in columns:
        for index, element in enumerate(col):

            if index not in temp_dict:
                temp_dict[index] = []
                
            temp_dict[index].append(element)

    r_list = []
    for data in temp_dict.values():
        
        r_list.append(data)

    
    return r_list

def make_csvs(path = '', columns_list = []):

    for data_columns in range(1, len(columns_list)):

        path = OUTPUT_FOLDER_PATH +  '\\' + column_id[data_columns] + r'.csv'

        time_list = columns_list[0]

        with open(path, "w+", newline='') as f:

            # create the csv writer
            writer = csv.writer(f)

            # write a row to the csv file

            single_csv_data = merge_columns([time_list, columns_list[data_columns]])

            writer.writerows(single_csv_data)
        

if not os.path.isdir(OUTPUT_FOLDER_PATH):
    os.makedirs(OUTPUT_FOLDER_PATH)

contents = read_csv_from_file(READ_FILE_PATH)

columns = split_columns(list = contents)

columns[0] = time_column(columns[0])

formatted_cols = []
formatted_cols.append(columns[0])

for col_index, col in enumerate(columns):
    
    if col_index != 0:
        
        formatted_cols.append(angle_to_displacment(col))

path = r"C:\Users\alexr\Downloads\test.csv"

#print(formatted_cols)

make_csvs(path, formatted_cols)










