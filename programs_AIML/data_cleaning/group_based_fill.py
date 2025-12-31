# Fills NaN in 'Price' with the mean price calculated for each 'Category'
df['Price'] = df.groupby('Category')['Price'].transform(
    lambda x: x.fillna(x.mean())
)