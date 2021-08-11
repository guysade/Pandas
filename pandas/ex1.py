import pandas as pd

df = pd.read_csv(r"C:\Users\guy\Documents\Python\pandas\Automobile_data.csv", na_values = "not available")
print(df)
df = df.loc[df['price'].idxmax()]
print(df['company'], df['price'])