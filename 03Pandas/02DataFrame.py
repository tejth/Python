import pandas as pd

#Creating DataFrame using list
x =[1,2,3,4,5]
var1 = pd.DataFrame(x)
print(var1)
print()
print()

#Creating DataFrame using Dictionary
var2= pd.DataFrame({"a":[1,2,3,4],"b":[5,6,7,8]})
print(var2)
print()
var3 = pd.DataFrame({"a":[1,2,3,4],"b":[5,6,7,8]}, columns=["a"])
print(var3)
print()
print()

#Passing parameters
var4 = pd.DataFrame({"a":[1,2,3,4],"b":[5,6,7,8]}, columns=["a","b"],index=["m","n","o","p"])
print(var4)
print()
print()


list1 = [[1,2,3,4],[5,6,7,8]]
var5 = pd.DataFrame(list1)
print(var5)
print()
print()


#Creating dataframe from series
sr={"s":pd.Series([1,2,3,4]),"r":pd.Series([1,2,3,4])}
var6 = pd.DataFrame(sr)
print(var6)
print()
print()


#Arithmetic Operations
var7 = pd.DataFrame({"a":[1,2,3,4],"b":[5,6,7,8]})
var7["c"]= var7["a"]+var7["b"]
print(var7)
print()
var7["new"]=var7["a"]<=20
print(var7)
print()
print()


#Inserting and deleting data
var8 = pd.DataFrame({"a":[1,2,3,4],"b":[5,6,7,8],"d":[9,10,11,12]})
var8.insert(1,"python",var8["a"])
print(var8)
var8["pynew"]=var8["a"][:3]
print(var8)
print()
print()

var8 = var8.pop("b")
del var8["a"]
print(var8)