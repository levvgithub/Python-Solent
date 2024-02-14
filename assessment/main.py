# Importing csv, menu modules and providing a link to the csv file

import csv
import menu_module as m
import retrieve_module as r
import analytics_module as a

csv_file = "device_feature.csv"

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
