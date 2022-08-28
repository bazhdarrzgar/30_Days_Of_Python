print('========================== Tuples ==========================')
print('\n\n\n')
print('========================== Creating a Tuple ==========================')

'''
# Empty tuple

# Syntax

variable_name = ()


# or using the tuple constructor

variable_name = tuple()


# Example

variable_name = ('item1', 'item2','item3', ....)

'''


fruits = ('banana', 'orange', 'mango', 'lemon')
print(fruits) # ('banana', 'orange', 'mango', 'lemon')

fruits = tuple(('banana', 'orange', 'mango', 'lemon'))
print(fruits) # ('banana', 'orange', 'mango', 'lemon')




print('========================== Tuple length ==========================')
'''
# Syntax


len(name_variable)

'''

tpl = ('item1', 'item2', 'item3')
print(len(tpl)) # 3




print('========================== Accessing Tuple Items ==========================')
'''
# Syntax

variable_name = (value1, value2, value3, value4)
#                  0        1      2      3
#                 -4       -3     -2      -1

variable_name[0] # value1
variable_name[1] # value2
variable_name[2] # value3
....



variable_name = (value1, value2, value3, value4)

end_length = len(variable_name) # 4

end_index = len(variable_name) - 1 # 3
variable_name[end_index] # value4

'''

tpl = ('item1', 'item2', 'item3')

first_item = tpl[0]
print(first_item) # item1

second_item = tpl[1]
print(second_item) # item2



print('==========================')
fruits = ('banana', 'orange', 'mango', 'lemon')

first_fruit = fruits[0]
print(first_fruit) # banana

second_fruit = fruits[1]
print(second_fruit) # orange

last_index =len(fruits) - 1
last_fruit = fruits[last_index]
print(last_index) # mango



print('==========================')
tpl = ('item1', 'item2', 'item3','item4')

first_item = tpl[-4]
print(first_item) # item1

second_item = tpl[-3]
print(first_item) # item2



print('==========================')
fruits = ('banana', 'orange', 'mango', 'lemon')

first_fruit = fruits[-4]
print(first_fruit) # banana 
second_fruit = fruits[-3]
print(second_fruit) # orange 
last_fruit = fruits[-1]
print(last_fruit) # lemon 




print('========================== Slicing tuples ==========================')
'''
# Syntax

variable_name = (value1, value2, value3, value4)

variable_name[start_index:end_index] # end_index is not in the list

variable_name[start_index:] # if you don't specify the end index then the program will continue for other index in the end it take the program one index more than the total index of the tuple

variable_name[:end_index] # if you don't specify the start index then the program will continue for other index in the end it take the program one index more than the total index of the tuple

'''

tpl = ('item1', 'item2', 'item3','item4')

all_items = tpl[0:4]        
print(all_items) # ('item1', 'item2', 'item3', 'item4')

all_items = tpl[0:]        
print(all_items) # ('item1', 'item2', 'item3', 'item4')

middle_two_items = tpl[1:3]  # does not include item at index 3
print(middle_two_items)      # ('item2', 'item3')



print('==========================')

fruits = ('banana', 'orange', 'mango', 'lemon')

all_fruits = fruits[0:4]    
print(all_fruits) # ('banana', 'orange', 'mango', 'lemon')

all_fruits= fruits[0:]      
print(all_fruits) # ('banana', 'orange', 'mango', 'lemon')

all_fruits= fruits[:4]      
print(all_fruits) # ('banana', 'orange', 'mango', 'lemon')

orange_mango = fruits[1:3]  # doesn't include item at index 3
print(orange_mango) # ('orange', 'mango')

orange_to_the_rest = fruits[1:]
print(orange_to_the_rest) # ('orange', 'mango', 'lemon')



print('==========================')

tpl = ('item1', 'item2', 'item3','item4')
#       -4        -3       -2       -1
#        3         2        1        0

