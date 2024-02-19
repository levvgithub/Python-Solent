# List of choices from what to choose
import csv
import pandas as pd


# df = pd.read_csv('C:/Users/Лев/Documents/GitHub/Python-Solent/device_features.csv')
# df = df[['column_name_1', 'column_name_2', 'column_name_3']]

# def retrieve_element(csv_file, row_index, col_index):
#     print(csv_file)
#     file_data = []
#     with open(csv_file, newline='') as file:
#         reader = csv.reader(file)
#         file_data = list(reader)
        # try:
        #     element1 = file_data[row_index][col_index]
        #     return element1
        # except IndexError:
        #     return None  # Handle index out of range error

file_name = "device_features.csv"
try:
    # Open csv file and read data from a file
    with open(file_name, encoding='UTF-8') as csv_file:
        csvreader = csv.reader(csv_file)
           # read in and store the headings separately
        header = []
        header = next(csvreader)
        OEM_ID_Column = -1
        Model_Name_Column_ID = -1
        Manufacturer_Column_ID = -1
        Weight_Column_ID = -1
        Price_Column_ID = -1
        Price_Currency_Column_ID = -1
        for count, row in enumerate(header):
            # print(count, row)
            if row.strip() == 'oem_id':
                OEM_ID_Column = count
            if row.strip() == 'model':
                Model_Name_Column_ID = count
            if row.strip() == 'manufacturer':
                Manufacturer_Column_ID = count
            if row.strip() == 'weight':
                Weight_Column_ID = count
            if row.strip() == 'price':
                Price_Column_ID = count
            if row.strip() == 'price_currency':
                Price_Currency_Column_ID = count
        dataset = []
        for row in csvreader:
            dataset.append(row)

#         we will find the profession of jack
#  in rows we print column PROFESSION for line/rows where name = JACK
        for row in dataset:
            if row[OEM_ID_Column] == 'A135UZKAUSC':
                print(row[Model_Name_Column_ID])
except IOError:
    print("Cannot read file.")

# # Example usage:
# csv_file = 'device_features.csv'
# row_index = 2  # Index of the row you want to retrieve (0-based index)
# col_index = 1  # Index of the column you want to retrieve (0-based index)

# element = retrieve_element(csv_file, row_index, col_index)
# if element is not None:
#     print(f"Element at row {row_index}, column {col_index}: {element}")
# else:
#     print("Invalid row or column index provided.")

choice_list = ["Retrieve devices by oem_id",
               "Retrieve devices by code name",
               "Retrieve devices by RAM capacity",
               "Retrieve devices by weight range (custom)",
               "Identify the top 5 regions",
               "Analyse the average price of devices",
               "Analyse the average mass for each manufacturer",
               "Count the number of released devices (custom)",
               "Chart for proportion of RAM types",
               "Chart for each USB connector type",
               "The monthly average price trends",
               "The max price, weight and memory for two brands (custom)",
               "Exit the program"]
# The options for retrieving. First key is filter criteria,
# second is a list of fields to show, the third is TRUE for range of values, FALSE for 1 value
# retrieve_condition = {0: ['oem_id',
#                           ['model', 'manufacturer', 'weight_gram', 'price', 'price_currency'],
#                           False],
#                       1: ['codename',
#                           ['brand', 'model', 'ram_capacity', 'market_regions', 'info_added_date'],
#                           False],
#                       2: ['ram_capacity',
#                           ['oem_id', 'released_date', 'announced_date', 'dimensions', 'device_category'],
#                           False],
#                       3: ['weight_gram',
#                           ['weight_gram', 'brand', 'model', 'width', 'height', 'depth', 'price', 'price_currency'],
#                           True]}

# Importing csv, menu modules and providing a link to the csv file

print("Press 1 to retrieve devices by oem_id")
print("Press 2 to retrieve devices by code name")
print("Press 3 to retrieve devices by RAM capacity")
print("Press 4 to retrieve devices by weight range (custom)")
print("Press 5 to identify the top 5 regions")
print("Press 6 to analyse the average price of devices")
print("Press 7 to analyse the average mass for each manufacturer")
print("Press 8 to count the number of released devices (custom)")
print("Press 9 for a chart for proportion of RAM types")
print("Press 10 for a chart for each USB connector type")
print("Press 11 for the monthly average price trends")
print("Press 12 for the max price, weight and memory for two brands (custom)")

def input_value(key):
    value = input(f"Enter {key}:")
    return value
# if __name__ == "__main__":
#     import menu_module as mn
#     import retrieve_module as rt

    # with open('device_features.csv') as device_features:
    #     csv_reader = csv.reader(device_features)
    #     for index, row in enumerate(csv_reader):
    #         if index == 0:
    #             oem_id = row[3]
import keyboard

# press ctrl+shift+z to print "Hotkey Detected"
# keyboard.add_hotkey('1', print, args=oem_id)
#
# keyboard.wait('esc')
