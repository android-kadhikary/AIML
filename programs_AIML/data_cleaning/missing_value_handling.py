import pandas as pd
df= pd.DataFrame(pd.read_csv("../../data/Transformed_Housing_Data.csv"))
# 1. Fill with a Specific Constant Value
# This is often used for categorical data or when you want to assign a default, such as 0 or "Unknown".
# Replace all NaN values in the entire DataFrame with the number 0
df.fillna(0, inplace=True)

# Replace NaNs in a specific column with the string 'Missing'
df['Category'].fillna('Missing', inplace=True)


# 2. Fill with Calculated Statistics
# This is the most common method for numerical data imputation to maintain the column's mean or median distribution.
# Fill NaNs in the 'Age' column with the mean (average) of the existing 'Age' values
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Fill NaNs in the 'Salary' column with the median of the existing 'Salary' values
df['Salary'].fillna(df['Salary'].median(), inplace=True)


# 3. Fill with Adjacent Values (Forward/Backward Fill)
# This is useful for time series or sequential data where the previous or next observation is the best estimate.
# Method          Alias               Description
# method='ffill'  method='pad'        Forward Fill: Replaces a NaN with the last known valid value that came before it.
# method='bfill'  method='backfill'   Backward Fill: Replaces a NaN with the next valid value that comes after it.
# Method,Alias,Description
# method='ffill',method='pad',Forward Fill: Replaces a NaN with the last known valid value that came before it.
# method='bfill',method='backfill',Backward Fill: Replaces a NaN with the next valid value that comes after it.

# 4. Fill with Different Values for Different Columns
# You can pass a dictionary to .fillna() to specify unique replacement values for multiple columns simultaneously.
# Dictionary mapping column name to its replacement value
fill_values = {
    'Age': df['Age'].median(),
    'Category': 'Other',
    'Score': 0
}

df.fillna(fill_values, inplace=True)

# Note on inplace=True: Including inplace=True modifies the DataFrame directly. If you omit it, 
# the method returns a new DataFrame with the filled values,
# and you would need to assign it back to the original variable: df = df.fillna(0).