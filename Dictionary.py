#########practice dictionary
mydict = {
    'Fname' : 'Kalai',
    'Lname' : 'Durai',
    'Age' : 34
}
print("My Dictionary: ",mydict)


#####both the methods work same

#age = mydict['Age']
age = mydict.get('Age')
print("age from dict: ", age)

mydict['Age'] = 33
age = mydict.get('Age')
print("age from dict: ", age)

print("prints Keys values from Dictionary")
for x in mydict:
    print(x)                ##prints Key Values

print("\nprints all values from Dictionary")
for a in mydict:
    print(mydict[a])

print("both keys and values: ")
for a,b in mydict.items():
    print(a,':',b)

if 'Fname' in mydict:
    print ("yes, Fname is present")
    print ("value: ", mydict.get('Fname'))
    print("len of the dictionary: ",len(mydict))

mydict['Year'] = 1986
print("after the year is added: ", mydict)

mydict.pop('Age')
print("after Age is popped: ", mydict)

mydict.popitem()                            ####removes the last item added. in this case its year
print("after last item is popped: ", mydict)

mydictcopy = mydict.copy()
print("copied file : ", mydictcopy)

mydictcopy = dict(mydict)
print("copied file : ", mydictcopy)
