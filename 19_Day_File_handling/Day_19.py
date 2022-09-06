print('========================== File Handling ==========================')
'''
# Syntax

open('filename', mode) # mode(r, a, w, x, t, b)  could be to read, write, update


"r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)

'''




print('========================== Opening Files for Reading ==========================')

## open()  this function will open the file and return the (name) of file and (mode) and (encoding) information of this file
## open()  this function reutrn error if not find the file
# f = open('./files/reading_file_example.txt')
f = open('sample.txt')

print(f) # <_io.TextIOWrapper name='sample.txt' mode='r' encoding='UTF-8'>





## read()   this function will read the file for returning the value of that file
## open()   this function will open the file
## close()  this function will close the file

f = open('sample.txt')

txt = f.read()
print(type(txt)) # <class 'str'> # because text file read all the data as string
print(txt) # hello world 22

f.close()





f = open('sample.txt')

# read only 10 length of the character this is use length for reading not index for
txt = f.read(10)
print(type(txt)) # <class 'str'>
print(txt) # hello worl

f.close()





f = open('sample.txt')

# readline()  this function will read only one line
line = f.readline()
print(type(line)) # <class 'str'>
print(line) # hello world 1

f.close()





f = open('sample.txt')

# readline()    this function only read one line
# readlines()   this function will read all the line and return the (line and new line) like (list) array
lines = f.readlines()
print(type(lines))
print(lines)
# ['hello world 1\n', 'hello world 2\n', 'hello world 3\n', 'hello world 4\n', 'hello world 5\n', 'hello world 6\n', 'hello world 7\n', 'hello world 8\n', 'hello world 9\n', 'hello world 10\n', 'hello world 11\n', 'hello world 12\n', 'hello world 13\n']

f.close()





f = open('sample.txt')

# split()   # this function will read every line but in sparate way not all the line in one time this is why the new line is not return when we use read() function
# after this function we have splitlines() function that take care for returning this line like (list)
# splitlines()   # this function is split the line by nothing means it will remove the new line and all this data return like (list) array
lines = f.read().splitlines()
print(type(lines)) # <class 'str'>
print(lines)
# ['hello world 1', 'hello world 2', 'hello world 3', 'hello world 4', 'hello world 5', 'hello world 6', 'hello world 7', 'hello world 8', 'hello world 9', 'hello world 10', 'hello world 11', 'hello world 12', 'hello world 13']

f.close()





# you can use with loop like while loop or other for loop for returning every line of the file and put the all the vlaue to other variable
# Note: the   open()   function will return all the line of the file, you don't need while loop or for loop in this case it is optional
with open('sample.txt') as f:
    lines = f.read().splitlines()
    print(type(lines)) # <class 'list'>
    print(lines)
    # ['hello world 1', 'hello world 2', 'hello world 3', 'hello world 4', 'hello world 5', 'hello world 6', 'hello world 7', 'hello world 8', 'hello world 9', 'hello world 10', 'hello world 11', 'hello world 12', 'hello world 13']




print('========================== Opening Files for Writing and Updating ==========================')

'''
"a" - append - will append to the end of the file, if the file does not it creates a new file.

"w" - write - will overwrite any existing content, if the file does not exist it creates.

'''

with open('sample.txt', 'a') as f:
    # write()  this function will add any value you want to your file
    # Note: if the file is not exit then   write()   function is create the file for it and put it this value into this file that create it
    done = f.write('This text has to be appended at the end\n')
    print(done) # 39 # it is mean 39 character


with open('./files/writing_file_example.txt','w') as f:
    f.write('This text will be written in a newly created file')
    



print('========================== Deleting Files ==========================')

# os = operating system # it will take control to your system by some function
import os
# remove()  this function use for remove the empty or none empty file
# Note: if file is not exit then this will return the error
os.remove('sample1.txt')




import os
# path.exists()   this function is check if the path exist or not
# exists()        this funciton is check if the file or folder exist or not
if os.path.exists('sample1.txt'):
    os.remove('sample.txt')
else:
    print('The file does not exist')
    
    

print('========================== File Types ==========================')
print('========================== File with json Extension ==========================')

import pprint

# dictionary
person_dct= {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}

pprint.pprint(person_dct)

