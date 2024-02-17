# List of choices from what to choose
choice_list =["Retrieve devices by oem_id",
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
retrieve_condition = {0: ['oem_id',
                          ['model', 'manufacturer', 'weight_gram', 'price', 'price_currency'],
                          False],
                      1: ['codename',
                          ['brand', 'model', 'ram_capacity', 'market_regions', 'info_added_date'],
                          False],
                      2: ['ram_capacity',
                          ['oem_id', 'released_date', 'announced_date', 'dimensions', 'device_category'],
                          False],
                      3: ['weight_gram',
                          ['weight_gram', 'brand', 'model', 'width', 'height', 'depth', 'price', 'price_currency'],
                          True]}

# Importing csv, menu modules and providing a link to the csv file

csv_file = "device_feature.csv"

if __name__ == "__main__":
    import menu_module as mn
    import retrieve_module as rt
    import analytics_module as an
    #Prompt a pathname
    max_path_attempts = 5
    default_file = "device_features.csv"
    path = mn.input_file_path(default_file,max_path_attempts)
    print("Selected file path:", path)
    #Prompt what exactly to retrieve / analyse/ visualise
    # Constants - boundaries to call a right module
    min_retrieve = 0
    max_retrieve = 3
    min_analytics = 4
    max_analytics = 12
    choice = 0
    while choice != len(choice_list)-1:
        if choice in range(min_retrieve, max_retrieve+1):
            rt.retrieve(path, retrieve_condition[choice])
    print("Bye")
