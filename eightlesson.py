#Import pandas

import pandas as pd

#Read this csv into a dataframe called purchase_df

purchase_df = pd.read_csv("./Data/Purchase_data.csv", encoding='utf-8')

#Use the head() method to check that you have read in the data correctly.

purchase_df.head()

#convert invoice_time to be datetime data type

purchase_df['invoice_time'] = pd.to_datetime(purchase_df['invoice_time'])

purchase_df

#Compute the average and max price charged. Store the results in variables called avg_price and max_price

avg_price = purchase_df.price.mean()
max_price =purchase_df.price.max()

print(f"Average price: {avg_price:.2f}")
print(f"Maximum price: {max_price:.2f}")

#Compute the average price and average number of items purchased with only a single call to the mean() method. Store these averages in avg_price and avg_num_items.

avgs = purchase_df[["price", "num_item"]].mean()
avg_price = avgs["price"]
avg_num_items = avgs["num_item"]

print(f"Average price: {avg_price:.2f}")
print(f"Avergae number of items: {avg_num_items:.2f}")

#How many different products are there?

list_prods = purchase_df.product_id.unique()
num_prods = len(list_prods)

print(f"There are {num_prods} different products in this supermarket")