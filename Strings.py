###string practice
kalai = " kalai " \
        "selvi "
print(kalai)

#array
print(kalai[6],kalai[0])
b='Kalaiselvi'
print("b: ",b)
#slicing
print("slicing : " , b[3:5])   #5th positoin not included - 2st posiion is space

print ("slicing reverse: " , b[-5:-3])  #-3 position not included- negative indexing

#length
print("length of the string: ", len(kalai))
kalai=kalai.strip()
print("whitespace strip:",kalai)
print("length of the string: ", len(kalai))

print("whitespace strip:",kalai.strip('k'))

print("whitespace strip:",kalai.strip('lvi'))

print("lower case:",kalai.lower())
print("upper case:",kalai.upper())

print ("replace a with o:  ",kalai.replace('a','o'))

print ("split the word: ", kalai.split(" "))