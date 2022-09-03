print('========================== List Comprehension ==========================')

'''
# Syntax

# (target) is this variable or this value or this function that handle the value
# (i) any value that we have in (target) is move to the first (i) and you can do anything in this value by done something to this (i)
# (i) second is get value from (i) first and return this value like list to this place that you want like   print()  function
# if expression is use for filter on this value that loop throw from the for loop or done this operation if my if expression is true

[i for i in target if expression]
'''


# One way
'''
(string) -> change (string to list) -> print(list)
'''

language = 'Python'
lst = list(language) # changing the string to list
print(type(lst))     # list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']



# We do this way because each value go to the first (i) one by one and you can do anything to this value using first (i) like multipliction and divition or change it to something or add soemthing to it or ....
# and also we can use if expression with it if you want filter on this value or done the operation if condition is true
# Second way: list comprehension
'''
[i for i in (string)] => change string to list

(string) -> [i for i in (string)] -> print(list)
'''
lst = [i for i in language]
print(type(lst)) # list
print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']





# Generating numbers
numbers = [i for i in range(11)]  # to generate numbers from 0 to 10
print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# It is possible to do mathematical operations during iteration for (i) first
# squares = [(i * i) for i in range(11)]
squares = [i * i for i in range(11)]
print(squares)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# It is also possible to make a list of tuples
# because we have comma (,) between both (i) first then the compiler understand that you want put both of this value to tuple array inside list
numbers = [(i, i * i) for i in range(11)]
print(numbers)                             # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), ...]







# # Generating even numbers
# even_numbers = [i for i in range(21) if (i % 2 == 0)]  # to generate even numbers list in range 0 to 21
even_numbers = [i for i in range(21) if i % 2 == 0]  # to generate even numbers list in range 0 to 21
print(even_numbers)                    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# # Generating odd numbers
# odd_numbers = [i for i in range(21) if (i % 2 != 0)]  # to generate odd numbers in range 0 to 21
odd_numbers = [i for i in range(21) if i % 2 != 0]  # to generate odd numbers in range 0 to 21
print(odd_numbers)                      # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


positive_even_numbers = [i for i in range(21) if i % 2 == 0 and i > 0]
print(positive_even_numbers)                    # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


# Filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers) # [4, 6, 8, 10]


# Flattening a three-dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [i for i in list_of_lists]
print(flattened_list) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


'''
# change three-dimensional or more dimensional list or tuple or set array to one list array how ?

# we put all the value that come one by one from my target to the (i) first and (i) first put all this value to the second (i) like one or two or three or four or ... dementional like it is in the target array
# this is all done using

i for i in target # don't change the one or two or three or four or ... dimentional array



# but we can change all this in one dimentional list array from (i) second using

for i in i # change two or three or four or ... dimentional array to one dimentional list array



# in the end we have this

[i for i in target for i in i]

'''

flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]





print('========================== Lambda Function ==========================')
'''
# Syntax

## Create lambda
variable_name = lambda parameter1, ... : make_action_to_the_parameter ...
## Calling lambda
print(variable_name(value1, ...))


x = lambda param1, param2, param3, ...: param1 + param2 + param2 + ...
print(x(arg1, arg2, arg3))


# create lambda also putting value to the lambda all this in one line
print(lambda (param1, param2, param3, ...: param1 + param2 + param2 + ...)(arg1, arg2, arg3, ...))


## info
1. lambda not need return keyword the value is return by it self automatically
2. lambda is use for small work all this in one line
3. just send value to the parameter value and value will return for you and you can put it to anywhere you want
'''

def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3))     # 5



# Let's change the above function to a lambda function
add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))    # 5



# create lambda function also putting the value to the lambda
print((lambda a, b: a + b)(2,3)) # 5



square = lambda x : x ** 2
print(square(3))    # 9



cube = lambda x : x ** 3
print(cube(3))    # 27



# # Multiple variables
# multiple_variable = lambda a, b, c: (a ** 2) - (3 * b) + (4 * c)
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3)) # 22





# Lambda Function Inside Another Function

'''
# Syntax

def function_name(parameter_function, ...):
    return lambda parameter_l, ..: parameter_l + parameter_function ... # order is not matter for calculation

function_name(value1_function, value2_l) # order of sending value is matter



## Example
def function_name(x):
    return lambda n : x ** n

# value1 is for (x)
# value2 is for (n) lambda
function_name(value1, value2)

'''

def power(x):
    return lambda n : n ** x

# 2 for x function
# 3 for n lambda function
cube = power(2)(3)
print(cube)          # 9

# 2 for x function
# 5 for n lambda function
two_power_of_five = power(2)(5)
print(two_power_of_five)  # 25



def power(x):
    final = lambda n : n ** x
    return final

cube = power(2)(3)
print(cube)          # 9
