# Returns a file name and path
def input_file_path(default_path, max_path_attempts):
    # default_path - file name by default
    # max_path_attempts - max number of attempts to find the file
    import os.path
    file_found = False
    path = ""
    i = 1
    while i <= max_path_attempts and file_found == False:
        path = input(f"Please provide the path to the CSV file ({default_path} by default):")
        # If path is empty we use current folder and file "device_features.csv"
        if path == "":
            path = default_path
        if os.path.isfile(path):
            print(f"File is found: {path} ")
            file_found = True
        else:
            print(f"There is no file: {path}. You have {max_path_attempts - i} attempts")
            i += 1
    return path