all_items = tpl[-4:]         
print(all_items) # ('item1', 'item2', 'item3', 'item4')

middle_two_items = tpl[-3:-1]  # does not include item at index 3 (-1)
print(middle_two_items) # ('item2', 'item3')



print('==========================')

fruits = ('banana', 'orange', 'mango', 'lemon')
#          -4         -3       -2       -1
#           3          2        1        0

all_fruits = fruits[-4:]    
print(all_fruits) # ('banana', 'orange', 'mango', 'lemon')

orange_mango = fruits[-3:-1]  # doesn't include item at index 3
print(orange_mango) # ('orange', 'mango')

orange_to_the_rest = fruits[-3:]
print(orange_to_the_rest) # ('orange', 'mango', 'lemon')




print('========================== Changing Tuples to Lists ==========================')
'''
# Syntax change tuple to list

variable_name = (value1, value2, value3, value4)

list(variable_name) # [value1, value2, value3, value4]


# Syntax change list to tuple

variable_name = [value1, value2, value3, value4]

tuple(variable_name) # (value1, value2, value3, value4)

'''

tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl) 
print(lst) # ['apple', 'orange', 'mango', 'lemon']


fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits) 
print(fruits) # ['apple', 'orange', 'mango', 'lemon']



print('========================== changing value ==========================')
'''
# Syntax

variable_name = (value1, value2, value3, value4)



# 1. change tuple to list because we can't modify the tuple then we chage tuple to list and modify the list and after that change the list to tuple

variable_list = list(variable_name) # [new_value1, value2, value3, vlaue4]


# 2. chagne the value using index of that value

variable_list[0] = new_value1      


# 3. change list to tuple

variable_tuple = tuple(variable_name) # (new_value1, value2, value3, value4)

'''

tpl = ('item1', 'item2', 'item3','item4')

# tpl[0] = 'apple'    # # error because we can't modifying value in array tuple
# tpl[0] = 'apple' # TypeError: 'tuple' object does not support item assignment


# to change value in tuple

fruits = list(tpl) # first you should chage tuple to list

fruits[0] = 'apple'
print(fruits)     # ['apple', 'item2', 'item3', 'item4']


# after that change list to tuple
tpl = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')




print('========================== Checking an Item in a Tuple ==========================')
'''
# Syntax

in       # if the value is in the list

not in   # if the value is not in the list


variable_name = (value1, value2, value3, value4)

value1 in variable_name      # True or False

value5 not in variable_name  # True or False

'''

tpl = ('item1', 'item2', 'item3','item4')
print('item2' in tpl)    # True


fruits = ('banana', 'orange', 'mango', 'lemon')

print('orange' in fruits) # True

print('apple' in fruits) # False





print('========================== Joining Tuples ==========================')
# we can use plus sign to join list or tuple or set or stirng or number or ....

'''
# Syntax

variable_name1 = (value1, value2, value3, value4)
variable_name2 = (value1, value2, value3, value4)
....



variable_name3 = variable_name1 + variable_name2 + ....

print(variable_name3) # (value1, value2, value3, value4, value1, value2, value3, value4)

'''

tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')

tpl3 = tpl1 + tpl2
print(tpl3) # ('item1', 'item2', 'item3', 'item4', 'item5', 'item6')

# tpl1.extend(tpl2) # AttributeError: 'tuple' object has no attribute 'extend'



fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')

fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables) # ('banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')



print('========================== Deleting Tuples ==========================')
# delete entire array with this variable that define the array 

'''
# Syntax

variable_name = (value1, value2, value3, value4)

del variable_name # we delete the entire array with definer of the array

print(variable_name) # NameError: name 'variable_name' is not defined

'''

tpl1 = ('item1', 'item2', 'item3')
del tpl1

# print(tpl1) # if you try get value of this tuple you get this erro # NameError: name 'tpl1' is not defined



fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits

# print(fruits) # if you try get value of this tuple you get this erro # NameError: name 'tpl1' is not defined



