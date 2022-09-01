print('========================== Loops ==========================')
print('\n\n')
print('========================== While loop ==========================')
# while loop: look at condition if true then loop throw the code problem untile the condition is match my target

'''
# Syntax

while condition:
    ...code problem

'''

count = 0

while count < 5:
    print(count)
    count = count + 1
    # count += 1

# result: ( 0 1 2 3 4 )


print('========================== While with else ==========================')
# while with else: you can use while with else like you do with if statement, this is for more intract with different statement in python

'''
# Syntax

while condition:
    ...code problem
    
else:
    ...code problem
    
'''

print('\n\n')


count = 0

while count > 5:
    print(count)
    count = count + 1
    # count += 1

else:
    print(count)

# result: 0


print('========================== Break ==========================')
# Break: break is use with if statement for breaking in certain condition

'''

# syntax
while condition:
    code goes here
    if another_condition:
        break

'''

count = 0

while count < 5:
    print(count)
    count = count + 1
    # count += 1
    # when the loop get in 3 number this condition will be true
    if count == 3:
        # the code problem is for breaking in 3 number loop will be stop
        break

# result: ( 0 1 2 )


print('========================== Continue ==========================')
# Continue: continue is use with if statement for breaking this condition in this specific place and continue after that

'''
# Syntax

while condition:
    ...code problem
  
    if another_condition:
        continue

'''

count = 0

while count < 5:
    count = count + 1

    if count == 3:
        continue

    print(count)

# result: 1 2 4 5


print('\n\n')

count = 0

while count < 5:
    count = count + 1
    print(count)

    if count == 3:
        continue


# result: 1 2 3 4 5


# don't do that because program will be confuise after you set condition with if statement for continuatin and put code problem after if statement continuation, don't put code problem after if statement continuation

# while count < 5:

#   if count == 3:
#     continue

#   print(count)
#   count = count + 1

# result: 1 2 3 ???????


# this is example of for loop that use continuation for more visualization i put this example here to meet the compareson between while and for loop that use continuation or break
print('\n\n')

# range(number): range means like you are array that start in range of start this number and end exactly in this number like this is below
# range(10) = 0 1 2 3 4 5 6 7 8 9
# number 10 is not in the list because range is work like index this is why when you say range(10) the number of 10 is not show but when you use this range for string they loop throw all the character of the string because string is base on index 
# the range function is use for array or string or dictionary

for i in range(10):
    if i == 3:  # skips if i is 3
        continue
    print(i)  # 0 1 2 4 5 6 7 8 9


print('\n\n')

for i in range(10):
    if i == 3:  # skips if i is 3
        break
    print(i)  # 0 1 2


print('========================== For Loop with array and dictionary ==========================')
# for loop with list

'''
# Syntax

for iterator in array: # array can be tuple or list or set
    ...code problem

'''

numbers = [0, 1, 2, 3, 4, 5]

# we put all the number of the list from variable (numbers) to variable (number) this is done one by one
for number in numbers:
    print(number)

# result: 0 1 2 3 4 5




# for loop with tuple
'''
# Syntax

for iterator in tpl:
    ...code problem

'''

numbers = (0, 1, 2, 3, 4, 5)

# putting all value of tuple one by one from variable (numbers) to (number)
# using tuple with list is not different
for number in numbers:
    print(number)




# for loop with dictionary
'''
# Syntax

for iterator in dct:
    code goes here

'''



person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

print('\n\n')

# calling all the key of dictionary variable ( person ) to variable ( key ) one by one, why value is not return ? because the value for dictionary is keys when you call the dictionary but when you call the value of key for dictionary in this case the return will be the value of the specific keys
for key in person:

    print(key)

'''
# result

first_name
last_name
age
country
is_marred
skills
address

'''





print('\n\n')


print(person.items())
'''
dict_items([('first_name', 'Asabeneh'), ('last_name', 'Yetayeh'), ('age', 250), ('country', 'Finland'), ('is_marred', True), ('skills', ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']), ('address', {'street': 'Space street', 'zipcode': '02210'})])
'''





import pprint

print('\n\n')

pprint.pprint(person)

'''
{'address': {'street': 'Space street', 'zipcode': '02210'},
 'age': 250,
 'country': 'Finland',
 'first_name': 'Asabeneh',
 'is_marred': True,
 'last_name': 'Yetayeh',
 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']}
'''






print('\n\n')

