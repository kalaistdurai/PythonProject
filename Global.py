#####practice global

def Myfunc ():
    x = 20
    print(x)

def Myfunc5():
    global y
    y = 20
    print (y)

x = 10
Myfunc()
print(x)

y = 10
Myfunc5()
print(y)

Person = ('kalai','selvin','shirley')
