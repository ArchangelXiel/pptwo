'''x = "Hello"
y = 15

print(bool(x))
print(bool(y))

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

print(bool(0))
'''

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj)) 