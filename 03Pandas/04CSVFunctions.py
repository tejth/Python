import pandas as pd;


csv_1 = pd.read_csv(".//user.csv")
print(csv_1)
print()
print()


#Getting information about start and stop indexes
print(csv_1.index)
print()

#Getting columns names
print(csv_1.columns)
print()

#Gives overall description of data
print(csv_1.describe)
print()

#Print first n rows
print(csv_1.head(2))
print()
print()


#Print last n rows
print(csv_1.tail(2))
print()
print()


#Using slice operation to get data
print(csv_1[:2])
print()
print()


#Converting csv to numpy
csv_1 = csv_1.to_numpy()
print(csv_1)
print()
print()

#Sorting data
print(csv_1.sort_index(axis=0,ascending=False))
print()
print()


#Chaging data
csv_1.loc[0,"Username"]="newUser"
print(csv_1)
print()
print()


#Getting particular data
print(csv_1.loc[[2,3],["Username","Identifier"]])
print(csv_1.iloc[0,1])
print()
print()



#Dropping COLUMN
csv_1.drop(0, axis=0)


# replace missing values (NaN) in the var2 Series or DataFrame with the value 12.
var2 = pd.read_csv("./Test_new1.csv")
var2.fillna(12,inplace=True)

#Replace first two values
var2.fillna("python",limit=2)