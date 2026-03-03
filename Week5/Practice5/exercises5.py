import re

def task1(text):
    pattern = r"ab*"
    for match in re.findall(pattern, text):
        yield match

def task2(text):
    pattern = r"ab{2,3}"
    for match in re.findall(pattern, text):
        yield match

def task3(text):
    pattern = r"[a-z]+_[a-z]+"
    for match in re.findall(pattern, text):
        yield match

def task4(text):
    pattern = r"[A-Z][a-z]+"
    for match in re.findall(pattern, text):
        yield match

def task5(text):
    pattern = r"a.*b"
    for match in re.findall(pattern, text):
        yield match

def task6(text):
    result = re.sub(r"[ ,\.]", ":", text)
    yield result

def task7(text):
    result = re.sub(r"_([a-z])", lambda x: x.group(1).upper(), text)
    yield result

def task8(text):
    parts = re.split(r"(?=[A-Z])", text)
    for part in parts:
        if part != "":
            yield part

def task9(text):
    result = re.sub(r"([A-Z])", r" \1", text).strip()
    yield result

def task10(text):
    result = re.sub(r"([A-Z])", r"_\1", text).lower()
    yield result


choice = input(
"""Enter your choice (1-10):
1. a followed by zero or more b
2. a followed by two to three b
3. lowercase joined with underscore
4. Uppercase followed by lowercase
5. a followed by anything ending in b
6. Replace space/comma/dot with colon
7. snake_case to camelCase
8. Split at uppercase letters
9. Insert spaces before capital letters
10. camelCase to snake_case
"""
)

text = input("Enter text: ")

if choice == '1':
    for value in task1(text):
        print(value)

elif choice == '2':
    for value in task2(text):
        print(value)

elif choice == '3':
    for value in task3(text):
        print(value)

elif choice == '4':
    for value in task4(text):
        print(value)

elif choice == '5':
    for value in task5(text):
        print(value)

elif choice == '6':
    for value in task6(text):
        print(value)

elif choice == '7':
    for value in task7(text):
        print(value)

elif choice == '8':
    for value in task8(text):
        print(value)

elif choice == '9':
    for value in task9(text):
        print(value)

elif choice == '10':
    for value in task10(text):
        print(value)