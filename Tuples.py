##########practive tuples
mytuple = (10,34,15,2)
print ("my tuple: ", mytuple)
print ("2nd value from tuple: ", mytuple[1])       #####specific index

print ("the last value from tuple: ", mytuple[-1])   #######reverse indexing

mytuple = mytuple + (30,12,14)
print ("my tuple: ", mytuple)
print("range of value: ",mytuple[3:8])

print("range from last value: ", mytuple[-4:-1])

########tuple values cant be changed. so converted to list, updated the list
#### and converted back to tuple
tuplelist = list(mytuple)
tuplelist[2] = "kk"
mytuple=tuple(tuplelist)
print("changed tuple value: ", tuplelist)

for x in mytuple:
    print(x)

if 'kk' in mytuple:
    print ("kk found")
else:
    print("kk not found")


newtuple=('kalai')
print("one value in tuple: ", newtuple)
print("type of variable: ",type(newtuple))        ####recognize this as STR

newtuple=('kalai',)
print("one value in tuple: ", newtuple)
print("type of variable: ",type(newtuple))        ####recognize this as tuples
newtuple = mytuple + (10,12)
print("count of 10: ",newtuple.count(10))

#tuples are unchangeable but can be deleted completely

del newtuple
#print("after del: ", newtuple)       ###throws error as the newtuple doesnt exist
