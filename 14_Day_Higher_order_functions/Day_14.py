print('========================== Higher Order Functions ==========================')

'''
# Function perform the following operations:

* A function can take one or more functions as parameters
* A function can be returned as a result of another function
* A function can be modified
* A function can be assigned to a variable

'''


print('========================== Function as a Parameter ==========================')

'''
# Syntax

def function1(parameter1, parameter2, ....):
    return ...

def function2(parameter1, parameter2, ....):
    # this is how you should return value if you are using other function to make change of value of parameter this function here
    return parameter1(parameter2, ...)

# this value is for (function1) after calculation to this value from function1 the value of function1 return to parameter2 and parameter3 .... function2
# parameter1 is just for specify that i take this value to function1 means just for make position to function1
# how much parameter you have in function1 you should have one parameter more than the function1 in function2
function2(function1, value1, value2, ...)



## Example

def function1(parameter1):
    return sum(parameter1)

def function2(parameter1, parameter2):
    return parameter1(parameter2)

function2(function1, [1, 2, 3, 4, 5]) # 15
'''

def sum_numbers(nums):  # normal function
    return sum(nums)    # 15

def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation
    # return f(lst)

result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15





def sum_numbers(nums, nums1):  # normal function
    return nums * nums1    # 25

def higher_order_function(f, lst, lst1):  # function as a parameter
    summation = f(lst, lst1) # 25

    # summation = f(lst, lst1 * lst1) # 125 # 5 * 25 = 125
    # summation = f(lst * lst, lst1) # 125 #  25 * 5 = 125
    # summation = f(lst * lst, lst1) # 125 #  25 * 5 = 125
    # summation = f(lst * lst * lst, lst1 * lst1) # 625 # 125 * 5 = 625 # 625 * 5 = 3125
    # summation = f(lst * lst * lst, lst1 * lst1 * lst1) # 625 # 125 * 5 = 625 # 625 * 25 = 15625

    # summation = f(lst * lst, lst1 * lst1, lst) # error # no more than 2 parameter in the list

    return summation
    # return f(lst, lst1)

result = higher_order_function(sum_numbers, 5, 5)
print(result)       # 25





def sum_numbers(nums, nums1):  # normal function
    return nums * nums1    

def higher_order_function(f, lst, lst1):  # function as a parameter
    summation = f(lst, lst1)
    return summation
    # return f(lst)

result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5], 5)
print(result)       

# [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]





print('========================== Function as a Return Value ==========================')

def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        # returning (square) value
        # in this place because we don't specify anything in this function that name is (square) then the return keyword understand that you want return value of something that is outside the function and this function is just for calling this value
        return square
    elif type == 'cube':
        # returning (cube) value
        return cube
    elif type == 'absolute':
        # returning (absolute) value
        return absolute


# result = higher_order_function('square')(3)
# print(result)       # 9

result = higher_order_function('square')
print(result(3))       # 9
'''
result = higher_order_function('cube') => now this will just return (square)
result = square
result(3) = square(3) # now this will send this value for this (square) function and (square) response this call by sending it value
'''


# result = higher_order_function('cube')(3)
# print(result)        # 27

result = higher_order_function('cube')
print(result(3))       # 27
'''
result = higher_order_function('cube') => now this will just return (cube)
result = cube
result(3) = cube(3) # now this will send this value for this (cube) function and (cube) response this call by sending it value
'''


# result = higher_order_function('absolute')(-3)
# print(result)          # 3

result = higher_order_function('absolute')
print(result(-3))      # 3
'''
result = higher_order_function('absolute') => now this will just return (absolute)
result = absolute
result(3) = absolute(3) # now this will send this value for this (absolute) function and (absolute) response this call by sending it value
'''




print('========================== Python Closures ==========================')

def add_ten():
    ten = 10

    def add(num):
        return num + ten
    # return value of (add) function because this is function value and not variable value then this is go to the mom function because there is not anything that to make something to this return value or do something with it before sending to the mom function
    return add

closure_result = add_ten()
print(closure_result(5))   # 15
print(closure_result(10))  # 20
'''
closure_result = add_ten()

print(closure_result(5))   # 15
closure_result = add_ten()(5)

print(closure_result(10))  # 20
closure_result = add_ten()(10)
'''

# first value is for add_ten() function is basicly nothing
# second value is for add() function we don't specify the name because just by calling the add_ten() functiuon and specify the value of first function that inside the (add_ten) function the calling technique understand what you are want to do
print(add_ten()(5))   # error
print(add_ten()(10))  # error




