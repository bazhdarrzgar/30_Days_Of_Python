print('========================== Functions ==========================')
'''
# Syntax


# Declaring a function

def function_name():
    ...code problem
    ...code problem


# Calling a function

function_name()

'''


def generate_full_name():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    # no value will return to the function but when we call the function for there value the compiler look at the function because we have   print()   function this value will be take for printing to the console
    print(full_name)


# calling the function for there value
generate_full_name()
# Asabeneh Yetayeh





def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)


add_two_numbers()
# 5


print('========================== Function Returning a Value - Part 1 ==========================')


def generate_full_name():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    # we just return final result for value of variable (full_name)
    return full_name


# we get the value from the function to show in the console we use   print()  function
print(generate_full_name())






def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    # return value of variable (total)
    return total


# printing this value that we get from function add_two_number():
print(add_two_numbers())


print('========================== Function with Parameters ==========================')

'''
# Syntax


# Declaring a function

def function_name(parameter):
  ...code problem
  ...code problem


# Calling function

print(function_name(argument)
  
'''

def greetings(name):
    message = name + ', welcome to Python for Everyone!'
    # return value of (message) variable
    return message


# taking value to the parameter function
print(greetings('Asabeneh')) # Asabeneh, welcome to Python for Everyonej!





print('\n\n')

def add_ten(num):
    ten = 10
    return num + ten


print(add_ten(90)) # 100




print('\n\n')

def square_number(x):
  
    # final = x * x
    # return final
  
    return x * x


print(square_number(2)) # 4





print('\n\n')

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    
    return area


print(area_of_circle(10)) # 314.0





print('\n\n')

def sum_of_numbers(n):
    
    total = 0

    # we use n+1 because also we need final value to be part of the calculation 
    for i in range(n+1):
        # total = total + i
        total+=i
        
    print(total)


print(sum_of_numbers(10)) 
'''
55
None
'''

print(sum_of_numbers(100)) # 5050
'''
5050
None
'''





# Declaring two or more parameter
'''
# Syntax


  # Declaring a function

  def function_name(para1, para2, ...):
    ...code problem
    ...code problem


  # Calling function

  print(function_name(arg1, arg2, ...))

'''

print('\n\n')

def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name


# print(generate_full_name('Asabeneh', 'yetayeh'))
print('Full Name: ', generate_full_name('Asabeneh','Yetayeh'))
# Full Name:  Asabeneh Yetayeh






print('\n\n')

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum


print('Sum of two numbers: ', sum_two_numbers(1, 9))
# Sum of two numbers:  10






print('\n\n')

def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age;


print('Age: ', calculate_age(2021, 1819))
# Age:  202






print('\n\n')

def weight_of_object (mass, gravity):
    # change integer to string using    str()   function
    # we change the integer result to string after calculation between each other because we use this tring to demage with another string
    weight = str(mass * gravity) + ' N' # the value has to be changed to a string first
    return weight


print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))
# Weight of an object in Newtons:  981.0 N





print('========================== Passing Arguments with Key and Value ==========================')

'''
# Syntax


# Declaring a function

def function_name(para1, para2):
    ...code problem
    ...code problem


# Calling function

print(function_name(para1 = 'John', para2 = 'Doe')) # the order of arguments does not matter here
'''

def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)


# print(print_fullname('Asabeneh', 'Yetayeh'))
'''
Asabeneh Yetayeh
None
'''
# # taking value to the specific parameter for this function that you want by just specify the parameter name and put it this value that you want using equal sign (=)
# print(print_fullname(lastname = 'Asabeneh', firstname = 'Yetayeh'))
'''
Yetayeh Asabeneh
None
'''
# taking value to the specific parameter for this function that you want by just specify the parameter name and put it this value that you want using equal sign (=)
print(print_fullname(firstname = 'Asabeneh', lastname = 'Yetayeh'))
'''
Asabeneh Yetayeh
None
'''




