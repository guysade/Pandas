def howMany(list):
    newlist = [0,0,0,0,0,0,0,0,0,0]
    x = 0
    for x in list:
        newlist[x] = (newlist[x] + 1)
    print(newlist)

print(howMany([5,5,5,5,5,5,7,8,9,9,9]))