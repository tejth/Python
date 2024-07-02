import pandas as pd

var1 = pd.read_csv(".//user.csv")

#filling null values
var1.fillna("python")
var1.fillna({"username":"python","Identifier":"c"})

#using methods
var1.fillna(method="ffill")

#replacing values
var1.replace(to_replace=1,value=22)
var1.replace([2,3],92)
var1.replace("[A-Za-z]","python",regex=True)
var1.replace({"username":'[A-Z]'},22,regex=True)
var1.replace(1,method="ffill",limit=2,inplace=True)

#using interpolate
var1.interpolate(method="linear",limit_direction="both",limit=2,inplace=True)
