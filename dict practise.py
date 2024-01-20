# import csv
# data_set = []
# path = "device_features.csv"
# with open(path, newline='') as device_features:
#     csv_read = csv.DictReader(device_features)
#     data_set = list(csv_read)

# print(data_set)

# selected_key = 'brand'

# # Create a new dictionary based on the selected key
# new_dict_devices = {selected_key: csv_read[selected_key]}

# # Print the new dictionary
# print(new_dict_devices)

# import csv

# # Specify the CSV file path
# csv_file_path = 'device_features.csv'

# # Specify the key you want to use
# selected_key = 'brand'

# # Create an empty dictionary
# data_dict = {}

# # Read the CSV file and create a dictionary
# with open(csv_file_path, 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for row in csv_reader:
#         key = row[selected_key]
#         data_dict[key] = row

# # Print items based on the specified key
# for key, value in data_dict.items():
#     print(f"{selected_key}: {key}, Data: {value}")




import csv

# Specify the CSV file path
csv_file_path = 'device_features.csv'

# Specify the key you want to use
selected_key = 'brand'

# Specify the value you're interested in
selected_value = 'Apple'  # Change this to the name you're interested in

# Read the CSV file and create a dictionary
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    apple_list = []
    for row in csv_reader:
        key = row[selected_key]
        if key == selected_value:
            # Print data for the specified key and value
            # print(f"{selected_key}: {key}, Data: {row}")
            apple_list.append(row)

    # print(apple_list['brand'])
    for row in apple_list:
        # key = row[selected_key]
        # if key == selected_value:
        #     print(f"{selected_key}: {key}, Data: {}")
        some_row = row[0]
        print(some_row)




