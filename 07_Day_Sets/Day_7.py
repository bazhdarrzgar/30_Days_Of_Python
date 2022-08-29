from turtle import update


print('========================== Sets ==========================')
print('\n\n\n')
print('========================== Creating Set ==========================')

'''
# Syntax

st = {}

# or 

st = set()

'''

st = {'item1', 'item2', 'item3', 'item4'}
print(st) # {'item1', 'item3', 'item2', 'item4'}

fruits = {'banana', 'orange', 'mango', 'lemon'}
print(fruits) # {'banana', 'orange', 'mango', 'lemon'}

number = {1, 2, 3, 4 }
print(number) # {1, 2, 3, 4 }



print('========================== Getting set Length ==========================')
# len() function use to return the length of array in this case is set array

st = {'item1', 'item2', 'item3', 'item4'}
print(len(st)) # 4

number = {1, 2, 3, 4 }
print(len(number)) # 4



print('========================== Accessing Items in a Set ==========================')
'''
# Syntax

in        # means if value is in the set

value in variable_name        # True or False



not in    # means if value is not in the set

value not in variable_name    # True or False

'''

st = {'item1', 'item2', 'item3', 'item4'}
print("Does set st contain item3 ? ", 'item3' in st) # Does set st contain item3 ? True

fruits = {'banana', 'orange', 'mango', 'lemon'}
print('Does mongo is in the list ? ', 'mango' in fruits ) # Does mongo is in the list ?  True




print('========================== Adding Items to a Set ==========================')
# add() function will add the value to the set in this case, but just one value can be add and the value can be in the list or tuple
# the add() function will not add the duplicate value to the set

# st = {'item1', 'item2', 'item3', 'item4'}
# st.add('item5', 'item6')
# print(st) # you can just add one item no more than one item # TypeError: set.add() takes exactly one argument (2 given)


fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
print(fruits) # {'orange', 'mango', 'banana', 'lemon', 'lime'}


number = {1, 2, 3, 4}
number.add(5)
print(number) # {1, 2, 3, 4, 5}


# adding duplicate value to the set but add() function not add it
number.add(5)
print(number) # {1, 2, 3, 4, 5}


# adding number from the list to the set
number_list = [1, 2, 3, 4, 5, 6]
number.add(number_list[5])
print(number) # {1, 2, 3, 4, 5}


# adding number from the tuple to the set
number_list = (1, 2, 3, 4, 5, 6, 7)
number.add(number_list[6])
print(number) # {1, 2, 3, 4, 5}


# adding one tuple to the set 
number.add((8, 9, 10, 11, 12))
number.add((14, 19))
print(number) # {1, 2, 3, 4, 5, 6, 7, (8, 9, 10, 11, 12), (14, 19)}


# # you can't add tuple to the set using   add()   function
# number.add({8, 9, 10, 11, 12})
# print(number) # TypeError: unhashable type: 'set'


# # # you can't add list to the set using   add()   function
# number.add([13, 14, 15, 16, 17])
# print(number) # TypeError: unhashable type: 'list'




print('========================== Uptdate Items in Set ==========================')
# update() function will add item to the set but can add more than one value, and the value can be in the list or tuple when you want add it to the set
# the update() function will not add the duplicate vlaue to the set
# if you you add list or tuple or set to the set then the   update()   function will change all this to the normal value and add it to the set
# if you plane using update() function to add value then the value should be inside the set or list or tuple if you want add it to the set


st = {'item1', 'item2', 'item3', 'item4'}

st.update(['item5','item6','item7'])
print(st) # {'item2', 'item1', 'item6', 'item3', 'item7', 'item5', 'item4'}


# adding duplicate value but update() function will not allow
st.update(['item5','item6','item7'])
print(st) # {'item2', 'item1', 'item6', 'item3', 'item7', 'item5', 'item4'}



fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')

fruits.update(vegetables)
print(fruits) # {'cabbage', 'onion', 'mango', 'tomato', 'carrot', 'potato', 'orange', 'lemon', 'banana'}


number = {1, 2, 3, 4}
number.update({5, 6, 7, 8}, {9, 10, 11, 12})
print(number) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}




print('========================== Removing Items from a Set ==========================')
# remove() function will remove any vlaue in the set in this case, the remove() function accept one vlaue to remove it in the set no more than one, by default not remove any value return error if you don't put any argument on it, also if remove() function does not find the vlaue return error


