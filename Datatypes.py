#####Datatype examples
a = 10
b = 10.10
c = -10
d = -10.5
e = "kalai"
f = 10j
print(type(a) , ',',a)
print(type(b) ,',',b)
print(type(c),',',c)
print(type(d),',',d)
print(type(e),',',e)
print(type(f),',',f)

j = float(a)
k = int(b)
l = complex(a)
print(j,',',type(j))
print(k,',',type(k))
print(l,',',type(l))

import random
print(random.randrange(1,10))


a = int(1.02)
b = float(10)
c = str(2.0)
d = int("80")
e = float(89.89)
print("a = ",a)
print("b = ",b)
print("c = ",c)
if type(d) == int:
    print("d = ",d)
print("e = ",e)

print(type(d))
print(type(c))
