import pprint

print('========================== Dictionaries ==========================')
# you can create dictionary using this bracket {} inside this bracket for each value we have key and key can have array ( list or tuple or set ) or dictionary or just normal value

empty_dict = {}
print(empty_dict)  # {}


dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'} # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print('\n', dct)


person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'zoombie': ('JavaScript', 'React', 'Node', 'MongoDB', 'Python'),
    'panties': {'JavaScript', 'React', 'Node', 'MongoDB', 'Python'},
    'panda': {'java': 'JavaScript', 'react': 'React', 'react': 'Node', 'mongo': 'MongoDB', 'python': 'Python'},
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

print('\n', person)

'''

{'first_name': 'Asabeneh', 'last_name': 'Yetayeh', 'age': 250, 'country': 'Finland', 'is_marred': True, 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'], 'zoombie': ('JavaScript', 'React', 'Node', 'MongoDB', 'Python'), 'panties': {'Python', 'Node', 'JavaScript', 'MongoDB', 'React'}, 'panda': {'java': 'JavaScript', 'react': 'Node', 'mongo': 'MongoDB', 'python': 'Python'}, 'address': {'street': 'Space street', 'zipcode': '02210'}}

'''



# format the output using   (pprint)   module

'''

# Syntax

pprint.pprint(variable_name) # ....

print(pprint.pformat(variable_name))  # ....


'''
print('\n\n')
pprint.pprint(person)




pretty_dict_str = pprint.pformat(person)
print('\n\n', pretty_dict_str)

'''

{'address': {'street': 'Space street', 'zipcode': '02210'},
 'age': 250,
 'country': 'Finland',
 'first_name': 'Asabeneh',
 'is_marred': True,
 'last_name': 'Yetayeh',
 'panda': {'java': 'JavaScript',
           'mongo': 'MongoDB',
           'python': 'Python',
           'react': 'Node'},
 'panties': {'Node', 'JavaScript', 'MongoDB', 'React', 'Python'},
 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
 'zoombie': ('JavaScript', 'React', 'Node', 'MongoDB', 'Python')}

'''




print('========================== Dictionary Length ==========================')
# len() return the length of the dictionry, this is work base on key not value

dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print(len(dct)) # 4



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

print(len(person)) # 7



print('========================== Accessing Dictionary Items ( dictionary_name[] )==========================')
# dictionary_name[] will return the value of the key, also accessing the index value of key if the key using array for there value, but not return value of more than one key 

'''
# Syntax

dictionary_name[key_name]

## or

dictionary_name[key_name][index_value]

'''

dct = {
    'key1': 'value1', 
    'key2': 'value2', 
    'key3': 'value3', 
    'key4': 'value4', 
    'address': {
        'street': 'Space street', 
        'zipcode': '02210'
    }
}

print(dct['key1']) # value1
# print(dct['key1', 'key2']) # error because you can't return value of more than one key # KeyError: ('key1', 'key2')
# print(dct['key1']['key2']) # error because you can't return value of more than one key # TypeError: string indices must be integers

print(dct['key4']) # value4
print(dct['address']) # {'street': 'Space street', 'zipcode': '02210'}
# print(dct['address'][0]) # error because you can access the index value of array for key but you can use key name of this key for calling value of key
# print(dct['zoombie']) # error # dictionary_name[] if not find the value return error # KeyError: 'zoombie'



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

