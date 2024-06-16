import numpy as np
import pandas as pd
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
df.head()

#Info on Unique Values
print(df['col2'].unique())
print(df['col2'].nunique())
print(df['col2'].value_counts())

#Selecting Data
newdf = df[(df['col1']>2) & (df['col2']==444)]
print(newdf)


#Applying function
def times2(x):
    return x*2
print(df['col1'].apply(times2))
print(df['col3'].apply(len))
print(df['col1'].sum())


#Permanently removing Column
del df['col1']
print(df)

#GET Column and Index Name
print(df.columns)
print(df.index)


#Sorting and Ordering DataFrame
df.sort_values(by='col2') #inplace=False by default


#Find Null Values or Check For null Value
print(df.isnull())


#Drop Rows with Nan Values
print(df.dropna())

#Filling in NaN values with something else: 
df = pd.DataFrame({'col1':[1,2,3,np.nan],
                   'col2':[np.nan,555,666,444],
                   'col3':['abc','def','ghi','xyz']})
print(df.head())
df.fillna('FILL')
print(df)

data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)
print(df.pivot_table(values='D',index=['A', 'B'],columns=['C']))
