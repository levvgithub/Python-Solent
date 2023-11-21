import csv
data_set = []
path = "device_features.csv"
with open(path, newline='') as device_features:
    csv_read = csv.DictReader(device_features)
    data_set = list(csv_read)

# print(data_set)
print(data_set["brand"])

selected_key = 'Apple'

