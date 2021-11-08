ls = ['guy','liron','renne']
collection = map(lambda a: list(a).sort(reverse=True),list(ls))
print(list(collection))
print(ls)
