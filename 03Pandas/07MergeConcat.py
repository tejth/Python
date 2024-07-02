import pandas as pd



#Merging

var1 = pd.DataFrame({"A":[1,2,3,4],"B":[11,12,13,14]})
var2 = pd.DataFrame({"A":[1,2,3,4],"B":[21,22,23,24]})

print(pd.merge(var1,var2,on="A"))
print()
print()


#Left , Right ,Outer, Inner

var3 = pd.DataFrame({"A":[1,2,3,4],"B":[11,12,13,14]})
var4 = pd.DataFrame({"A":[1,2,3,4],"B":[21,22,23,24]})

print(pd.merge(var3,var4,how="left"))
print(pd.merge(var3,var4,how="outer",indicator=True))
print()
print()

#Suffix and indexing
var5 = pd.DataFrame({"A":[1,2,3,4],"B":[11,12,13,14]})
var6 = pd.DataFrame({"A":[1,2,3,4],"B":[21,22,23,24]})

print(pd.merge(var5,var6,left_index=True,right_index=True,suffixes=("name","id")))
print()
print()



#Concatination

sr1 = pd.Series([1,2,3,4])
sr2 = pd.Series([11,21,31,41])

print(pd.concat([sr1,sr2]))
print()
print()


#Using Dictionaries
sr3 = pd.Series({"A":[1,2,3,4],"B":[11,12,13,14]})
sr4 = pd.Series({"A":[1,2,3,5],"B":[21,22,23,24]})
print(pd.concat([sr3,sr4]))
print()
print()


#Along axis
d1 = pd.DataFrame({"A":[1,2,3,4],"B":[11,12,13,14]})
d2 = pd.DataFrame({"A":[1,2,3,5],"B":[21,22,23,24]})

print(pd.concat([d1,d2],axis=1))
print()
print()

#using join
d3 = pd.DataFrame({"A":[1,2,3,4],"B":[11,12,13,14]})
d4 = pd.DataFrame({"A":[1,2,3,5],"B":[21,22,23,24]})

print(pd.concat([d3,d4],axis=1,join="inner"))
print()
print()

#Using keys
d5 = pd.DataFrame({"A":[1,2,3,4],"B":[11,12,13,14]})
d6 = pd.DataFrame({"A":[1,2,3,5],"B":[21,22,23,24]})

print(pd.concat([d5,d6],axis=0,keys=["d5","d6"]))
print()
print()