# # Note: if you plan to use more than one function you should be a ware that function just return 1 value not more than 1 value
# # sending value for more than two function inside mom function is like that
# function_name(function_mom_value)(value_function1)(value_function2)(....)




print('========================== Python Decorators ==========================')

'''
# Syntax

def function1():
    return value1

def function2(parameter):
    def function3():
        # this value will return for function3 and function3 should be return it self for mom function
        return parameter().upper()
        return parameter().lower()

    return function3

# first value is for function2
# second value is for function1
print(function2(function1)())


# to access parameter of mom function inside another function that inside mom funciton you should use
parameter() # means this bracket   ()   in the end of the parameter
'''

def greeting():
    return 'Welcome to Python'

def uppercase_decorator(function):
    def wrapper():
        # this is just normal variable that handle value of   function()   parameter
        func = function()

        make_uppercase = func.upper()
        return make_uppercase
        # return func.upper()
        '''
        func = function()
        func.upper() = function().upper()
        '''

    return wrapper

# g = uppercase_decorator(greeting)
# print(g())          # WELCOME TO PYTHON
print(uppercase_decorator(greeting)())




def greeting():
    return 'Welcome to Python'

def uppercase_decorator(function):
    def wrapper():
        return function().upper()

    return wrapper

# g = uppercase_decorator(greeting)
# print(g())          # WELCOME TO PYTHON
print(uppercase_decorator(greeting)())





def greeting():
    return 'Welcome to Python'

def uppercase_decorator(function):
    return function().upper

# g = uppercase_decorator(greeting)
# print(g())          # WELCOME TO PYTHON
print(uppercase_decorator(greeting)())





# # Let us implement the example above with a decorator
'''
# Syntax

def function2(parameter):
    def function3():
        return parameter().upper()
        return parameter().lower()

    return function3

@function2
def function1():
    return value

print(function1())




# this will send the value of next function that come after @ to this function that we taked the name to @ 
@function_name2
def function_name1():
    ....
 
 
# when you want call the result that you get from this two function you should use function1 that you use for sending value using @function_name2
print(funciton_name1())

'''

def uppercase_decorator(function):
    def wrapper():
        return function().upper()

    return wrapper

# the value of (greeting) function will return to the (uppercase_decorator) function using (@uppercase_decorator) we should write this before this function that you want return there value for (uppercase_decorator) function
@uppercase_decorator
def greeting():
    return 'Welcome to Python'

# in the end just call this function that you use for sending value to other funciton in this case is (greeting) function
print(greeting())   # WELCOME TO PYTHON




print('========================== Applying Multiple Decorators to a Single Function ==========================')

'''
# Syntax

def function2(parameter):
    def function2_1():
        return parameter().upper()

    return function2_1



def function3(parameter)
    def function3_1():
        return parameter().split()

    return function3_1


# first Decorator will change the splite the value
# second Decorator will change the prameter to upper case means (list can convert to upper case) but (upper case and convert to splite)

# not matter what name parameter and function name you have in both of the function the Decorator will send this value that change from first function to second and ....
# this is means that Decorator use for transaction between value from function first to second and ... to get the final change
@function3
@function2   # order with decorators is important in this case - .upper() function does not work with lists
def function1():
    return value

# this function that use for sending value to other function or in this case what function is come after @function_name is this function that we should call
print(function1())

'''

# First Decorator
def uppercase_decorator(function):
    def wrapper():
        return function().upper()

    return wrapper


# Second decorator
def split_string_decorator(function):
    def wrapper():
        return function().split()

    return wrapper

@split_string_decorator
@uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'

print(greeting())   # ['WELCOME', 'TO', 'PYTHON']






print('========================== Accepting Parameters in Decorator Functions ==========================')

'''
# Syntax

# this parameter is handle this three vlaue that we take to function1 by sprater it using sub parameter you use this value
# sub parameter for super parameter: parameter(sub para, sub para, sub para)
def function2(parameter):
    def function2_1(parameter1, parameter2, parameter3):
        # this is use for calling (function1) # important
        function(parameter1, parameter2, parameter3)
        # we just using 3 parameter here if you wnat you can use first and second also
        print("I live in {}".format(parameter3))

    return function2_1

# Decorator function2 because i send value from function1 to function2
@function2
# we have 3 parameter and i use first and second parameter but third parameter i use in function2
# all value of this three parameter will also send to function2
def function1(parameter1, parameter2, parameter3):
    print("I am {} {}. I love to teach.".format(
        parameter1, parameter2))

# we call function1 and we taked value because function1 come after Decorator function2 and we said if we have function after Decorator function and not Decorator this will be call and use for sending vlaue
function1(value, value, value)

'''

