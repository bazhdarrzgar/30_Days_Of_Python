print('========================== Exception Handling ==========================')

'''
# Syntax

try:
    ...code problem (Run this code)
    
except:
    ...code problem (Execute this code when there is an exception)
    
else:
    ...code problem (No exception ? run this code)

finally:
    ...code problem (Always run this code)

'''



'''
try:
    ...code problem (in this block if things go well)
except:
    ...code problem (in this block run if things go wrong)

'''

try:
    print(10 + '5') # error
    
except:
    print('Something went wrong') # Something went wrong

 
# # the right way    
try:
    print(10 + int('5'))  # 15

except:
    print('Something went wrong')  


    
    
    
    
    

try:
    name = input('Enter your name:')
    year_born = input('What year you are born:')
    age = 2019 - year_born # error because   input()   function take the value as string
    print(f'You are {name}. And your age is {age}.')

except:
    print('Something went wrong')


# # the right way
try:
    name = input('Enter your name:')
    year_born = input('What year you are born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')

except:
    print('Something went wrong')









# multiple except and using error condition like validation here
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - int(year_born) # (Value Error) if you are try to type value that not integer
    # age = 2019 - year_born # (Type Error) because string can be calculate with integer
    # age = 2019 / int(year_born) # (Zero Division Error) because we are using division and if you type 0 in this case you get ( Zero Division Error )
    print(f'You are {name}. And your age is {age}.')

# if i get (Type Error) i get this message
except TypeError:
    print('Type error occured')

# if i get (Value Error) i get this message
except ValueError:
    print('Value error occured')

# if i get (Zero Division Error) i get this message
except ZeroDivisionError:
    print('zero division error occured')







try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')

except TypeError:
    print('Type error occur')

except ValueError:
    print('Value error occur')

except ZeroDivisionError:
    print('zero division error occur')

# if (except) condition is not true then this (else) condition will be run if (try) is true
else:
    print('I usually run with the try block')

# finally is always run 
finally:
    print('I alway run.')
    
    
    
    
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')

# if there is error (Exception) keyword return basic error and this error is put on (e) variable in the end the (except) catching error print to the console
except Exception as e:
    print(e)


## you should specify the (Exception) as something because (Exception) just specify it self for print() function if you try this, this is why you should put value of (Exception) to something
# except Exception:
#     print(Exception) # <class 'Exception'>

    
    

print('========================== Packing and Unpacking Arguments in Python ==========================')
print('\n\n\n')
print('========================== Unpacking ==========================')

## Unpacking list

def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
# you can send all this value in one place using just one variable for multiple parameter
# you should use multiple variable to send this value to the parameter in the funciton in right place depending on the index position that they have in function
print(sum_of_five_nums(lst)) # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'




def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
# with start (*) flag expression compiler understand that you are using array to send each value of list to the right parameter depending of the index of the value and parameter for transaction
# but remember this is right if your value and the parameter is have the same number means in this case 5 value for 5 parameter but you can't send 6 or 4 value to 5 parameter or vice versa
print(sum_of_five_nums(*lst))  # 15




def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5, 6]
print(sum_of_five_nums(*lst))  # TypeError: sum_of_five_nums() takes 5 positional arguments but 6 were given




def sum_of_five_nums(a, b, c, d, e, f):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # TypeError: sum_of_five_nums() missing 1 required positional argument: 'f'





numbers = range(2, 7)  # normal call with separate arguments
# change all this (range) of value to (list)
print(list(numbers)) # [2, 3, 4, 5, 6]


args = [2, 7]
# putting all the value of list (args) to this range using start (*) flag
# remember you can't use more than 3 value for parameter   range()   function because   range()   function parameter represented as (start_index, end_index, step)
numbers = range(*args)
print(numbers)       # range(2, 7)
print(list(numbers)) # [2, 3, 4, 5, 6]





countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
'''
fin = Finland
sw  = Sweden
nor = Norway
*rest = ['Denmark', 'Iceland']
'''
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']


numbers = [1, 2, 3, 4, 5, 6, 7]
'''
one = 1
*middle = [2 3 4 5 6]
last = 7
'''
one, *middle, last = numbers
print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7





## Unpacking Dictionaries 

def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'

dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
# if you want send value of dictinary to function using start (*) then you sould use two start (*) because first start just send key and second is value
# we want value in this case to send to the function then we use two start (**)
# remember (this is work for function that have multiple parameter)
print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.


print(*dct)    # name country city age
# print(**dct) # TypeError: 'name' is an invalid keyword argument for print()

# # you can use any trick you want but for my case i don't get to the result to use start (*) to get back value of dictionary
print(*{*dct}) # name country city age
print(*[*dct]) # name country city age
print(*{**dct}) # name country city age





print('========================== Packing ==========================')

# Packing Lists

# any value send to this function will store on the parameter (args)
def sum_all(*args):
    s = 0
    # for each
    for i in args:
        s += i
    return s

# this value is send like value one by one not like list or tuple or set or dictionary
print(sum_all(1, 2, 3))             # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28

# # try  to send value like list or tuple or set 
# print(sum_all([1, 2, 3]))         # 6 # TypeError: unsupported operand type(s) for +=: 'int' and 'list'