'''
{'city': 'Helsinki',
 'country': 'Finland',
 'name': 'Asabeneh',
 'skills': ['JavaScrip', 'React', 'Python']}
'''




import pprint

# JSON: A string form a dictionary
person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"

pprint.pprint(person_json)

'''
("{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': "
 "['JavaScrip', 'React', 'Python']}")
'''





import pprint

# we use three quotes and make it multiple line to make it more readable this is for JSON string form dictionary
person_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}'''

pprint.pprint(person_json)

'''
('{\n'
 '    "name":"Asabeneh",\n'
 '    "country":"Finland",\n'
 '    "city":"Helsinki",\n'
 '    "skills":["JavaScrip", "React","Python"]\n'
 '}')
'''




print('========================== Changing JSON to Dictionary ==========================')

'''
# Syntax

json.loads(json..)

'''

import json

# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''

# let's change JSON to dictionary
person_dct = json.loads(person_json)

print(type(person_dct)) # <class 'dict'>
print(person_dct) # {'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}
# access the value of key using the key of this value
print(person_dct['name']) # Asabeneh





print('========================== Changing Dictionary to JSON ==========================')

'''
# Syntax

json.dumps(dictionary..., indent = number_of_space) # indent is for beautifies the json, it is number of space for the new line # by default not space and not new line

'''

import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}

# let's convert it to json
person_json = json.dumps(person) # indent could be 2, 4, 8. It beautifies the json
print(type(person_json)) # <class 'str'>
print(person_json)
# {"name": "Asabeneh", "country": "Finland", "city": "Helsinki", "skills": ["JavaScrip", "React", "Python"]}

person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
print(type(person_json)) # <class 'str'>
print(person_json)
'''
{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": [
        "JavaScrip",
        "React",
        "Python"
    ]
}
'''





print('========================== Saving as JSON File ==========================')

'''
# Syntax

import json

dictionary = {
...

}

## with   open()   function
# w   means write
# encoding specify the type of encodig it can be utf-8 or ascii or utf...
with open('file-name.json', 'w', encoding =....) as variable_name:
    ## with   json.dump()   function
    # ensure_ascii    for ensuring if you want use ascii or not
    # indent          for specify the number of space
    json.dump(dictionary, variable_name, ensure_ascii = True_or_False, indent = number)

'''

# remember for importing json
import json

# dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}

## this is use with   open()   function
# w           flag menas write
# encoding    specify the type of encoding it can be ascii or utf-16 or utf-32 ir utf-8
with open('sample.json', 'w', encoding='utf-8') as f:
    ## this is use with   json.dump()   function
    # ensure_ascii    for ensuring that if you want use the ascii (True) or not (False)
    # index           for number of space after each line
    json.dump(person, f, ensure_ascii=False, indent = 4)


    
    
    
    
print('========================== File with csv Extension ==========================')

import csv

with open('amex.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
    line_count = 0

    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1

    print(f'Number of lines:  {line_count}')

'''
Column names are :Symbol, Name, LastSale, MarketCap, IPOyear, Sector, industry, Summary Quote, 
	XXII is a teachers. He lives in 22nd Century Group, Inc, 0.8951.
	..............
	..............
'''






print('========================== File with xlsx Extension ==========================')

'''
# Syntax

## Open xls file

xlrd.open_workbook('name_file.xls')


## printing number of column

xlrd.open_workbook('name_file.xls').nsheets


## printing name of sheet

xlrd.open_workbook('name_file.xls').names

'''

# pip install xlrd
import xlrd

excel_book = xlrd.open_workbook('sample3.xls')

print(excel_book.nsheets) # 2 # number of the column
print(excel_book.sheet_names) # <bound method Book.sheet_names of <xlrd.book.Book object at 0x7f7f559430a0>> # ???




print('========================== File with xml Extension ==========================')

'''

<?xml version="1.0"?>
<person gender="female">
  <name>Asabeneh</name>
  <country>Finland</country>
  <city>Helsinki</city>
  <skills>
    <skill>JavaScrip</skill>
    <skill>React</skill>
    <skill>Python</skill>
  </skills>
</person>

'''





import xml.etree.ElementTree as ET

tree = ET.parse('sample4.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)

'''
Root tag: person
Attribute: {'gender': 'female'}
field:  name
field:  country
field:  city
field:  skills
'''
    
    
   