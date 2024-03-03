# # List of choices from what to choose
# import csv
# def menu_function():
#     print("Press 1 to retrieve devices by oem_id")
#
# def retrieve1(dataset, value_field, value_id, print1_id, print2_id):
#
#             # dataset = []
#             # for row in csvreader:
#             #     dataset.append(row)
#
#             for row in dataset:
#                 if row[value_id] == value_field:
#                     print(row[print1_id], row[print2_id])
#
# if __name__ == "__main__":
#     file_name = "device_features.csv"
#     try:
#         with open(file_name, encoding='UTF-8') as csv_file:
#             csvreader = csv.reader(csv_file)
#             header = []
#             header = next(csvreader)
#             OEM_ID_Column = -1
#             Model_Name_Column_ID = -1
#             Manufacturer_Column_ID = -1
#             Weight_Column_ID = -1
#             Price_Column_ID = -1
#             Price_Currency_Column_ID = -1
#             for count, row in enumerate(header):
#                 # print(count, row)
#                 if row.strip() == 'oem_id':
#                     OEM_ID_Column = count
#                 if row.strip() == 'model':
#                     Model_Name_Column_ID = count
#                 if row.strip() == 'manufacturer':
#                     Manufacturer_Column_ID = count
#                 if row.strip() == 'weight':
#                     Weight_Column_ID = count
#                 if row.strip() == 'price':
#                     Price_Column_ID = count
#                 if row.strip() == 'price_currency':
#                     Price_Currency_Column_ID = count
#         choice = 0
#         while choice != 13:
#             menu_function()
#             choice = int(input())
#             match choice:
#                 case 1:
#                     oem_name = input("Enter oem_id")
#                     retrieve1(csvreader, oem_name, OEM_ID_Column, Model_Name_Column_ID, Manufacturer_Column_ID)
#     except IOError:
#         print("Cannot read file.")
#
#
# # with open('device_features.csv') as device_features:
# #     csv_reader = csv.reader(device_features)
# #     for index, row in enumerate(csv_reader):
# #         if index == 0:
# #             oem_id = row[3]
# import keyboard
#
# # press ctrl+shift+z to print "Hotkey Detected"
# # keyboard.add_hotkey('1', print, args=oem_id)
# #
# # keyboard.wait('esc')
#
# # print("Press 2 to retrieve devices by code name")
# #     print("Press 3 to retrieve devices by RAM capacity")
# #     print("Press 4 to retrieve devices by weight range (custom)")
# #     print("Press 5 to identify the top 5 regions")
# #     print("Press 6 to analyse the average price of devices")
# #     print("Press 7 to analyse the average mass for each manufacturer")
# #     print("Press 8 to count the number of released devices (custom)")
# #     print("Press 9 for a chart for proportion of RAM types")
# #     print("Press 10 for a chart for each USB connector type")
# #     print("Press 11 for the monthly average price trends")
# #     print("Press 12 for the max price, weight and memory for two brands (custom)")

import csv
import pandas as pd

def menu_function():
    print("Press 1 to retrieve devices by oem_id")
    print("Press 2 to retrieve devices by code name")
    print("Press 3 to retrieve devices by RAM capacity")
    print("Press 4 to retrieve devices by model (custom)")
    print("Press 5 to identify the top 5 regions")
    print("Press 6 to analyse the average price of devices")
    print("Press 7 to analyse the average mass for each manufacturer")
    print("Press 8 to analyse the average weight and height of devices (custom)")
    print("Press 13 to exit")

def retrieve1(dataset, header, value_input, value_name, print_names):
    value_id = header.index(value_name)  # Get the index of the value name directly
    for row in dataset:
        if row[value_id] == value_input:
            for name in print_names:
                print(name, ':', row[header.index(name)])
def retrieve_regions(df, brand_name):
    brand_df = df[df['brand'] == brand_name]

    # Split the 'market_regions' column by comma
    split_regions = brand_df['market_regions'].str.split(',')

    # Explode the resulting lists to separate rows
    exploded_regions = split_regions.explode()

    # Count occurrences of each region
    region_counts = exploded_regions.value_counts()

    # Select top 5 regions and return as a list
    top_5_regions = region_counts.head(5).index.tolist()

    return top_5_regions


def average_price_for_brand(df, brand_name):
    # Filter DataFrame for the specified brand
    brand_df = df[df['brand'] == brand_name].copy()

    # Convert price to numeric (assuming it's in string format)
    brand_df['price'] = pd.to_numeric(brand_df['price'])

    # Drop rows with NaN values in price column
    brand_df = brand_df.dropna(subset=['price'])

    # Calculate average price
    average_price = brand_df['price'].mean()

    return average_price


