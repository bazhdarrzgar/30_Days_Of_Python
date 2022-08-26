
print('========================== Single line comment ==========================')
# we can comment in single line using hashtag (#)
letter = 'P'                # # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1 # return the length of the string using   ( len() )  function
greeting = 'Hello, World!'  # # String could be a single or double quote,"Hello, World!" or 'Hello, World!'
print(greeting)             # Hello, World!
print(len(greeting))        # 13 # return the length of the string using   ( len() )  function
sentence = "I hope you are enjoying 30 days of python challenge"
print(sentence) # "I hope you are enjoying 30 days of python challenge" 




print('========================== Multiline String ==========================')
# we can comment in multiple line using single quotes ( '''.....''' ) or double quotes ( """....""" ) 
# also because we are using single quotes or double quotes and string is represent by single quotes or double quotes or this quotes (``) then if you are use this quotes for variable then this quotes will be the string not the comment

'''
comment.....
'''
# enter will be the new line inside the string this is true in python
multiline_string = '''this is string 
I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.
'''
print(multiline_string)

"""
comment.....
"""
# Another way of doing the same thing comment
multiline_string = """this is string
I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)






print('========================== String Concatenation ==========================')
# you can concate multiple string using plus sign  (+)
first_name = 'Asabeneh' # string
last_name = 'Yetayeh' # string
space = ' ' # empty string
full_name = first_name  +  space + last_name 
print(full_name) # Asabeneh Yetayeh
# Checking length of a string using len() builtin function
print(len(space)) # 1
print(len(first_name))  # 8
print(len(last_name))   # 7
print(len(first_name) > len(last_name)) # True
print(len(full_name)) # 15





print('========================== Unpacking characters ==========================')
# you can unpack the string using variable like array 
'''
# Syntax

variable_name = 'string'       # length of the string is 6
a,b,c,d,e,f = variable_name    # length of the varible is 6 each variable depending of the index number is equal to the string character

'''
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
# a,b,c,d,e = language # error because the variable is not match all the character in the string or length of the string
print(a) # P
print(b) # y
print(c) # t 
print(d) # h
print(e) # o
print(f) # n





print('========================== Accessing characters in strings by index (positive number)==========================')
# accessing character length like array using this bracket   [ ]
'''
# Syntax

variable_name = 'string'
variable_name[0] # s
variable_name[1] # t
variable_name[2] # r
variable_name[3] # i
variable_name[4] # n
variable_name[5] # g

# s t r i n g
# 0 1 2 3 4 5

'''
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1 # length of 'Python' is 6 and 6 - 1 = 5 index 5 = n means end character                                                                          
last_letter = language[last_index]
print(last_letter) # n





print('========================== Accessing characters in strings by index (negative number) ==========================')
'''
# If we want to start from right end we can use negative indexing. -1 is the last index

variable_name = 'string'
variable_name[-6] # s
variable_name[-5] # t
variable_name[-4] # r
variable_name[-3] # i
variable_name[-2] # n
variable_name[-1] # g

#  s   t   r   i   n   g
# -6  -5  -4  -3  -2  -1
#  0   1   2   3   4   5
'''
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o






print('========================== Slicing ==========================')
'''
# Syntax

varaible_name = 'string'
variable_name[start_index:end_index]
variable_name[0:4] # stri # means start in index 0 and finish in index 4 means index 4 is not in the list
variable_name[-1:-4] # ign # means start in index -1 and finish in index -4 means index -4 is not in the list
'''

language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) # Pyt
last_three = language[3:6] # start in index 3 and finish in index 6 but index 6 is not exist then we just say index 6 is like empty thing we do that because we want end character
print(last_three) # hon
# Another way
last_three = language[-3:] # means start in index -3 and end index is not specify in this case programmer need print from index -3 to the end character end character is in the list, for minize number is from minize to positive number it is like we say    [-3:positive_infinity_number]
print(last_three)   # hon
last_three = language[3:] # means start in index 3 and end index is not specify in this case programmer need print from index -3 to the end character end character is in the list
print(last_three)   # hon






print('========================== Skipping character while splitting Python strings ==========================')
'''
# Syntax

variable_name = 'string'
variable_name[start_index:end_index:step]
varaible_name[0:6:2] # srg
'''

language = 'Python'
pto = language[0:6:2] # start in index 0 and finish in index 6 and do that in every 2 step
print(pto) # pto




print('========================== Escape sequence ==========================')
# \n   new line
# \t   tab
# \    for escapping character like slash ( \   or   single quotes '   or   double quotes " )
print('I hope every one enjoying the python challenge.\nDo you ?') # line break
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a back slash  symbol (\\)') # To write a back slash
print('In every programming language it starts with \"Hello, World!\"')





print('========================== String Methods ==========================')
print('\n\n\n')
print('========================== upper() and lower() and capitalize() ==========================')
# capitalize(): Converts the first character the string to Capital Letter
# upper(): Converts String to upper case
# lower(): Converts String to lower case

challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'
print(challenge.upper()) # 'THIRTY DAYS OF PYTHON'
print(challenge.lower()) # 'thirty days of python'





print('========================== count() ==========================')
'''
# count(): returns occurrences of substring in string

 
# Syntax
count(substring, start=.., end=..)


## Example

variable_name = 'string'
variable_name.count('s', start = 2, end = 6) # start index is in the list, but end index is not in the list at 
variable_name.count('s') # by deafult search in the whole string
'''

challenge = 'thirty days of pythony'
print(challenge.count('y')) # 3 # by deafult search in the whole string
print(challenge.count('y', 7, 21)) # 2 # start index is in the list but end index is not in the list
print(challenge.count('y', 7, 22)) # 3 
print(challenge.count('th')) # 2`





print('========================== endswith() ==========================')
# endswith(): Checks if a string ends with a specified ending (substring or number or ..) if exist then return True or False
'''
# Syntax

endswith('substring')


## Example
variable_name = 'string'
endswith('g') # True

'''
challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False





print('========================== expandtabs() ==========================')
# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
# \t   tab size is 8
# expandtabs()  tab size is 8 by deafult

# if you want use     expandtabs()    you should use    \t    to work your function   expandtabs() 
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'






print('========================== find() ==========================')
# find(): Returns the index of first result of finding occurrence of substring in the string
# if you want search in the entir substring you should use regular expression with flag to search in the entire substring

challenge = 'thirty days of python'
print(challenge.find('y'))  # 5 # we find it in index 5
print(challenge.find('th')) # 0 # we find it in index 0



print('========================== format() ==========================')
# format()	formats string into nicer output or putting value of variable in the string 
'''
# Syntax

variable_name_1 = value1
variable_name_2 = value2
variable_name_3 = value3
variable_name_... = ...

variable_name4 = 'hello i am {}, i am from {}, i am right now in {}'.format(variable_name_1, variable_name_2, variable_name_3, ...)

print(variable_name_4) # hello i am value1, i am from value2, i am right now in value3
'''  

first_name = 'Asabeneh'
last_name = 'Yetayeh'
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(first_name, last_name, job, country) # putting the value of this variable to the independed place in the string for this bracket     {}   depended to the index number or order of the variable
# sentence = f'I am {first_name} {last_name}. I am a {job}. I live in {country}.'
print(sentence) # I am Asabeneh Yetayeh. I am a teacher. I live in Finland.


# changing number to string using     str()    function
radius = 10
pi = 3.14
area = pi * radius # radius ## 2
result = 'The area of circle with {} is {}'.format(str(radius), str(round(area, 1)))
print(result) # The area of circle with 10 is 31.4





print('========================== index() ==========================')

# index(): Returns the index of first result of substring in the string
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5 # using find() function
print(challenge.find('th')) # 0 # using find() function

print(challenge.index('y'))  # 5 # using index() function
print(challenge.index('th')) # 0 # using index() function



print('========================== isalnum() ==========================')
# isalnum(): Checks alphanumeric character means if all the index in the list is alphanumric in the english character also number but not symbol and .....

challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False # because we have space

challenge = 'thirtydaysofpython2019' # number is in the list
print(challenge.isalnum()) # False





print('========================== isalpha() ==========================')
# isalpha(): Checks if all characters are alphabets it is accept all the character in english also space but not symbol and number and ....

challenge = 'thirtydaysofpython'
print(challenge.isalpha()) # True
challenge = 'thirty days of python'
print(challenge.isalpha()) # False
num = '123'
print(num.isalpha())      # False




print('========================== isdecimal() ==========================')
# isdecimal(): Checks if all character is Decimal Characters this is not accept the space and symbol and character english and ...

num = '10'
print(num.isdecimal()) # True
num = '10 '
print(num.isdecimal()) # False
num = '10.5'
print(num.isdecimal()) # False




print('========================== isdigit() ==========================')
# isdigit(): Checks Digit Characters, means just number not space and not character english and not symbol and ..
# isdigit()  =   isdecimal()

challenge = '30'
print(challenge.isdigit())   # True
challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30:)'
print(challenge.isdigit())   # True





print('========================== isidentifier() ==========================')
# isidentifier(): Checks for valid identifier, is not accept number and symbol or space or .. just (string) or (string with underscore)

challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True
challenge = 'thirty_days_of_python_:)'
print(challenge.isidentifier()) # False
challenge = 'thirty days of python_:)'
print(challenge.isidentifier()) # False




print('========================== islower() ==========================')
# islower(): Checks if all alphabets in a string are lowercase

challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.islower()) # False
challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False



print('========================== isupper() ==========================')
# islower(): Checks if all alphabets in a string are uppercase

challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True
challenge = 'thirty days of python'
print(challenge.isupper()) # False
challenge = 'Thirty days of python'
print(challenge.isupper()) # False





print('========================== isupper() ==========================')
# isnumeric(): Checks numeric characters, just number accept not space or point or anything just fucking number

num = '10'
print(num.isnumeric())      # True
print('ten'.isnumeric())    # False
print('10:0'.isnumeric())    # False
print('10.0'.isnumeric())    # False




print('========================== join() ==========================')
# join(): Returns a concatenated string

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
# this will joing all the list
# also because join is work like for loop means concate the list value one by one, means not all this value join it in one time, because of that you can use string before   join()   function to beutify your work
result = '#, '.join(web_tech) 
print(result) # HTML#, CSS#, JavaScript#, React



print('========================== strip() ==========================')
# strip(): Removes both leading and trailing characters

challenge = ' thirty days of python '
print(challenge) #  thirty days of python # with space before the string
print(challenge.strip()) # thirty days of python # without space before the string 
print(challenge.strip('of')) #  thirty days of python # they don't work because   strip()  is search from first index (0) if not find then get out, if you want search in the entire string you should use regular expression with it
print(challenge.strip(' thirty')) # days of python # this is work because   strip()   in this time is find the match from first index (0) and second and ... 




print('========================== replace() ==========================')
# replace(): Replaces substring inside string this is true for the entire string means return all this value that replace by   replace()   function
'''
# Syntax

variable_name = 'string is string'
variable_name.replace('find something', 'replace with something')

'''

challenge = 'thirty days of python and python'
print(challenge.replace('python', 'coding')) # thirty days of coding and coding
print(challenge.replace('thi', 'fou')) # fourty days of python and python





# print('========================== split() ==========================')
# split(): Splits String from Left, work base on space by default

challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']

challenge = 'thirty,days,of,python'
print(challenge.split(',')) # ['thirty', 'days', 'of', 'python']

challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']





print('========================== title() ==========================')
# title(): Returns a Title Cased String, change all the first character word to capital in the entire statement or line
# capitilize()  !=   title()
# capitilize() function just capital the first character in this word that come first in the statement or line

challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python
print(challenge.capitalize()) # Thirty days of python




print('========================== swapcase() ==========================')
# swapcase(): swapcase means swap the cases this is Checks if String Starts with the Specified String, just change capital to small and small to capital
  
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON





print('========================== startswith() ==========================')
# startswith(): Checks if String Starts with the Specified String, return True or False for the answear

challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True
challenge = '30 days of python'
print(challenge.startswith('thirty')) # False



print('========================== endswith() ==========================')
# startswith(): Checks if String Ends with the Specified String, return True or False for the answear

challenge = 'thirty days of python'
print(challenge.endswith('python')) # True
challenge = '30 days of python'
print(challenge.endswith('javascript')) # False
