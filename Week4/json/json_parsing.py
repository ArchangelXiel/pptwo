import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["name"]) 



json.dumps(x, indent=4)
json.dumps(x, indent=4, separators=(". ", " = "))
json.dumps(x, indent=4, sort_keys=True)