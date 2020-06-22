########practice Regx

import re

txt = "The rain 123 The rain in Spain"
x = re.search("^The.*Spain$",txt)
print(x)
x = re.findall("Spain",txt)
print(x)
x = re.sub("The","the",txt)
print(x)
x = re.split(" ",txt)
print(x)

x=re.search("\d",txt)        ####if digits are present in string
print(x)

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())

x = re.search(r"\bS\w+", txt)
print(x.span())

