print('========================== Lists ==========================')
'''
# Syntax

## Creating list
variable_name = list() # list() function can be use to create list or change   tuple   and   set   to list

## tuple to list
variable_name = (value, value, ...)
variable_name.list() # change tuple to list

## set to list
variable_name = {value, value, ...}
variable_name.list() # change set to list
'''

empty_list = list() # empty list
print(len(empty_list)) # 0 # length of the list is 0
print(empty_list) # [] # no value in the list

fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Print the lists and it length
print('Fruits:', fruits) # Fruits: ['banana', 'orange', 'mango', 'lemon']
print('Number of fruits:', len(fruits)) # 4
print('Vegetables:', vegetables) # Vegetables: ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
print('Number of vegetables:', len(vegetables)) # 5
print('Animal products:',animal_products) # Animal products: ['milk', 'meat', 'butter', 'yoghurt']
print('Number of animal products:', len(animal_products)) # 4
print('Web technologies:', web_techs) # Web technologies: ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongDB']
print('Number of web technologies:', len(web_techs)) # 7
print('Countries:', countries) # Countries: ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']
print('Number of countries:', len(countries)) # 5





print('========================== different data type in list ==========================')

lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] 
print(lst) # ['Asabeneh', 250, True, {'country': 'Finland', 'city': 'Helsinki'}]




# print('========================== Accessing items ==========================')
'''
# to access the index we are using this bracket    [index number]
# Syntax

variable_name = [value1, value2, value3, .....]
variable_name[0] # value1
variable_name[1] # value2
variable_name[2] # value3
....


variable_name = [value1, value2, value3, .....]
                   0       1        2     ....
                   
'''

fruits = ['banana', 'orange', 'mango', 'lemon'] 
first_fruit = fruits[0] # we are accessing the first item using index[0]
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit) # lemon
# Last index
last_index = len(fruits) - 1 # length of the list is   4    and    4 - 1 = 3  and   index[3] = lemon     means last iterm
last_fruit = fruits[last_index]


'''
# index in reverse way

variable_name = [value1, value2, value3, value4]
                   -4      -3     -2      -1
                   
'''

fruits = ['banana', 'orange', 'mango', 'lemon'] 
last_fruit = fruits[-1] # here we can say   index[3] = index[-1]
second_last = fruits[-2] # here we can say   index[2] = index[-2]
print(last_fruit)       # lemon
print(second_last)      # mango





print('========================== Slicing items ==========================')
'''
# Syntax

variable_name = [value, value, value, ...]

# start index will be in the list but end index not in the list this is true for positive and negative number

variable_name[start_index:end_index]  



# if you don't have end index then the index is continue more than the end index, say for example 'string' value is containe 5 index then end index in this time is 6 means one value more, this is true for list and tuple and ....

variable_name[start_index:]  


'''

fruits = ['banana', 'orange', 'mango', 'lemon'] 

all_fruits = fruits[0:4] # ['banana', 'orange', 'mango', 'lemon']  # end index is not in the list but in this case we give the index to the [start index:end index] end index, that more that this index that is in the list, then this is how we can return all value in the list
print(all_fruits)


all_fruits = fruits[0:3] # ['banana', 'orange', 'mango'] # end index is not in the list
print(all_fruits)


all_fruits = fruits[0:] # ['banana', 'orange', 'mango', 'lemon'] # if we don't set where to stop it takes all the rest
print(all_fruits) # 


orange_and_mango = fruits[1:3] # it does not include the end index
print(orange_and_mango) # ['orange', 'mango']


orange_mango_lemon = fruits[1:] 
print(orange_mango_lemon) # ['orange', 'mango', 'lemon']


fruits = ['banana', 'orange', 'mango', 'lemon'] 

all_fruits = fruits[-4:] # it returns all the fruits
print(all_fruits) # ['banana', 'orange', 'mango', 'lemon'] # for negative number if you don't specify the end index then this is go from negative number to positive number
# ['banana', 'orange', 'mango', 'lemon']
#    -4        -3        -2        -1
# ----------> ---------------> ------->


orange_and_mango = fruits[-3:-1] # it does not include the end index
print(orange_and_mango) # 'orange', 'mango']


orange_mango_lemon = fruits[-3:]
print(orange_mango_lemon) # ['orange', 'mango', 'lemon'] # for negative number if you don't specify the end index then this is go from negative number to positive number
# ['banana', 'orange', 'mango', 'lemon']
#    -4        -3        -2        -1
# ----------> ---------------> ------->




print('========================== Modifing value using index ==========================')
'''
# Syntax

variable_name = [value1, value2, value3, ...]

variable_name[0] = new_value1
variable_name[1] = new_value2
variable_name[2] = new_value3
....

'''

