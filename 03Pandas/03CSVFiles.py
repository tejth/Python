import pandas as pd


# Creating and adding data into a CSV File
dis = {"a":[1,2,3,4,5,6] , "s":[1,2,3,4,5,6]}
d = pd.DataFrame(dis)
d.to_csv("Test_new.csv", index=False)


# Setting Header to the CSV File
dis2 = {"a":[1,2,3,4,5],"s":[1,2,3,4,5],"d":[1,2,3,4,5]}
d1 = pd.DataFrame(dis2)
d1.to_csv("Test_new1.csv",index=False,header=["col1","col2","col3"])


#Reading a Csv File
csv_1 = pd.read_csv("Test_new.csv")
print(csv_1)
print()
print()

#Reading Particular Number of Rows 
csv_2 = pd.read_csv("Test_new1.csv", usecols=["col1","col2"])
print(csv_2)
print()
print()

#Skipping number of rows
csv_3 = pd.read_csv("Test_new1.csv", skiprows=[0,1])
print(csv_3)
print()
print()

#Setting particular column as a index
csv_4 = pd.read_csv("Test_new1.csv", index_col="col1")
print(csv_4)
print()
print()

#Changing Header
csv_5 = pd.read_csv("Test_new1.csv", header=2)
print(csv_5)
print()
print()

#Setting column names
csv_6 = pd.read_csv("Test_new1.csv", names=["newcol1","newcol2"])
print(csv_6)
print()
print()


#Setting header to node and using prefix to set header
csv_7 = pd.read_csv("Test_new1.csv", header=None, prefix="col")
print(csv_7)
print()
print()


#Chaging DatType of a Particular column
csv_8 = pd.read_csv("Test_new1.csv", dtype={"col1":"float"})
print(csv_8)
print()
print()
