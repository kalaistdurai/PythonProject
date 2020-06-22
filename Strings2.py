### string practice cont.
a = 'this is my world'
x='hello, '
b = 'his' in a
print('b: ',b)       #displays true or false

b = 'hello' in a
print('b: ',b)       #displays true or false
if b == False:
        print('x+a: ',x+a)

b = 'hello' not in a
print('b: ',b)       #displays true or false
if b == False:
        print('a: ',a)

a1,a2,a3,a4 = 34,35,36,37
a = a + ' {3} ' + a + ' {1} ' + ' {0} '
a = a.format(a1,a2,a3,a4)
print('a:',a)


a = "this is my \"world\""
print("a:", a)

b = a.index('my')
print ("position of \"my\" in a : ", b)

b=a.find('my')
print ("position of \"my\" in a : ", b)

b=a.find('our')
print ("position of \"my\" in a : ", b)

a = a + a
b=a.find('my')
print("a:", a)

print ("position of \"my\" in a : ", b)
b=a.rfind('my')
print("a:", a)

print ("position of \"my\" in a : ", b)

a='abcdef'
print("zfill a 2 : " ,a.zfill(10))
