def hello(name):
    print('hello ' + name)
hello('guy')

def multiple(n1,n2):
    print(n1 * n2)
multiple(2,3)

def toNumber(number):
    for x in range(number):
        yield x 
generator = toNumber(20)
print(list(generator))