st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2') 
print(st) # {'item1', 'item3', 'item4'}


# st = {'item1', 'item2', 'item3', 'item4'}
# st.remove('item2', 'item3') # TypeError: set.remove() takes exactly one argument (2 given)


# st = {'item1', 'item2', 'item3', 'item4'}
# st.remove('item10') # error because it is not find the value


# st = {'item1', 'item2', 'item3', 'item4'}
# st.remove()
# print(st) # TypeError: set.remove() takes exactly one argument (0 given)



print('========================== Poping Items from a Set ==========================')
# pop() function will remove value in the end of the set, because set array is not indexing then pop() function can't remove item in the set using index of the value in the set 
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop() 
print(removed_item) # orange



# fruits = {'banana', 'orange', 'mango', 'lemon'}
# removed_item = fruits.pop(0) # TypeError: set.pop() takes no arguments (1 given)



print('========================== Clearing Items in a Set ==========================')
# clean() function will clean all the value in the set means just remove the value not the set it self

st = {'item1', 'item2', 'item3', 'item4'}
st.clear()
print(st) # set()


fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()




print('========================== Deleting a Set ==========================')
# del keyword will delete entire set means the value and the set it self 

st = {'item1', 'item2', 'item3', 'item4'}
del st
# print(st) # NameError: name 'st' is not defined


fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits 
# print(fruits) # NameError: name 'fruits' is not defined





print('========================== Converting List to Set ==========================')
# set() function will changing value or list or tuple to the set

lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  
print(st) # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered


fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) 
print(fruits) # {'mango', 'lemon', 'banana', 'orange'}


# set is allow tuple in there array
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana', ('value1', 'value2', 'value3')]
fruits = set(fruits)
print(fruits) # {('value1', 'value2', 'value3'), 'lemon', 'orange', 'mango', 'banana'}


# # set is not allow another set in there array 
# fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana', ('value1', 'value2', 'value3'), {'value1', 'value2', 'value3'}]
# fruits = set(fruits)
# print(fruits) # TypeError: unhashable type: 'set'


# # set is not allow list in there array
# fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana', ('value1', 'value2', 'value3'), ['value4', 'value5', 'value6']]
# fruits = set(fruits)
# print(fruits) # TypeError: unhashable type: 'list'



print('========================== Joining Sets ==========================')
# union() function will join to two array with each other and return the join 
'''
# Syntax

variable_name1 = {value1, value2, value3}
variable_name2 = {value4, value5, value6}


variable_name3 = variable_name1.union(variable_name2)

print(variable_name3) # {value1, value2, value3, value4, value5, value6}


print(variable_name1) # {value1, value2, value3}

print(variable_name2) # {value4, value5, value6}

'''

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
print(st3) # {'item1', 'item8', 'item3', 'item5', 'item7', 'item6', 'item4', 'item2'}
print(st1) # {'item1', 'item2', 'item4', 'item3'}
print(st2) # {'item5', 'item8', 'item6', 'item7'}



fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'cabbage', 'orange', 'carrot', 'potato', 'tomato', 'lemon', 'banana', 'mango', 'onion'}

print(fruits) # {'banana', 'orange', 'mango', 'lemon'} 
print(vegetables) # {'tomato', 'potato', 'cabbage','onion', 'carrot'}



# # union() can't join two different array with each other like tuple and sets
# fruits = ('banana', 'orange', 'mango', 'lemon')
# vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
# print(fruits.union(vegetables)) # AttributeError: 'tuple' object has no attribute 'union'


# # union() can't join two different array with each other like list and sets
# fruits = ['banana', 'orange', 'mango', 'lemon']
# vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
# print(fruits.union(vegetables)) # AttributeError: 'list' object has no attribute 'union'



fruits = {'banana', 'orange', 'mango', 'lemon', ('value1', 'value2', 'value3')}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'banana', 'potato', 'cabbage', 'lemon', 'mango', 'carrot', 'tomato', 'onion', 'orange', ('value1', 'value2', 'value3')}





print('========================== Update item in the set ==========================')
# update() function will add value to the set it can add more than one value and the value should be inside the tuple or set or list to be add to the set.

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # {'tomato', 'cabbage', 'potato', 'lemon', 'mango', 'onion', 'carrot', 'banana', 'orange'}


fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}


