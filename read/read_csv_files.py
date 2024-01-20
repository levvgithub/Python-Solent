# Import csv library
import csv

# define a file name
file_name = "./songs.csv"

# Open a csv file 
with open(file_name,encoding='UTF-8') as csv_file:
    print(f"{file_name} is now open for read")

try:
    # Open csv file and read data from a file
    with open(file_name, encoding='UTF-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        # read in and store the headings separately
        headings = next(csv_file)
        
        # Display heading in csv file
        print(headings)
        
        # Display a list of values for each line
        for row in csv_reader:
            print(row[0], row[3])
            
except IOError:
    print("Cannot read file.")