print(person['first_name']) # Asabeneh
# print(person['first_name']['last_name']) # TypeError: string indices must be integers
print(person['country'])    # Finland
print(person['skills'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # Space street
# print(person['city'])       # Error # dictionary_name[] if not find the value return the error






print('========================== Accessing Dictionary Items ( dictionary_name.get() )==========================')

# dctionary_name.get(key_name) will return the value of key but one key not more than one key, also you can't access the index value of key if you are using    dictionary_name.get(key_name)
# if get function is not find the value is return (None)
'''
# Syntax

dictionary_name.get(key_name)

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

print(person.get('first_name')) # Asabeneh
# print(person.get('first_name', 'last_name')) # Asabeneh # if you try to return value more than one key you can't with    person.get(key_name)
print(person.get('country'))    # Finland
print(person.get('skills'))     #['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))     # None





print('========================== Adding Items to a Dictionary ==========================')
'''
# Syntax

## overriding key of vlaue for one value

dictionary_name[key_name] = value 

dictionary_name[key_name] = {key: value, key: value, ... } # adding dictionary

dictionary_name[key_name] = [value, value, ...] # adding list

dictionary_name[key_name] = (value, value, ...) # adding tuple

dictionary_name[key_name] = {value, value, ...} # adding set



# adding value without killing the value of array

dictionary_name[key_name].append(value) # this is for this key that use array ( list, tuple, set ) and want add value for there array

'''

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'


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
person['job_title'] = 'Instructor'
 
person['skills'].append('HTML')

# person['address'] = {'Instructor': 'hi'} # if you do that you are override all value of (address) key

# person['address'].append('HTML') # error because you need the key to add value to dictionary # AttributeError: 'dict' object has no attribute 'append'



print(person)

'''
{'first_name': 'Asabeneh', 'last_name': 'Yetayeh', 'age': 250, 'country': 'Finland', 'is_marred': True, 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python', 'HTML'], 'address': {'street': 'Space street', 'zipcode': '02210'}, 'job_title': 'Instructor'}
'''




print('\n\n')
pprint.pprint(person)

'''
{'address': {'street': 'Space street', 'zipcode': '02210'},
 'age': 250,
 'country': 'Finland',
 'first_name': 'Asabeneh',
 'is_marred': True,
 'job_title': 'Instructor',
 'last_name': 'Yetayeh',
 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python', 'HTML']}
'''





print('========================== Modifying Items in a Dictionary ==========================')
'''
# Syntax

dictionary_name[key_name] = value

dictionary_name[key_name].append(value) # adding value for array (list, tuple, set)

'''

dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}

dct['key1'] = 'value-one'

pprint.pprint(dct) # {'key1': 'value-one', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}




print('\n\n')

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

person['first_name'] = 'Eyob'
person['age'] = 252

pprint.pprint(person)
'''
{'address': {'street': 'Space street', 'zipcode': '02210'},
 'age': 252,
 'country': 'Finland',
 'first_name': 'Eyob',
 'is_marred': True,
 'last_name': 'Yetayeh',
 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']}
'''





print('========================== Checking Keys in a Dictionary ==========================')
'''
# Syntax

key_name in dictionary_name

key_name not in dictionary_name

'''

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False





print('========================== Removing Key and Value Pairs from a Dictionary ==========================')
# when you specify the key to delete then the value and the key will be delete entirey

# pop(key): removes the item with the specified key name
# popitem(): removes the last item
# del: removes an item with specified key name
'''
# Syntax

dictionary_name.pop(key_name) 

dictionary_name.popitem()

del dictionary_name[key_name]

'''

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

dct.pop('key1') # removes key1 item

pprint.pprint(dct) # {'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}



dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

dct.popitem() # removes the last item

pprint.pprint(dct) # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}


del dct['key2'] # removes key2 item

pprint.pprint(dct) # {'key1': 'value1', 'key3': 'value3'}




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
person.pop('first_name')        # Removes the firstname item

pprint.pprint(person) 

'''
{'address': {'street': 'Space street', 'zipcode': '02210'},
 'age': 250,
 'country': 'Finland',
 'is_marred': True,
 'last_name': 'Yetayeh',
 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']}
'''



print('\n\n')
person.popitem()                # Removes the address item

pprint.pprint(person) 

'''
{'age': 250,
 'country': 'Finland',
 'is_marred': True,
 'last_name': 'Yetayeh',
 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']}
'''



print('\n\n')
del person['is_marred']        # Removes the is_marred item

pprint.pprint(person) 

'''
{'age': 250,
 'country': 'Finland',
 'last_name': 'Yetayeh',
 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']}
'''





print('========================== Changing Dictionary to a List of Items ==========================')
# dictionary_name.items()   will change the dictionary to list
# this will put the key and value of the key as tuple, if your value is (list or tuple or set or dictionary) then this will be the same but inside the tuple with there key, and all this inside list 

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) 

'''

dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])

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

print(person.items()) 

'''

dict_items([
    ('first_name', 'Asabeneh'), 
    ('last_name', 'Yetayeh'), 
    ('age', 250), 
    ('country', 'Finland'), 
    ('is_marred', True), 
    ('skills', ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']), 
    ('address', {'street': 'Space street', 'zipcode': '02210'})
])

'''




print('========================== Clearing a Dictionary ==========================')
# dictionary_name.clean()   will delete all the value in the dictionary but not the identifier of dictionary means the variable
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None





print('========================== Deleting a Dictionary ==========================')
'''
# Syntax

## this will delete entire dictionary with there identifier means there variable
del dictionary_name

'''

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct

# print(dct) # NameError: name 'dct' is not defined





print('========================== Clearing a Dictionary ==========================')
# dictionary_name.copy()  this will copy the dictionary in this case the copy of the original dictionary will not reference to the original array means any change made in copy dictionary will not made in original dictionary

dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct_copy = dct.copy() 

print(dct_copy) # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}



dct_copy['key1'] = 'new value1'

print(dct) 
# {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}

print(dct_copy) 
# {'key1': 'new value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}





print('========================== Getting Dictionary Keys as a List ==========================')
# dictionary_name.keys()  # getting all the key of dictionary
# this will not show you the key of this dictionary that inside another dictionary

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])


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

keys = person.keys()
print(keys)
# dict_keys(['first_name', 'last_name', 'age', 'country', 'is_marred', 'skills', 'address'])





print('========================== Getting Dictionary values as a List ==========================')
# dictionary_name.values()  # getting all the values of dictionary

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

keys = dct.values()
print(keys)     # dict_values(['value1', 'value2', 'value3', 'value4'])




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

keys = person.values()
print(keys)
# dict_values(['Asabeneh', 'Yetayeh', 250, 'Finland', True, ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'], {'street': 'Space street', 'zipcode': '02210'}])


