import pandas as pd

var = pd.read_csv("./user2.csv")
print(var)
print()
print()


#Removing all the null values
var.dropna()
print(var)
print()
print()

#Removing all the null column
var.dropna(axis=1)

#Removing a row ehich has no value or which is empty
var.dropna(axis=0, how='all')

#If there are missing values in this column, the entire row will be dropped.
var.dropna(subset=["Last name"])

#Using thres parameter var.dropna(thresh=1) is a method in Pandas that drops rows (or columns, depending on the axis) from a DataFrame or Series var where the number of non-NA values is less than or equal to the specified threshold, which is 1 in this case.
var.dropna(thresh=1) 

