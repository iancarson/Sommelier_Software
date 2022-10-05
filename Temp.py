import pandas as pd
import json


#Open the file
f = open("json.json")
#Load Json file
data = json.load(f)
#Move all items that are under a dollar to isle 15
for i in range(len(data)):
    if data["price"] < 1:
        data["Aisle"] = 15

#Sort the element by sales
sort_by_sales = dict(sorted(data.items(),key=lambda item:item["Sales"]))
#Sort the sales by days. Two days means that the value of days is more
sort_by_days = dict(sorted(sort_by_sales.items(),key=lambda item:item["Yesterday"]))
#Sort the days by discount.
sort_by_discount =  dict(sorted(sort_by_sales.items(),key=lambda item:item["Discount"]))
first_sale = sort_by_discount[len(sort_by_discount) - 1]
second_sale = sort_by_discount[len(sort_by_discount) - 2]

#Cashiers-Checkout algorithm
totalCost = 0
cashier_tuples= {}
for i in range(len(data)):
    totalCost += data["Price"]
    #If this is a new key, then insert and set it's quantity to one.
    if cashier_tuples[data["ID"]] == 0:
        cashier_tuples[data["ID"]] = 1
    else:
        cashier_tuples[data["ID"]] +=1
