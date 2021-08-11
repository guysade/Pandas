import pandas as pd
pd.set_option('display.max_rows', None)

GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}

df1 = pd.DataFrame(GermanCars)
df2 = pd.DataFrame(japaneseCars)
print(df1)
print(df2)


print('#### This is exercise 10 ####')
Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}
df3 = pd.DataFrame(Car_Price, columns=['company', 'price'])
df4 = pd.DataFrame(car_Horsepower,columns=['company', 'horsepower'])
df3['horsepower'] = car_Horsepower['horsepower']
print(df3)