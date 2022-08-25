# Arithmetic Operations in Python
# Integers
print('========================== Operators ==========================')
print('\n\n\n')
print('========================== Assignment Operators ==========================')

'''

# Assignment Operators

=     x = 5        x = 5
+=    x += 3       x = x + 3
-=    x -= 3       x = x - 3
*=    x *= 3       x = x * 3
/=    x /= 3       x = x / 3
%=    x %= 3       x = x % 3
//=   x //= 3      x = x // 3
**=   x **= 3      x = x ** 3
&=    x &= 3       x = x & 3
|=    x |= 3       x = x | 3
^=    x ^= 3       x = x ^ 3
>>=   x >>= 3      x = x >> 3
<<=   x <<=        x = x << 3

'''
print('Addition: ', 1 + 2) # 3
print('Subtraction: ', 2 - 1) # 1
print('Subtraction: ', 1 - 2) # -1
print('Multiplication: ', 2 * 3) # 6
print ('Division: ', 4 / 2) # 2.0   # Division in python gives floating number
print('Division: ', 6 / 2) # 3.0    # Division in python gives floating number
print('Division: ', 7 / 2) # 3.5
print('Division without the remainder: ', 7 // 2) # 3   # gives the result without the floating number or without the remaining
print('Modulus: ', 3 % 2) # 1   # Gives the remainder
print ('Division without the remainder: ', 7 // 3) # 2   # gives the result without the floating number or without the remaining
print('Exponential: ', 3 ** 2) # 9    # it means 3 * 3





print('========================== Floating numbers ==========================')

# Floating numbers
print('Floating Number,PI', 3.14)
print('Floating Number, gravity', 9.81)





print('========================== Complex numbers ==========================')

# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex number: ',(1 + 1j) * (1-1j))





print('========================== Declaring the variable and Print the result ==========================')

# Declaring the variable at the top first

a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b # 5
diff = a - b # 1
product = a * b # 6
division = a / b # 1.5
remainder = a % b # 1
floor_division = a // b # 1
exponential = a ** b # 9

# I should have used sum instead of total but sum is a built-in function try to avoid overriding builtin functions
print(total) # if you don't label your print with some string, you never know from where is  the result is coming
print('a + b = ', total) # 5
print('a - b = ', diff) # 1
print('a * b = ', product) # 6
print('a / b = ', division) # 1.5
print('a % b = ', remainder) # 1
print('a // b = ', floor_division) # 1
print('a ** b = ', exponential) # 9

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two # 3 + 4 = 7
diff = num_two - num_one # 4 - 3 = 1
product = num_one * num_two # 3 * 4 = 12
div = num_two / num_two # 4 / 4 = 1.0
remainder = num_two % num_one # 4 % 3 = 1

# Printing values with label
print('total: ', total) # 7
print('difference: ', diff) # 1
print('product: ', product) # 12
print('division: ', div) # 1.0
print('remainder: ', remainder) # 1






print('========================== Calculating area of a circle ==========================')
# rule of finding area of circle: (3.14 * (radius^2))

radius = 10                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # 3.14 * 10^2 = 3.14 * 100 = 314.0
print('Area of a circle:', area_of_circle)  # Area of a circle: 314.0





print('========================== Calculating area of a rectangle ==========================')
# Rule to find area of reactangle: length * width

length = 10
width = 20
area_of_rectangle = length * width # 10 * 20
print('Area of rectangle:', area_of_rectangle) # Area of reactangle: 200





print('========================== Calculating a weight of an object ==========================')
# Rule to find weight of object in earth: mass * gravity

mass = 75
gravity = 9.81
weight = mass * gravity # 75 * 9.81
print(weight, 'N') # 735.75 N





print('========================== Calculate the density of a liquid ==========================')
# Rule to find desity of a liquid: mass / volume
mass = 75 # in Kg
volume = 0.075 # in cubic meter
density = mass / volume # 1000 Kg/m^3




print('========================== Comparison Operators ==========================')

print(3 > 2)     # True, because 3 is greater than 2
# 3 is greater than or equal to 2
print(3 >= 2)    # True, because 3 is greater than 2 but not equal than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
# 3 is less than or equal to 2
print(2 <= 3)    # True, because 2 is less than 3 but not equal than 2
print(3 == 2)    # False, because 3 is not equal to 2 in value but in type yes
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False, because length of 'mango' is not equal to length of 'avocado' but in type yes equal
print(len('mango') != len('avocado'))  # True, because length of 'mango' is not equal to length of 'avocado' 
print(len('mango') < len('avocado'))   # True, because length of 'mango' is less than length of 'avocado' 
print(len('milk') != len('meat'))      # False, because length of 'milk' is no equal to length of meat 
print(len('milk') == len('meat'))      # True, because length of 'milk' is equol to length of 'meat' in type and value(length)
print(len('tomato') == len('potato'))  # True, because length of 'tomato' is equol to length of 'potato' in type and value(length)
print(len('python') > len('dragon'))   # False, because length of 'python' is not greater than length of 'dragon' 


# Comparing something gives either a True or False
print('True == True: ', True == True) # True == True: True # yes in type and value
print('True == False: ', True == False) # True == False: False # no in type and value
print('False == False:', False == False) # False == False: True # yes in type and value




print('========================== Logical Operator ==========================')
'''
# Logical Operator

& 
and
# return True if both statements are true
# Example: x > 5 and x < 10

|
or
# return True if one of the statements is true
# Example: x > 5 and x < 10

not
# Reverse the result, returns False if condition is true
# Example:   not (x > 5 and x < 10)

'''


print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statement is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True - Because not False mean True
print(not not True)  # True - because ( not True is False ) and ( not False is True )
print(not not False) # False - because ( not False is True ) and ( not True is False )
print('True and True: ', True and True) # True and True: True
print('True or False:', True or False) # True or False: True


 
 
 

# this code is run in if not another code is come after that means different type of code that is not have ( is       is not       in       not in )
print('========================== Another way comparison ==========================')

'''
is: Returns true if both variables are the same object(x is y) means x = y
is not: Returns true if both variables are not the same object(x is not y) means x != y
in: Returns True if the queried list contains a certain item(x in y) means if unless one value of x is equal to value in y then true is come
not in: Returns True if the queried list doesn't have a certain item(x in y) means if unless one value of x is equal to value in y then false is come
'''

# True - because the data values are the same
print('1 is 1', 1 is 1)                   
# True - because 1 is not 2
print('1 is not 2', 1 is not 2)           
# True - because 'A' value is in one of the value of 'Asabeneh'
print('A in Asabeneh', 'A' in 'Asabeneh') 
# False - because 'B' value is not in one of the value of 'Asabeneh'
print('B in Asabeneh', 'B' in 'Asabeneh') 
# True - because 'conding' value is in one of the value of 'conding for all' 
print('coding' in 'coding for all') 
# True - because 'a' value is in one of the value of 'an' 
print('a in an:', 'a' in 'an')      
# True - because 4 value is equal to value of   2**2 = 4 
print('4 is 2 ** 2:', 4 is 2 ** 2)  

