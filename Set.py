#########practice set
myset = {10,20,30,'kalai','shirley','selvin',10,12,30}
print("myset: ",myset)
if 'kala' in myset:
    print("myset value is present: ", myset)
else:
    print("my set value is not present")

#### cannot change item value in 'set'
#but can add - adds one value ; update - adds more than one value

myset.add('kk')
myset.update(['mm','nn','oo'])

print ("add values: ", myset)

####two ways to delete an item from the set
###remove - throws error if item not found
###discard - doesnt throw error if item not found

myset.remove('kk')
print ("after remove: ", myset)
x = myset.pop()                    ####remove using POP - will remove the last value
print("what valyue is removed: ",x)

myset.discard('kk')            ###didnt throw error eventhough deletd in the remove
print ("after remove: ", myset)

#myset.remove('kk')          ###threw error as 'kk' is not found. kk is deleted in the 1st remove


#####joinn two sets --- UNION, update - both removes duplicates

set1 = {10,11,12}
set2 = set1.union({'kk','ll','mm',10})
print("set2: ", set2)
print("set1: ", set1)

set2.update(set1)
print("ater update set1: ", set1)
print("set2: ", set2)









