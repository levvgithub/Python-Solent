
def retrieve(path, condition):
    import csv
    import menu_module as menu
    data_set = []
    # Creating a dictionary
    try:
        with open(path, newline='') as device_features:
            csv_read = csv.reader(device_features)
            header = next(csv_read)
            for row in csv_read:
                row_dict = {header[i]: row[i] for i in range(len(header))}
                data_set.append(row_dict)

    except FileNotFoundError:
        print(f"Error: The file {path} was not found.")
    except IOError:
        print(f"Error: IO error occurred while opening {path} ")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")


