import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start()) 




txt = "The rain in Spain"
x = re.split("\s", txt)
print(x) 
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x) 