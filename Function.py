x = 10 #global variable
print(x)

def func1():
    print('inside func1 - without global keyword')
    x=5
    print(x)
func1()
print(x)

def func2():
    print('inside func2 - with global keyword')
    global x
    x = 100
    print(x)
func2()
print(x)

