#########practice Class

class Myclass:
    x = 5

p1 = Myclass()
print(p1.x)


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def Myfunc(self):
        print("Hello, my name is ", self.name)

class Student(Person):
    def __init__(self,name,age,year):
        super().__init__(name,age)
        self.year = year

    def Myfunc2(self):
        print('name: ',self.name,'age: ',self.age,'year: ',self.year)


P1 = Person("Kalai",34)
P1.age = 33
print(P1.name,P1.age)
###del P1.age        ###deletes the Object's property
P1.Myfunc()

x = Student("Selvin",37,1983)
x.Myfunc2()

import Global
a = Global.Person[1]          ####takes tuple values from the code Global.py
print (a)
print(Global.x)
print(Global.y)

import Global as G
a = G.Person[2]
print(a)

import platform
a = platform.system()
print(a)
x = dir(G)
print(x)

from Global import y
print (G.y)

import datetime
print('datentime: ', datetime.datetime.now())
print('year: ',datetime.datetime.now().year)
print('dayname: ',datetime.datetime.now().strftime("%A"))
print('date', datetime.datetime.now().date())
print('Day :', datetime.datetime.now().day)
print ('time: ', datetime.datetime.now().time())

x = datetime.datetime(2020,11,3)
print(x)
print(x.strftime('%C'))


x = abs(-7.25)
print (x)

x = pow(2,2)
print(x)

import math
x = math.sqrt(81)
print(x)

x = math.ceil(7.2)
print('ceil: ', x)
x = math.floor(7.2)
print('floor :', x)

import json
x = '{"name":"Kalai","Age":"34"}'

#parse x
y = json.loads(x)
print(y["name"])
print(y["Age"])

#convert from dict to JSON

x = {'Name':'Kalai','Age':'34'}
y = json.dumps(x)
print (y)

#convert from list to JSON

x = ['kalai','selvin','shirley']
y = json.dumps(x)
print(y)



print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

print(json.dumps(x,indent=4,separators=(". ","="),sort_keys=True))
