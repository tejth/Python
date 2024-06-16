
import pandas as pd
import numpy as np
from numpy.random import randn
np.random.seed(101)


#Creating a DataFrame
df = pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())
print(df)
print()
print()


#Selection and Indexing
print(df['W'])
df[['W','Z']] #Pass a list of column names
print(df.W)  #Syntac not recommended
print(type(df['W']))
print()
print()

#Creating a new Column
df['new'] = df['W'] + df['Y']
print(df)


#Removing Columns
df.drop('new',axis=1) #No change in ordiginal dataaframe unless inPlace is mentioned
print(df)
 
#Removing Row
df.drop('E',axis=0,inplace="True")
print(df)


#Selecting Rows
print(df.loc['A'])
print(df.loc[['A','B']])
print(df.iloc[2])
print(df.loc['B','Y']) #Selecting subset of rows and columns
print(df.loc[['A','B'],['W','Y']])


#Conditional Selection
print(df>0)
print(df[df>0])
print(df['W']>0)
print(df[df['W']>0])
print(df[df['W']>0]['Y'])
print(df[df['W']>0][['Y','X']])
print(df[(df['W']>0) & (df['Y'] > 1)])


#index Reseting
df.reset_index()   #Reset to default 0,1,..n index
newind = 'CA NY WY OR CO'.split()
df['States'] = newind
print(df)
df.set_index('States') #Mention inPlace to change original dataFrame
print(df)


#MultiIndex and Index Hierarchy


# Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
print(hier_index)
df = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])
print(df)
print(df.loc['G1'])
print(df.loc['G1'].loc[1])
df.index.names = ['Group','Num']
print(df)
print(df.xs('G1'))
print(df.xs(['G1',1]))
print(df.xs(1,level='Num'))



