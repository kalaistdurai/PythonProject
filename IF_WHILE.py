#########pracice IF
a = 3
b = 10
if a == b:
    print ("a is equal to b")
elif a > b:
    print ("a is greater than b")
else:
    print ("a is less than b")

i = 1
while i < 6:
    print ("i: ", i)
    if i == 4:
        break
    i += 1

i = 0
while i < 6:
    i += 1
    if i == 4:
        continue
    print("i: ", i)

for x in 'kalai':
    print (x)

mylist = [12,13,14,15,14]
i = 0
for x in mylist:
    if x == 14:
        print(i)
        i += 1
        continue
    i +=1


for x in range(6):
    print(x)

for x in range (1,10,2):
    print(x)

def my_func(food):
    for x in food:
        print (x)

food1 = ["apple","kiwi","pizza"]
print (food1)

my_func(food1)


def tri_recursion(k):
  print ("value of k: ", k)
  if(k > 0):
    print ("k>0")
    result = k + tri_recursion(k - 1)
    print ('value of tri_recursion(k-1): ', tri_recursion(k - 1))
    print('result: ' , result)
  else:
    result = 0
    print ("result in else: ", result)
  return result

print("\n\nRecursion Example Results")
tri_recursion(2)
