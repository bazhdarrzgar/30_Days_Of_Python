print('========================== Python Error Types ==========================')
'''
# different type error example

1. SyntaxError


    print 'hello world'
          ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?



2. NameError

    print(age)
NameError: name 'age' is not defined



3. IndexError

    numbers[5]
IndexError: list index out of range



4. ModuleNotFoundError

    import maths
ModuleNotFoundError: No module named 'maths'



5. AttributeError

    math.PI
AttributeError: module 'math' has no attribute 'PI'



6. KeyError

    users['county']
KeyError: 'county'



7. TypeError

    4 + '3'
TypeError: unsupported operand type(s) for +: 'int' and 'str'



8. ImportError

    from math import power
ImportError: cannot import name 'power' from 'math' (unknown location)



9. ValueError

    int('12a')
ValueError: invalid literal for int() with base 10: '12a'



10. ZeroDivisionError

    1/0
ZeroDivisionError: division by zero


'''
print('\n\n\n')
print('========================== SyntaxError ==========================')


print 'hello world'
'''
    print 'hello world'
          ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?
'''



print('hello world')

'''
hello world
'''



print('========================== NameError ==========================')

print(age)

'''
    print(age)
NameError: name 'age' is not defined
'''


age = 25

print(age)

'''
25
'''



print('========================== IndexError ==========================')

numbers = [1, 2, 3, 4, 5]

numbers[5]

'''
    numbers[5]
IndexError: list index out of range
'''


print('========================== ModuleNotFoundError ==========================')

import maths

'''
    import maths
ModuleNotFoundError: No module named 'maths'
'''


import math




print('========================== AttributeError ==========================')

import math

math.PI

'''
    math.PI
AttributeError: module 'math' has no attribute 'PI'
'''

math.pi

'''
3.141592653589793
'''


print('========================== KeyError ==========================')

users = {'name':'Asab', 'age':250, 'country':'Finland'}

users['name']
'''
'Asab'
'''


users['county']

'''
    users['county']
KeyError: 'county'
'''


user['country']

'''
'Finland'
'''



print('========================== TypeError ==========================')

4 + '3'

'''
    4 + '3'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''


4 + int('3')

'''
7
'''


4 + float('3')

'''
7.0
'''




print('========================== ImportError ==========================')

from math import power

'''
    from math import power
ImportError: cannot import name 'power' from 'math' (unknown location)
'''


from math import pow

pow(2,3)

'''
8.0
'''





print('========================== ValueError ==========================')

int('12a')

'''
    int('12a')
ValueError: invalid literal for int() with base 10: '12a'
'''




print('========================== ZeroDivisionError ==========================')

1/0

'''
    1/0
ZeroDivisionError: division by zero
'''