number = {1, 2, 3, 4}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
number.update(vegetables)
print(number) # {1, 2, 3, 4, 'onion', 'carrot', 'potato', 'tomato', 'cabbage'}





print('========================== Finding Intersection Items ==========================')
# intersection() function will find similarity between two array

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st3 = st1.intersection(st2) # {'item3', 'item2'}
print(st3)


st1 = {'item1', 'item2', 1, 2}
st2 = {'item3', 'item2', 1}
st3 = st1.intersection(st2) # {1, 'item2'}
print(st3)


whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.intersection(even_numbers)) # {0, 2, 4, 6, 8, 10}


python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.intersection(dragon))     # {'o', 'n'}




print('========================== Checking Subset and Super Set ==========================')

'''
# A set can be a subset or super set of other sets:

# super set: the set of super set is more than sub set
# sub set: the set of sub set is less than super set
# the number of set of super set and sub set is not equal

# remember to apply this you should have simlarity between a set of sub set and super set else False return in any case

* Subset:     issubset()
* Super set:  issuperset()

'''

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}

print(st2.issubset(st1)) # True

print(st1.issubset(st2)) # False

print(st1.issuperset(st2)) # True

print(st2.issuperset(st1)) # False


whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.issubset(even_numbers)) # False, because it is a super set
print(whole_numbers.issuperset(even_numbers)) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.issubset(dragon))     # False



st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item6', 'item5'}

print(st2.issubset(st1)) # False # because there is no similarity between super set and sub set

print(st1.issuperset(st2)) # False # because there is no similarity between super set and sub set

print(st1.issubset(st2)) # False # because there is no similarity between super set and sub set

print(st2.issuperset(st1)) # False # because there is no similarity between super set and sub set




print('========================== Checking the Difference Between Two Sets ==========================')
# difference() function will return this value that difference between target array in this case is  ( set() )  

'''
# Syntax

target_set = (value1, value2, value3)
comparison_set = (value1, value2, valu6)

target_set.difference(coparison_set) # value3

comparison_set.difference(target_set) # value6

'''

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.difference(st1)) # set()  # because value of   (st2)   is not different from   (st1)
print(st1.difference(st2)) # {'item1', 'item4'}  # because value of   (st1)   is different in ('item1', 'item4') from value of   (st2)



whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}

print(whole_numbers.difference(even_numbers)) # {1, 3, 5, 7, 9}



python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}

print(python.difference(dragon))     # {'p', 'y', 't'}  unordered (characteristic of sets)
print(dragon.difference(python))     # {'d', 'r', 'a', 'g'}




print('========================== Finding Symmetric Difference Between Two Sets ==========================')
# symmetric_difference() finding difference between two array but in this time for comparison array also for target array is work
# the symmetric_difference() is not vice versa of difference function but in any of the case this function is work

'''
# Syntax

target_set = (value1, value2, value3)
comparison_set = (value1, value2, valu6)

target_set.symmetric_difference(coparison_set) # value3, value6

comparison_set.symmetric_difference(target_set) # value3, value6

'''

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}

print(st2.symmetric_difference(st1)) # {'item1', 'item4'}



st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}

print(st1.symmetric_difference(st2)) # {'item1', 'item4'}



whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}

print(whole_numbers.symmetric_difference(some_numbers)) # {0, 6, 7, 8, 9, 10}



whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}

print(some_numbers.symmetric_difference(whole_numbers)) # {0, 6, 7, 8, 9, 10}



python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}

print(python.symmetric_difference(dragon))  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}



python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}

print(dragon.symmetric_difference(python))  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}



print('========================== isdisjoin() ==========================')
# isdisjoin() function will check if this two function has similarity of true then return false if not return True, the returning True or False is not for first array or second is just for anyone but not this two.

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.isdisjoint(st1)) # False
print(st1) # {'item1', 'item2', 'item3', 'item4'}
print(st2) # {'item2', 'item3'}


even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers.isdisjoint(odd_numbers)) # True, because no common item
print(even_numbers) # {0, 2, 4 ,6, 8}
print(odd_numbers)  # {1, 3, 5, 7, 9}


python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.isdisjoint(dragon))  # False, there are common items {'o', 'n'}
print(python) # {'p', 'y', 't', 'h', 'o','n'}
print(dragon) # {'d', 'r', 'a', 'g', 'o','n'}



