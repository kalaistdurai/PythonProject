####practice array
mylist = [10,20,40,12,45,67,78]
print(mylist)

print("3nd: ", mylist[2])
print("-2nd: ",mylist[-2])   #-1 refers to the last item

print("range of values: ",mylist[1:4])  #1 index included but 4 index excluded

print ("print till the end: ",mylist[:])

print("negative indexing: ",mylist[-3:])
print("negative indexing: except last ",mylist[-3:-1])

a=0
for x in mylist:
    print("mylist[",a,"]: ",x)
    a = a + 1

print(mylist[:])
a = int(input("enter the item to be found"))
print("entered value a : ",a)
if a in mylist:
    print("item found remove it")
    #mylist.remove(a)                #removes specified value from the
    i = mylist.index(a)
    #del mylist[i]               #removes specified index
    #del mylist                  #deletes the list and list will not exist
    mylist.clear()               #empties the list without deleting it completely
    if len(mylist) == 0:
        print ("mylist is empty")
        #print(mylist[:])
        #print("len of the list: ",len(mylist))
else:
    print("item not found. add it")
    mylist.append(a)                   #to append at the end of the list
    #mylist.insert(2,a)                  #inserts at particular index
    print("list before sort: ",mylist[:])
    mylist.sort()                    #sorts the list
    print("list after sort: ",mylist)
    mylist.reverse()                 #reverses the order of the list
    print("list after reverse: ",mylist)
    print("len of the list: ", len(mylist))
    #thislist = mylist.copy()            #copies the mylist to thislist - using copy method
    thislist=list(mylist)
    print("copied list: ",thislist)


####join lists
namelist = ["kalai","selvin","shirley"]
numlist = [1,2,3]
print ("namelist: ", namelist)
print ("numlist: ", numlist)
newlist=namelist + numlist + mylist
print ("newlist : ", newlist)

newlist.extend(mylist)         #########extends the list
print ("newlist : ", newlist)

newlist=list(("kalai","shirley"))            ###another way to make a new list
print ("newlist : ", newlist)



