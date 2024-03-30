import csv
import pandas as pd

df = pd.read_csv('crypto_data.csv')

btc_filter_df = df[df['Symbol'] == 'BTC-USD']

series = pd.Series(btc_filter_df['Close'].values, index=btc_filter_df['Date'])

print(series)


# def series_func(dataset, header, value_input, value_name, print_names):
#     value_id = pd.Series(value_name)
#     for row in dataset:
#         if value_id['Symbol'] == 'BTC-USD':
#             for name in print_names:
#                 print([pd.Series(name)])
#
#
# if __name__ == "__main__":
#     file_name = "crypto_data.csv"
#     try:
#         df = pd.read_csv(file_name)
#         choice = 0
#         while choice != 13:
#             choice = int(input())
#             if choice == 1:
#                 oem_input = input("Enter oem_id: ")
#                 series_func(dataset, header, oem_input, 'oem_id',
#                       ['model', 'manufacturer', 'weight_gram', 'price', 'price_currency'])
#     except IOError:
#         print("Cannot read file.")


