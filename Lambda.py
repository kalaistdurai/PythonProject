#########practive Lambda
x = lambda a : a+10
print(x(5))

x = lambda a,b:a*b
print(x(2,3))


def myfunc(n):
    return lambda a:a*n

mydouble = myfunc(2)
print(mydouble(22))


