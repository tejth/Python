import numpy as np
import pandas as pd
from sqlalchemy import create_engine


#CSV INPUT
df = pd.read_csv('example')
print(df)
#CSV OUTPUT
df.to_csv('example',index=False)
print(df)

#Excel Input
pd.read_excel('Excel_Sample.xlsx',sheetname='Sheet1')
#Excel Output
df.to_excel('Excel_Sample.xlsx',sheet_name='Sheet1')


#HTML Input
df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
print(df[0])


#SQL
engine = create_engine('sqlite:///:memory:')
df.to_sql('data', engine)
sql_df = pd.read_sql('data',con=engine)
print(sql_df)