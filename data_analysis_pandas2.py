import pandas as pd
# First DataFrame
df1 = pd.DataFrame({'key':['A','B','C'],'value1': [1, 2, 3] })
# Second DataFrame
df2 = pd.DataFrame({'key':['A','B','D'],'value2': [4, 5, 6]  })
# Merge on 'key' column
merged_df = pd.merge(df1, df2, on='key', how='inner')  
# Options: 'inner', 'outer', 'left', 'right'
print("merged_df= ",merged_df)
# Setting indices for both DataFrames
df1.set_index('key', inplace=True)
df2.set_index('key', inplace=True)
# Join on index
joined_df = df1.join(df2, how='outer')  
# Options: 'inner', 'outer', 'left', 'right'
print("joined_df= \n",joined_df)