def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        # this is use for calling function (print_full_name) 
        function(para1, para2, para3)
        print("I live in {}".format(para3))
        
    return wrapper_accepting_parameters


@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(first_name, last_name))


print_full_name("Asabeneh", "Yetayeh", 'Finland')
'''
I am Asabeneh Yetayeh. I love to teach.
I live in Finland
'''




print('========================== Built-in Higher Order Functions ==========================')

'''
# Syntax
  
map(function, iterable)
'''


# Example: 1

numbers = [1, 2, 3, 4, 5] # iterable

def square(x):            # function
    return x ** 2
# 1 ** 2 = 1
# 2 ** 2 = 4
# 3 ** 2 = 9
# 4 ** 2 = 16
# 5 ** 2 = 25

# first value is operation function that i use for make operation on this value that i take from second value
# second value is use for done operation on

# map function is use for map value to something in this case i map one by one this value from list to the parameter (x) in function (square)
numbers_squared = map(square, numbers)
# we should change this value that i get from map function to list because this value that i get from function map this is non readable data
print(list(numbers_squared))    # [1, 4, 9, 16, 25]



# Lets apply it with a lambda function

# map each value of variable (numbers) list array to the parameter (x) of my lambda function
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]




# Example:2

numbers_str = ['1', '2', '3', '4', '5']  # iterable

# the operation in this case is (int) function is not need this bracket () if you put inside other function in this case is (map) function
# (int) function will change the value to integer
numbers_int = map(int, numbers_str)
print(list(numbers_int))    # [1, 2, 3, 4, 5]




# Example:3

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable

def change_to_upper(name):
    return name.upper()

# put all this value from variable (names) list array to the parameter (name) in function (change_to_upper) one by one to make change on this value
names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']



# Let us apply it with a lambda function
# putting all the value of variable (names) list array to (name) parameter of function (lambda) to make change on this value
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']




print('========================== Python - Filter Function ==========================')

'''
# Syntax

filter(function, iterable)
'''

# Example: 1

# Lets filter only even numbers
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):          # function
    if num % 2 == 0:
        return True
    return False


# first value is for specify the operation in this case is my function (is_even)
# second value is value it self

# Note: the value is send to the operation function to make filter throw the value

# filter is function use for filtering throw the value by specify the (operation function) and the (value) that you want done operation on
even_numbers = filter(is_even, numbers)
# this value that you get is (non readable object that filter throw on the value using filter function)
# to make readable convert it to the list
print(list(even_numbers))       # [2, 4]
# print(even_numbers)           # <filter object at 0x7fd1b20267c0>




# Example: 2

numbers = [1, 2, 3, 4, 5]  # iterable

def is_odd(num):           # function
    if num % 2 != 0:
        return True
    return False


# first is operation function
# second is value that send to the operation function and we filter throw all the value
odd_numbers = filter(is_odd, numbers)
# this value that you get is (non readable object that filter throw on the value using filter function)
# to make readable convert it to the list
print(list(odd_numbers))       # [1, 3, 5]



# Example: 3

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable

def is_name_long(name):                              # function
    if len(name) > 7:
        return True
    return False

long_names = filter(is_name_long, names)
print(list(long_names))         # ['Asabeneh']




print('========================== Python - Reduce Function ==========================')

from functools import reduce

numbers_str = ['1', '2', '3', '4', '5']  # iterable

def add_two_nums(x, y):
    return int(x) + int(y)

# 1 + 2 = 3
# 3 + 4 = 7
# 5 + 0 = 5

# 3 + 7 = 10
# 5 + 0 = 5

# 10 + 5 = 15


# first value is just for specify the operation in this case is my function (add_two_nums)
# second value is this value that i want to done the operation on
total = reduce(add_two_nums, numbers_str)
# total = add_two_nums(numbers_str)       # TypeError: add_two_nums() missing 1 required positional argument: 'y'
print(total)






# initializing list
lis = [1, 3, 5, 6, 2, ]

# using reduce to compute sum of list
print(reduce(lambda a, b: a + b, lis))

# using reduce to compute maximum element from list
print(reduce(lambda a, b: a if a > b else b, lis))