print('\n\n')

def add_two_numbers (num1, num2):
    total = num1 + num2
    print(total)

    
print(add_two_numbers(num2 = 3, num1 = 2)) # Order does not matter
'''
5
None
'''




print('========================== Function Returning a Value - Part 2 ==========================')

def print_name(firstname):
    # returning the value using return keyword
    return firstname


print_name('Asabeneh') # Asabeneh






print('\n\n')

def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    # return the value of variable full_name
    return full_name

    
print(print_full_name(firstname='Asabeneh', lastname='Yetayeh')) # Asabeneh yetayeh






print('\n\n')

def add_two_numbers(num1, num2):
    total = num1 + num2
    return total


print(add_two_numbers(2, 3))# 5






print('\n\n')

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;


print('Age: ', calculate_age(2019, 1819)) # Age: 200






print('\n\n')

def is_even (n):
    if n % 2 == 0:
        print('even')
        # this is means if this value that we give to the function is even then print even and return True for this number that is even
        return True    # return stops further execution of the function, similar to break
    # this is work like else but not quite like this because it is in the same position that if statemet is have if this value that we give to the function is odd then first condition will not return True then false will be return to the function
    # why this is not similer to else ? because if not true or false return by first condition then this condition is return False but if this is inside the else statement then this is not excute then return None for the function
    return False


print(is_even(10)) # True
print(is_even(7)) # False
'''
even
True
False
'''





print('\n\n')

def is_even (n):
    if n % 2 == 0:
        print('even')
        return True    # return stops further execution of the function, similar to break
    return False


# print(is_even(10)) # True
print(is_even(7)) # False
'''
False
'''






print('\n\n')

def is_even (n):
    if n % 2 == 0:
        print('even')
        # # this will not return true or false for this number that is even, because of that this is not true then second condition will be look at and return False for this number
        # return True    # return stops further execution of the function, similar to break
    return False


print(is_even(10)) # False
print(is_even(7)) # False
'''
even
False
False
'''





print('\n\n')

def is_even (n):
    if n % 2 == 0:
        print('even')
        return True    # return stops further execution of the function, similar to break
    # this is the same technique that we use before but with else statement
    else:
        return False


print(is_even(10)) # False
print(is_even(7)) # False
'''
even
True
False
'''





print('\n\n')

def is_even (n):
    if n % 2 == 0:
        print('even')
        # # in this case because we have else statement for second condition then we don't return anything to the function means true or false then return None for this number also with even print to the console
        # return True    # return stops further execution of the function, similar to break
    else:
        return False


print(is_even(10)) # False
print(is_even(7)) # False
'''
even
None
False
'''





print('\n\n')

def find_even_numbers(n):
    # we declared this list outside for loop because we don't need to just get the final value from for loop for the function means the for loop is not store the list each cicle return one value for the function, but when you declare the (evens) variable list outside the for loop then untile the for loop don't end the value of (evens) variable list don't return for the function

    # if you try to declare this variable inside the for loop or inside the if statement you get just  [10]  final value because for loop each cicle is return one number for the function means don't stored value in the list, and the final value will return to the function because funtion just return one value. 
    evens = []
    
    # we use (n + 1) because we need final value in the code problem
    for i in range(n + 1):
        # if value is even then
        if i % 2 == 0:
            # add this value to the list of (evens) varaible
            evens.append(i)
    
    # the value of (even) number will return for the function if pass the condition
    return evens


print(find_even_numbers(10))
# [0, 2, 4, 6, 8, 10]






print('\n\n')

def find_even_numbers(n):
    
    for i in range(n + 1):
        evens = []
        
        if i % 2 == 0:
            # evens = []
            evens.append(i)
    
    return evens


print(find_even_numbers(10))
# [10]






print('\n\n')

def find_even_numbers(n):
    
    for i in range(n + 1):
        # evens = []
        
        if i % 2 == 0:
            evens = []
            evens.append(i)
    
    return evens