# all_list = [1, 2, 3]
# print(sum_all(all_list)) # TypeError: unsupported operand type(s) for +=: 'int' and 'list'

# print(sum_all({1, 2, 3}))         # 6 # TypeError: unsupported operand type(s) for +=: 'int' and 'set'

# print(sum_all((1, 2, 3)))         # 6 # TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'





# Packing Dictionaries

'''
# Note: if you are using double start (**) inside function then each start means different thing but if you send the value from calling function to function it self the it is just mean the value
    # first start means key
    # second start means value

# this is matter because when you want call the key you just type this parameter that handle this two value and the key will be return not value
# but if you are using for loop the you are sending the key of value not value it self from parameter to the variable for loop,
# then now we understand that we just send the key of the parameter to variable for loop
# now you can call the value of key using this bracket [] that inside this bracket you put the key of value in this case the handler of that is (key) variable 
# now just put this variable inside this bracket [] and this will be the key and the value is the parameter but parameter is return key if we call it but when you use this bracket [] this is understand that you want call the value of the key
'''

def packing_person_info(**kwargs):
    # putting the key of the value (kwargs) parameter to (key) variable using for each the sending will be one by one
    for key in kwargs:
        # print key of value one by one just by calling    (key)    variable
        # also printing the value of this key using the (key) variable that handle the key and like index we can call the value of that key for my parameter (kwarge) liek this   kwargs[key]
        print(f"{key} = {kwargs[key]}")
    return kwargs


# creating dictionary and send it to the function
print(packing_person_info(name="Asabeneh", country="Finland", city="Helsinki", age=250))
'''
name = Asabeneh
country = Finland
city = Helsinki
age = 250
{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
'''




print('========================== Spreading in Python ==========================')

lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]


print(*lst_two) # 4 5 6 7
print(*lst_one) # 1 2 3

one, *two = lst_one
print(one, two) # 1 [2, 3]

one, *two, three = lst_two
print(one, two, three) # 4 [5, 6] 7


# we just put the value of this two list to this two variable using start (*) flag

# remember if you put the value of one list to different variable you get different result this means
    # if the one variable handle all the value then the list it self don't get back
    # if more than one variable handle this value then
        # if the variable handle one value of the list then the list it self don't get back
        # if the variable handle more than one value using start (*) in this case then the list will back with this value
lst = [0, *lst_one, *lst_two]
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]




country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']

# puting the value of this two list to separate variable using start (*)
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']





print('========================== Enumerate ==========================')

'''
# enumerate()   function use for return the index of the value and value it self
    # first one is return the index of the value
    # second one is return the value it-self

# enumerate()   function mostly use in for loop
'''

for index, item in enumerate([20, 30, 40]):
    print(index, item)
    '''
    0 20
    1 30
    2 40
    '''



# # without   enumerate()   function
# for index, i in [20, 30, 40]:   # TypeError: cannot unpack non-iterable int object
#     print(index, i)



for index in [20, 30, 40], [0, 1, 2]:
    print(index)
    '''
    [20, 30, 40]
    [0, 1, 2]
    '''



countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']

for index, i in enumerate(countries):
    print(f'The country {i} has been found at index {index}')
    '''
    The country Finland has been found at index 0
    The country Sweden has been found at index 1
    The country Norway has been found at index 2
    The country Denmark has been found at index 3
    The country Iceland has been found at index 4
    '''



countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']

for index, i in enumerate(countries):
    # this time we just work on value ('Norway') for this if condition
    if i == 'Norway':
        print(f'The country {i} has been found at index {index}')
        '''
        The country Norway has been found at index 2
        '''





print('========================== Zip ==========================')

'''
# zip()   function will send the value or value of list or .... to exactly this parameter that you want depending of the index position of the value and parameter

# zip()   funciton mostly use in for loop

# zip()   function is very helpful if you have problem with matching index calling with list or tuple or ... they don't return the error of array that out of range list or tuple or... just don't return there value to the console and that is it
'''

# one value is out of range but the   zip()   function will manage that by just don't calling it
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime', 'avacado']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []

# we put the list (fruits) to parameter (f)
# and we put the list (vegetables) to parameter (v)
for f, v in zip(fruits, vegetables):
    # sending this value that we get from both of the parameter (f, v) to list (fruits_and_veges) using function   ( append() )
    # the transaction is done one by one

    # we also put each of this value that we get any time from (f, v) parameter to dictionary and all this done inside list (fruits_and_veges)
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)
'''
[{'fruit': 'banana', 'veg': 'Tomato'}, {'fruit': 'orange', 'veg': 'Potato'}, {'fruit': 'mango', 'veg': 'Cabbage'}, {'fruit': 'lemon', 'veg': 'Onion'}, {'fruit': 'lime', 'veg': 'Carrot'}]
'''



import pprint
pprint.pprint(fruits_and_veges)

'''
[{'fruit': 'banana', 'veg': 'Tomato'},
 {'fruit': 'orange', 'veg': 'Potato'},
 {'fruit': 'mango', 'veg': 'Cabbage'},
 {'fruit': 'lemon', 'veg': 'Onion'},
 {'fruit': 'lime', 'veg': 'Carrot'}]
'''


