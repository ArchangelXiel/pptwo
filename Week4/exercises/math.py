import math
def DegreetoRadians(degrees):
    radians = degrees * (math.pi / 180)
    return radians

def TrapezoidalArea(base1, base2, height):
    area = 0.5 * (base1 + base2) * height
    return area
def PolygonalArea(num_sides, side_length):
    area = (num_sides * (side_length ** 2)) / (4 * math.tan(math.pi / num_sides))
    return area
def ParrallelogramArea(base, height):
    area = base * height
    return area

choice = input("Choose a function to execute: \n1: Degree to Radians \n2: Trapezoidal Area \n3: Polygonal Area \n4: Parallelogram Area\n")
if choice == '1':
    degrees = float(input("Enter degrees: "))
    print("Radians:", DegreetoRadians(degrees))
elif choice == '2':
    base1 = float(input("Enter base 1: "))
    base2 = float(input("Enter base 2: "))
    height = float(input("Enter height: "))
    print("Trapezoidal Area:", TrapezoidalArea(base1, base2, height))
elif choice == '3':
    num_sides = int(input("Enter number of sides: "))
    side_length = float(input("Enter side length: "))
    print("Polygonal Area:", PolygonalArea(num_sides, side_length))
elif choice == '4':
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    print("Parallelogram Area:", ParrallelogramArea(base, height))
