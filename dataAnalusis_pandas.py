import pandas as pd
data = {'Name': ['Alice', 'Bob', 'David'],
    'Age': [25, None, 40]}

data2 = {'Name': ['Alice', 'Bob', 'Kara'],
    'Age': [25, 35, 50]}

df = pd.DataFrame(data)
df2 = pd.DataFrame(data2)
# Replace NaN with 0
filled_df = df.fillna(0)
#print (filled_df)
#print (df.sort_values(by='Age'))
new_df=pd.merge(df,df2, on="Name",how="outer")
print(new_df)
#print(df.groupby('Name')['Age'].agg(['sum', 'mean']))
#print(df.sort_values(by=['Name','Age'], ascending=[True,False]))
df.set_index('Name', inplace=True)
df2.set_index('Name', inplace=True)
join_df=df.join(df2,how='outer', lsuffix='_df1', rsuffix='_df2')
print(join_df)