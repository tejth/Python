import pandas as pd;


#creating series using list
x =[1,2,3,4,5]
var = pd.Series(x,index=["a","b","c","d","e"],dtype="float",name="python")
print(var)
print()
print()

#creating series using dictionary
dic = {"a":[1,2,3,4,5],"b":[7,8,9,10]}
var2 = pd.Series(dic)
print(var2)
print()
print()

# Concatinating series
s1 = pd.Series(12,index=[1,2,3,4,5])
s2=pd.Series(12,index=[1,2,3,4])
print(s1+s2)