# we can use function items() for your dictionary to get the key and value of that key if you use for loop to loop technique for return this value
# putting key to the first variable in this case is key because key come pefore value in dictionary
# putting value to the second variable in this case is vlaue because value come after key in dictionary
for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out

'''
first_name Asabeneh
last_name Yetayeh
age 250
country Finland
is_marred True
skills ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
address {'street': 'Space street', 'zipcode': '02210'}
'''





# for loop with set
'''
# Syntax

for iterator in set:
    ...code problem

'''


print('\n\n')

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# putting value of set array from variable (it_companies) to variable (company)
for company in it_companies:
    print(company)

'''
IBM
Google
Oracle
Facebook
Apple
Microsoft
Amazon
'''




# print('\n\n')

# for i in range(len(it_companies)):
#   print(it_companies[i])
  
## you can access the value of set using index number of that value if you try this you get this error # TypeError: 'set' object is not subscriptable



# for i in range(len(language)):
#     print(language[i])






'''
# Syntax

for iterator in sequence:
    ...code problem

    if condition:
        break

'''

print('\n\n')

numbers = (0,1,2,3,4,5)

for number in numbers:
    print(number)

    # if number get the 3 this condition will be true
    if number == 3:
        # the loop in this number will break using break keyword
        break
      
# result: 0 1 2 3





print('\n\n')

numbers = (0,1,2,3,4,5)

for number in numbers:

    # when number get the 3 this condition will be true
    if number == 3:
        # the loop in this number will break using break keyword
        break

    print(number)
      
# result: 0 1 2






'''
# Syntax

for iterator in sequence:
    ...code problem
    
    if condition:
        continue

'''

print('\n\n')

numbers = (0,1,2,3,4,5)

for number in numbers:

    # skipping and 3 and after that continue that journey
    if number == 3:
        continue

    print(number)
    
    '''
    # simplfy this condition
    
    if number != 5:
      print('Next number should be ', number + 1)

    else 
      print('\nloop's end')
      
    '''
    print('Next number should be ', number + 1) if number != 5 else print("\nloop's end") # for short hand conditions need both if and else statements

print('outside the loop')





print('========================== For Loop with String ==========================')

'''
# Syntax

for iterator in string:
    ...code problem

'''

print('\n\n')

language = 'Python'

# the character of string variable (languages) will put to variable (letter) one by one character to the end
for letter in language:
    print(letter)

# result: P y t h o n





print('\n\n')

# putting one by one length number of variable ( language ) to variable ( i ) this is done using   len()   function
for i in range(len(language)):
    # calling array of language depending of this index that we use for calling vlaue of array language
    print(language[i])

# result: P y t h o n




print('========================== The Range Function ==========================')
'''
# Syntax

range(start_number, end_number, step)


range(11) # means from 0 to 11 # 0 1 2 3 4 5 6 7 8 9 10

range(5, 11) # means from 5 to 11 # 5 6 7 8 9 10

range(5, 11, 2) # means from 5 to 11 every 2 step # 5 7 9



# Syntax

list(): changing anything to list if support it

set(): changing anything to set if support it

tuple(): changing anything to tuple if support it

'''

lst = range(11)
print(lst) # range(0, 11)


lst = list(range(11))
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]


st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}






'''
# Syntax

for iterator in range(start, end, step):

'''

print('\n\n')

for number in range(11):
    print(number)   

# result: 0 1 2 3 4 5 6 7 8 9 10




print('========================== Nested For Loop ==========================')

'''
# Syntax

for x in y:
    for t in x:
        print(t)

# you can put for loop inside another for loop and you can also put another for loop inside this for loop that inside another for loop you can continue do that how much you like

'''


person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# putting key of variable ( person ) to variable ( key ) 
for key in person:
    # if one of the key is 'skills' this condition will be true
    if key == 'skills':
        # loop throw on the value of this key of 'skills' using   dictionary_name[key_name]
        # we using for loop for this key because this key is contain list you can do that for set and tuple also
        for skill in person['skills']:
            print(skill)






print('========================== For Else ==========================')
# remember you can use else with for loop but no matter if condition of for loop true or not the else done there job because this type of for loop is use for each to loop throw something

'''
# Syntax

for iterator in something...:
    ...code problem

else:
    ...code problem

'''

for number in range(11):
    print(number)   

# 0 1 2 3 4 5 6 7 8 9 10
else:
    print('\nThe loop stops at', number)





print('========================== Pass ==========================')
# pass means pass or success

for number in range(6):
    # in this for loop we use pass for indicate that not error will happen and all the range of value will be show without any problem
    pass
    print(number)


