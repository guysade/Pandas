import pandas as pd
pd.set_option('display.max_rows', None)
df = pd.read_csv(r"C:\Users\guy\Documents\Python\pandas\Automobile_data.csv", na_values = "not available")
print("#### this is exercise 7 ####")
print((df.groupby(['company']).mean(['average-mileage']))[['average-mileage']])

print("#### this is exercise 8 ####")
print(df.sort_values(['price']))

print("#### this is exercise 9 ####")
