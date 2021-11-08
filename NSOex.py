import json

x =  '{ "name":"John", "age":"30_r", "city":"New York_re"}'

y = json.loads(x)

print(y.keys())

matches = ["_r", "_re"]


for item in y.keys():
    if any(x in y[item] for x in matches):
        print(y[item])
        y[item] = y[item].split("_")[0]
        y[item] = y[item] + "_x"
        print(y[item])
    
print(y)