import pandas as pd



#Joining
var1 = pd.DataFrame({"A":[1,2,3,4],"B":[11,12,13,14]})
var2 = pd.DataFrame({"C":[10,20,30,40],"D":[11,12,33,44]})

print(var1.join(var2))
print()
print()


var3 = pd.DataFrame({"A":[1,2,3,4],"B":[11,12,13,14]})
var4 = pd.DataFrame({"C":[10,20],"D":[11,22]}, index=["a","b"])

print(var3.join(var4))
print()
print()

#using suffix
var6 = pd.DataFrame({"A":[1,2,3,4],"B":[11,12,13,14]},index=["a","b","c","d"])
var7 = pd.DataFrame({"C":[10,20],"B":[11,12]},index=["a","b"])

var7.join(var6, how="outer",lsuffix="_12",rsuffix="_12")


#GroupBy allows you to access a specific group from a grouped object by its group name. It returns a new DataFrame containing only the rows that belong to the specified group.
var5 = pd.DataFrame({"Name":["a","b","c","d","a","b","a","b","a","c","c","d"],"S_1":[12,13,14,12,13,14,15,23,25,16,10,34],"S_2":[23,24,25,26,27,28,29,30,25,34,35,36]})
var5.groupby("Name")
for x,y in var5:
    print(x)
    print(y)
    
    
var5.get_group("a")




#getting min ,max and median
var5.min()