def average_weight_by_manufacturer(df):
    # Group the DataFrame by 'manufacturer'
    grouped_by_manufacturer = df.groupby('manufacturer')

    # Select the 'weight_gram' column from the grouped DataFrame
    weight_column = grouped_by_manufacturer['weight_gram']

    # Calculate the mean of the 'weight_gram' column
    avg_weight_by_manufacturer = weight_column.mean()

    return avg_weight_by_manufacturer


def average_width_height_for_brand(df, brand_name):
    # Filter DataFrame for the specified brand
    brand_df = df[df['brand'] == brand_name].copy()

    # Convert width and height to numeric (assuming they're in string format)
    brand_df.loc[:, 'width'] = pd.to_numeric(brand_df['width'])
    brand_df.loc[:, 'height'] = pd.to_numeric(brand_df['height'])

    # Filter out rows with NaN values in width and height columns
    brand_df = brand_df.dropna(subset=['width', 'height'])

    # Calculate average width and height
    avg_width = brand_df['width'].mean()
    avg_height = brand_df['height'].mean()

    return avg_width, avg_height

if __name__ == "__main__":
    file_name = "device_features.csv"
    try:
        df = pd.read_csv(file_name)

        with open(file_name, encoding='UTF-8') as csv_file:
            csvreader = csv.reader(csv_file)
            dataset = list(csvreader)  # Load the entire CSV data into memory
            header = dataset[0]  # Store header separately
            OEM_ID_Column = header.index('oem_id')
            Model_Name_Column_ID = header.index('model')
            Manufacturer_Column_ID = header.index('manufacturer')
            Weight_Column_ID = header.index('weight_gram')
            Price_Column_ID = header.index('price')
            Price_Currency_Column_ID = header.index('price_currency')
            Brand_Column_ID = header.index('brand')
            RAM_Capacity_Column_ID = header.index('ram_capacity')
            Market_Regions_Column_ID = header.index('market_regions')
            Date_Added_Column_ID = header.index('info_added_date')

        choice = 0
        while choice != 13:
            menu_function()
            choice = int(input())
            if choice == 1:
                oem_input = input("Enter oem_id: ")
                retrieve1(dataset, header, oem_input, 'oem_id',
                          ['model', 'manufacturer', 'weight_gram', 'price', 'price_currency'])
            elif choice == 2:
                code_input = input("Enter code name: ")
                retrieve1(dataset, header, code_input, 'codename',
                          ['brand', 'model', 'ram_capacity', 'market_regions', 'info_added_date'])
            elif choice == 3:
                ram_input = input("Enter code name: ")
                retrieve1(dataset, header, ram_input, 'ram_capacity',
                          ['oem_id', 'release_date', 'announcement_date', 'dimensions', 'device_category'])
            elif choice == 4:
                model_input = input("Enter code name: ")
                retrieve1(dataset, header, model_input, 'model',
                          ['released_date', 'announced_date', 'hardware_designer'])
            elif choice == 5:
                brand_name = input("Enter brand name: ")
                top_regions = retrieve_regions(df, brand_name)
                print("Top 5 regions for brand '{}':".format(brand_name))
                for i, region in enumerate(top_regions, start=1):
                    print(i, region)
            elif choice == 6:
                brand_name = input("Enter brand name: ")
                average_price = average_price_for_brand(df, brand_name)
                print("Average price for devices of brand '{}': ${:.2f}".format(brand_name, average_price))
            elif choice == 7:
                avg_weight_by_manufacturer = average_weight_by_manufacturer(df)
                # Display the list of average weights for all manufacturers
                print("Average weight for each manufacturer:")
                print(avg_weight_by_manufacturer.to_string(index=True, header=False))
            elif choice == 8:
                brand_name = input("Enter brand name: ")
                avg_width, avg_height = average_width_height_for_brand(df, brand_name)
                print("Average width for devices of brand '{}': {:.2f} cm".format(brand_name, avg_width))
                print("Average height for devices of brand '{}': {:.2f} cm".format(brand_name, avg_height))
    except IOError:
        print("Cannot read file.")


        # retrieve1(dataset, oem_name, OEM_ID_Column,
        #           [Model_Name_Column_ID, Manufacturer_Column_ID,
        #            Weight_Column_ID, Price_Column_ID, Price_Currency_Column_ID])