print(find_even_numbers(10))
# [10]






print('========================== Function with Default Parameters ==========================')

'''
# Syntax


# Declaring a function

def function_name(param = value):
    ...code problem
    ...code problem


# Calling function

function_name()
# or you can override the value of this parameter
function_name(arg)

'''

# putting this parameter below value by using equal sign ( = )
def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    # returning value of (message) variable
    return message


print(greetings())
# Peter, welcome to Python for Everyone!
print(greetings('Asabeneh'))
# Asabeneh, welcome to Python for Everyone!






print('\n\n')

# taking value to more than one parameter by just using comma ( , ) 
def generate_full_name (first_name = 'Asabeneh', last_name = 'Yetayeh'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name


print(generate_full_name())
# Asabeneh Yetayeh

# you can send value to more than one parameter by just using comma (,) between value
# the value will send to the exactly this parameter that you want depending on the (order) of parameter and this value that you send
print(generate_full_name('David','Smith'))
# David Smith

# send value to the exactly this parameter you want depending of this parameter that you specify for the value
print(generate_full_name(last_name = 'David', first_name = 'Smith'))
# Smith David





print('\n\n')

def calculate_age(birth_year, current_year = 2021):
    age = current_year - birth_year
    # return value of (age) variable
    return age;


# this value will send to the first parameter, and if you use comma after that you can now send value to the second parameter
print('Age: ', calculate_age(1821))
# Age: 200

print('Age: ', calculate_age(1821, 2022))
# Age:  201





print('\n\n')

def weight_of_object (mass, gravity = 9.81):
    # after this calculation between this two parameter the integer value will change to string using   str()   function
    # we do that because we want demage it with another string
    weight = str(mass * gravity)+ ' N' # the value has to be changed to string first
    return weight


print('Weight of an object in Newtons: ', weight_of_object(100)) # Weight of an object in Newtons:  981.0 N
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # Weight of an object in Newtons:  162.0 N






print('========================== Arbitrary Number of Arguments ==========================')

'''
# Syntax


# Declaring a function

def function_name(*args):
    ...code problem
    ...code problem


# Calling function

function_name(param1, param2, param3,..)

'''

# * start before the parameter means how much value send to this function put it to the (nums) parameter like tuple array
def sum_all_nums(*nums):
    
    # return nums # (2, 3, 5)
    
    total = 0
    
    for num in nums:
        total += num     # same as total = total + num
    
    return total


# sending all this value to the (nums) parameter this value will be send like array of tuple to the parameter one by one
# this value will be send like tuple but if you want send it like list or set or tuple you get type error message 
print(sum_all_nums(2, 3, 5)) # 10

# print(sum_all_nums({2, 3, 5})) # TypeError: unsupported operand type(s) for +=: 'int' and 'set'

# print(sum_all_nums([2, 3, 5])) # TypeError: unsupported operand type(s) for +=: 'int' and 'list'

# print(sum_all_nums((2, 3, 5))) # TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'

# print(sum_all_nums((2, 3, 5), (1, 8, 9))) # TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'






print('\n\n')

def generate_groups (team, *args):
    print(team)
    for i in args:
        print(i)
      
        
# first value send to the (team) parameter because this is come first
# second and third and ... value send to the args parameter because we are using start before this parameter 
print(generate_groups('Team-1','Asabeneh','Brook','David','Eyob'))

'''
Team-1
Asabeneh
Brook
David
Eyob
None
'''





# # if we don't use start before (args) parameter then  function for other value don't know where to put them, and error will be happen like this # TypeError: generate_groups() takes 2 positional arguments but 5 were given
# def generate_groups (team,args):
#     print(team)
#     for i in args:
#         print(i)

        
# print(generate_groups('Team-1','Asabeneh','Brook','David','Eyob')) # TypeError: generate_groups() takes 2 positional arguments but 5 were given




print('========================== Function as a Parameter of Another Function ==========================')

'''
# Syntax

def function_1(parameter, ...)
    ...code problem
    return ....


# we just use parameter 1 for specify that i use technique ( function as a parameter of another function) means we don't put value for this parameter

def function_2(parameter_1, parameter, ....)
    ....code problem
    return parameter_1(...., ...., ..)
    

# in this call we put value to the (function_1) and result (function_1) will be the value for the (function_2)
print(function_2(function_1, value, ....))    

'''

# in this technique we use   function 1   to calculate value of (n) and we put this value to the parameter (x) for   function 2   as a value
def square_number(n):
    return n * n # 9

def do_something(f, x):
    return f(x) # 9
    # return f(x * x) # 81
    # return ( f * x * x ) # TypeError: unsupported operand type(s) for *: 'function' and 'int'
    # return f * x * x # TypeError: unsupported operand type(s) for *: 'function' and 'int'


# using first parameter   (f)   in just place the (square_number) to put it value to this function the value will be   (3)   for there parameter
print(do_something(square_number, 3)) # 9






print('\n\n')

# in this technique we use   function 1   to calculate value of (n) and we put this value to the parameter (x) for   function 2   as a value
def square_number(n):
    return n * n # 9

def do_something(f, x):
    return f(x * x) # 9 * 9
    # return f(x) # 9


print(do_something(square_number, 3)) # 81






print('\n\n')

def square_number(n, s):
    return n * n * s # 27

def do_something(f, x, y):
    return f(x * x, y) # 243 
    # 27(x) * 3(x) = 81 
    # 81(x*x)  *  3(y) = 243
    
    # return f(x * x, y * y) # 729
    # # 27(x) * 3(x) = 81 
    # # 81(x*x) * 3(y) = 243 
    # # 243(x*x, y) * 3(y) = 729

    # return (x * x, y * y, x * x) # (9, 9, 9)
    # # x * x = 3 * 3 = 9
    # # y * y = 3 * 3 = 9
    # # x * x = 3 * 3 = 9
    
    # return (x * x, y * y, x * x), y * y # ((9, 9, 9), 9)
    # # x * x = 3 * 3 = 9
    # # y * y = 3 * 3 = 9

    # return (x * x, y * y, x * x, y * y, x * x, y * y), x * x, y * y, x * x # ((9, 9, 9, 9, 9, 9), 9, 9, 9)
    # # x * x = 3 * 3 = 9
    # # y * y = 3 * 3 = 9

    # return (x * x, y * y, y * y), y * y # ((9, 9, 9), 9)
    # # x * x = 3 * 3 = 9
    # # y * y = 3 * 3 = 9

    # return f(x * y) # # TypeError: square_number() missing 1 required positional argument: 's'

print(do_something(square_number, 3, 3)) # 243






print('\n\n')

def square_number(n, s, v):
    return n * n * s * v # 81

def do_something(f, x, y, z):
    return f(x * x, y, z) # 729 
    # 27(x) * 3(x) = 81 
    # 81(x*x)  *  3(y) = 243
    # 243(x*x, y) * 3(z) = 729
    
    # return f(x * x, y * y, z) # 2187
    # # 27(x) * 3(x) = 81 
    # # 81(x*x) * 3(y) = 243 
    # # 243(x*x, y) * 3(y) = 729
    # # 729(x*x, y*y) * 3(z) = 2187

    # return f(x * x, y * y, z * z) # 6561
    # # 27(x) * 3(x) = 81 
    # # 81(x*x) * 3(y) = 243 
    # # 243(x*x, y) * 3(y) = 729
    # # 729(x*x, y*y) * 3(z) = 2187
    # # 2187(x*x, y*y, z) * 3(z) = 6561

    # return f(x * x, y * y, z * z, x * x, y * y, z * z) # TypeError: square_number() takes 3 positional arguments but 6 were given
    


print(do_something(square_number, 3, 3, 3)) # 