fruits = ['banana', 'orange', 'mango', 'lemon'] 

fruits[0] = 'Avocado' 
print(fruits)       #  ['Avocado', 'orange', 'mango', 'lemon']


fruits[1] = 'apple'
print(fruits)       #  ['Avocado', 'apple', 'mango', 'lemon']


last_index = len(fruits) - 1 # length of the fruits variable is   4   then   4 - 1 = 3    and   index[3] = 'lemon'   means end index
fruits[last_index] = 'lime'
print(fruits)        #  ['Avocado', 'apple', 'mango', 'lime']



print('========================== for loop with list() ==========================')
# how to find value in the list using    in    keyword or in vice versa using   not in  keyword if we want say if this value is not in this list is true or false
'''
# Syntax

variable_name = [value1, value2, value3, ....]

value1 in variable_name      # True or False
value4 not in variable_name  # True or False


'''

fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True

does_exist = 'lime' in fruits
print(does_exist)  # False




print('========================== Append ==========================')
# append() function will push the value to the list or tuple or set, append() function will add the value to the end of the list or tuple or set ..., means you can't add value to the specific place
'''
# Syntax

variable_name = [value1, value2, value3, ....]

variable_name.append(value4) # [value1, value2, value3, value4, ....]

'''

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')  # pushing apple to the list this is go to the end of the list
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']

fruits.append('lime')   
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime]





print('========================== insert ==========================')
# insert() function will add value to the list or tuple or set ..., but add the value to the specific place

'''
# Syntax

variable_name = [value1, value2, value3, ....]

variable_name.insert(index_number, value4) # what ever index you are want this value go to this place and push this value that is in this place to the next step

'''

fruits = ['banana', 'orange', 'mango', 'lemon']

fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']


fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print(fruits)

# fruits.insert('avacado')   # error # you should specify the index value this is rule for the   insert()   but not for the   append()
# print(fruits)





print('========================== remove ==========================')
# remove()   function will remove value in the list or tuple or ..., in what ever place in this array,  remove()   function will just search in the array and find it and remove it, this is true for removing first matching result but not for second and third and ....
'''
# Syntax


'''

fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon', 'banana']
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango', 'banana']





print('========================== pop() ==========================')
# pop() fucntion will pop value in the array by default will do that in end but you can put any index value you want
fruits = ['banana', 'orange', 'mango', 'lemon']

fruits.pop() # removing end index by default this will be   index[3]   by default
print(fruits)       # ['banana', 'orange', 'mango']


fruits.pop(0) # poping or removing  index[0] = 'banana'  
print(fruits)       # ['orange', 'mango'] 





print('========================== del() ==========================')
# del keyword will delete this vlaue of this index that is in the array
'''
# Syntax

variable_name = [value, value, value, ...]
variable_name = (value, value, value, ...)
variable_name = {value, value, value, ...}

del variable_name[index_number]

'''

fruits = ['banana', 'orange', 'mango', 'lemon']
del fruits[0]     
print(fruits)       # ['orange', 'mango', 'lemon']

del fruits[1]     
print(fruits)       # ['orange', 'lemon']

# del fruits
# print(fruits)       # This should give: NameError: name 'fruits' is not defined

del fruits[1:3]     # this deletes items between given indexes, so it does not delete the item with index 3
print(fruits)       # ['orange', 'lime']



print('========================== clear() ==========================')
# clear() function will delete all the value in the array

fruits = ['banana', 'orange', 'mango', 'lemon']

fruits.clear()     
print(fruits)       # []




print('========================== copy() ==========================')
# copy() function will copying a lits or tuple or set, the copy will be the actuall copy of the array
'''
# Syntax

variable_name = [value, value, value, ....]
variable_name = (value, value, value, ....)
variable_name = {value, value, value, ....}

new_varaible_name = variable_name.copy()

'''

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
 
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']





print('========================== + ==========================')
# you can join anything using plus sign  (+)

negative_numbers = [-5,-4,-3,-2,-1]
zero = [0]
positive_numbers = [1, 2, 3,4,5]

integers = negative_numbers + zero + positive_numbers
print(integers) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]


fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'] 

fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables )





print('========================== extend() ==========================')
# extend() function is join two array with each other 

'''
# Syntax

# this will join    variabel_name_first    with     variable_name_second    but when you want call the this variable that done operation join you should call     variable_name_first 

variable_name_first.extend(variable_name_second)
print(variable_name_first)



variable_name1 = [value, value, value, ...]
variable_name2 = [value, value, value, ...]
variable_name3 = [value, value, value, ...]
....

variable_name1.extend(variable_name2)
print(varaible_name1)

variable_name3.extend(variable_name1)
print(varaible_name3)

'''

