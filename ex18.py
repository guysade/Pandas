def func(a):
    x = a*2
    def func2(a, x):
        return a*x

print(func(2))