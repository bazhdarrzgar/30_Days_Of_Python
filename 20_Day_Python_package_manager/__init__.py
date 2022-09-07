# mypackage/__init__.py

'''
# The folder structure of your package should look like this:

─ mypackage
    ├── __init__.py
    ├── arithmetic.py
    └── greet.py

'''

# from folder (mypackage) calling file (arithmetic)
from mypackage import arithmetic

arithmetic.add_numbers(1, 2, 3, 5)
# 11

'''
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print(total)

add_numbers(1, 2, 3, 5) # 11

'''

arithmetic.subtract(5, 3)
# 2

'''
def subtract(a, b):
    print(a - b)

subtract(5, 3) # 2

'''

arithmetic.multiple(5, 3)
# 15

'''
def multiple(a, b):
    print(a * b)

multiple(5, 3)

'''

arithmetic.division(5, 3)
# 1.6666666666666667

'''
def division(a, b):
    print(a / b)

division(5, 3) # 1.6666666666666667

'''

arithmetic.remainder(5, 3)
# 2

'''
def remainder(a, b):
    print(a % b)

remainder(5, 3) # 2

'''

arithmetic.power(5, 3)
# 125

'''
def power(a, b):
    print(a ** b)
    
power(5, 3)

'''






from mypackage import greet

greet.greet_person('Asabeneh', 'Yetayeh') # 'Asabeneh Yetayeh, welcome to 30DaysOfPython Challenge!'

'''
def greet_person(firstname, lastname):
    return f'{firstname} {lastname}, welcome to 30DaysOfPython Challenge!'

print(greet_person('Asabeneh', 'Yetayeh')) # 'Asabeneh Yetayeh, welcome to 30DaysOfPython Challenge!'

'''