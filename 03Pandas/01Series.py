import numpy as np
import pandas as pd


#creating a series
labels = ['a','b','c']
my_list = [10,20,30]
arr = np.array([10,20,30])
d = {'a':10,'b':20,'c':30}
print(pd.Series(data=my_list))
print()
print(pd.Series(data=my_list,index=labels))
print()
print(pd.Series(arr))
print()
print(
pd.Series(arr,labels))
print()
print()

#A pandas Series can hold a variety of object types:
# Even functions (although unlikely that you will use this)
pd.Series([sum,print,len])
print()
print()



#Using Index
ser1 = pd.Series([1,2,3,4],index = ['USA', 'Germany','USSR', 'Japan']);
ser2 = pd.Series([1,2,5,4],index = ['USA', 'Germany','Italy', 'Japan']);
print(ser1)
print(ser2);    
print(ser1['USA'])
print(ser1+ser2)