num1 = [0, 1, 2, 3]
num2= [4, 5,6]
num1.extend(num2)
print('Numbers:', num1) # Numbers: [0, 1, 2, 3, 4, 5, 6]


negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)


fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'] 
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits )





print('========================== count() ==========================')
# count() function will count this value that you want in the array, the search is done in the entire array
'''
# Syntax

variable_name = [value1, value2, value2, .....]

count(value2)

'''

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1 # finding how much   'orange'   is in the list


ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3 # finding how much number   24   in the list





print('========================== index() ==========================')
# index() function will find index number of value this is true for first matching result, if you want done search in the entire array use regular expression with it

'''
# Syntax

variable_name = [value1, value2, value3, ...]

variable_name.index(value3) # 2

'''

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1


ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24)) # 2




print('========================== reverse() ==========================')
# reverse() function will reverse the order of the array

'''
# Syntax

variable_name = [value1, value2, value3, ...]

variable_name.reverse() # [...., value3, value2, value1]

'''

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)  # ['lemon', 'mango', 'orange', 'banana']


ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages)     # [24, 25, 24, 26, 25, 24, 19, 22]





print('========================== sort() ==========================')
# sort() function will order the array to this way that you want it can be Ascending order or Descending order

'''
# Syntax

variable_name = [value1, value2, value3, ...]

# Ascending order by default
variable_name.sort()



# Descending order by default
variable_name.sort(reverse=True)

'''

fruits = ['banana', 'orange', 'mango', 'lemon']
# Asceding order in order in string is stable like that 
# ( high vlaue come first,  low value come first, low value come last, high value come last )
fruits.sort()
print(fruits) # ['banana', 'lemon', 'mango', 'orange']


# Descending order in order in string is stable, but in reverse way of ascending order like that
# ( high vlaue come last,  low value come last, low value come first, high value come first )
fruits.sort(reverse=True)
print(fruits) # ['orange', 'mango', 'lemon', 'banana']


ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages) # [19, 22, 24, 24, 24, 25, 25, 26]


ages.sort(reverse=True)
print(ages) # [26, 25, 25, 24, 24, 24, 22, 19]




print('========================== Unpacking List Items ==========================')
# * means the rest of the list
lst = ['item','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']

print('============================')


first_item, second_item, third_item, *rest, last_item = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4']
print(last_item)      # ['item5']

print('============================')


*rest, last_item = lst
print(rest)           # ['item', 'item2', 'item3', 'item4']
print(last_item)      # ['item5']

print('============================')


first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10

print('============================')


countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr) # Germany
print(fr) # France
print(bg) # Belgium
print(sw) # Sweden
print(scandic) # ['Denmark', 'Finland', 'Norway', 'Iceland']
print(es) # Estonia

print('============================')


fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first_fruit, second_fruit, third_fruit, *rest = fruits
print(first_fruit)     # banana
print(second_fruit)    # orange
print(third_fruit)     # mango
print(rest)            # ['lemon','lime','apple']




print('========================== Slicing Items from a List ==========================')
fruits = ['banana', 'orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order, means step will be negative, like we loop throw the array from right to left this is how the negative index work

# ['banana', 'orange', 'mango', 'lemon']
#   -4         -3        -2       -1
# <----(-1)<----(-1)<----(-1)<----(-1)

print(reverse_fruits) # ['lemon', 'mango', 'orange', 'banana']


orange_and_lemon = fruits[::2] # 2 step. It will take every 2cnd item 

# ['banana', 'orange', 'mango', 'lemon']
#   0           1         2        3
# <----(0)----->()----->(2)---->()

print(orange_and_lemon) # ['banana', 'mango']



orange_and_lemon = fruits[::3] # 3 step. It will take every 3cnd item 

# ['banana', 'orange', 'mango', 'lemon']
#   0           1         2        3
# <----(0)----->()------>()----->(3)

print(orange_and_lemon) # ['banana', 'lemon']




print('========================== sorted() ==========================')
# sorted(): returns the ordered list without modifying the original list.
'''
# Syntax

variable_name = [value1, value2, value3, ...]
sorted(variable_name) # sort in ascending order


variable_name = [value1, value2, value3, ...]
sorted(variable_name, reverse=True) # reverse the order means descending the order

'''

fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))   # ['banana', 'lemon', 'mango', 'orange']


fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits, reverse=True)
print(fruits)     # ['orange', 'mango', 'lemon', 'banana']
