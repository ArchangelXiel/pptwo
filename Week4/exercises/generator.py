def generator(n):
    for i in range(n+1):
        yield i**2

def squares(a, b):
    for i in range(a, b+1):
        yield i**2

def threefour(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
def decrement(n):
    for i in range(n, -1, -1):
        yield i 

choice=input("Enter your choice (1-4): \n  1. Divisible by 3 and 4\n 2. Squares to b\n 3. Squares from a to b\n 4. Decrement from n to 0\n  ")
if choice == '1':
    x=int(input("Enter a number: "))
    print("Divisible by 3 and 4:")
    for value in threefour(x):
        print(value)
elif choice == '2':    
    x=int(input("Enter a number: "))
    print("Squares to b:")
    for value in generator(x):
        print(value)
elif choice == '3':
    x=int(input("Enter a number a: "))
    y=int(input("Enter a number b: "))
    print("Squares from a to b:")
    for value in squares(x, y):
        print(value)
elif choice == '4':
    x=int(input("Enter a number: "))
    print("Decrement from n to 0:")
    for value in decrement(x):
        print(value)

'''
print("Divisible by 3 and 4:")
for value in threefour(x):
    print(value)

print("Squares to b:")
for value in generator(x):
    print(value)

print("Squares from a to b:")
for value in squares(x, y):
    print(value)

print("Decrement from n to 0:")
for value in decrement(x):
    print(value)    '''