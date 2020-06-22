############practice iterator

mystr = 'kalaiselvi'
myit = iter(mystr)
for x in mystr:
    print(next(myit))

mytuple = ('kalai','selvin','shirley')
myit = iter(mytuple)

for x in mytuple:
    print(next(myit))

#####class example for iteration

class Numseq:
    def __iter__(self):
        self.a = 1
        self.b = 2
        return self

    def __next__(self):
        x = self.a
        y = self.b
        self.a +=1
        return x,y

myclass = Numseq()
myiter = iter(myclass)

print (next(myiter))
print (next(myiter))
print (next(myiter))