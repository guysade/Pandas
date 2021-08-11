import pandas as pd

df = pd.read_csv(r"C:\Users\guy\Documents\Python\pandas\Automobile_data.csv", na_values = "not available")
df = df.loc[df['company'] == 'toyota']
print(df)