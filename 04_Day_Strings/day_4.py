
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

# if you want use     expandtabs()    you should use    \t    to work this function 
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'






# # find(): Returns the index of first occurrence of substring

# challenge = 'thirty days of python'
# print(challenge.find('y'))  # 5
# print(challenge.find('th')) # 0

# # format()	formats string into nicer output    
# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# job = 'teacher'
# country = 'Finland'
# sentence = 'I am {} {}. I am a {}. I live in {}.'.format(first_name, last_name, job, country)
# print(sentence) # I am Asabeneh Yetayeh. I am a teacher. I live in Finland.

# radius = 10
# pi = 3.14
# area = pi # radius ## 2
# result = 'The area of circle with {} is {}'.format(str(radius), str(area))
# print(result) # The area of circle with 10 is 314.0

# # index(): Returns the index of substring
# challenge = 'thirty days of python'
# print(challenge.find('y'))  # 5
# print(challenge.find('th')) # 0

# # isalnum(): Checks alphanumeric character

# challenge = 'ThirtyDaysPython'
# print(challenge.isalnum()) # True

# challenge = '30DaysPython'
# print(challenge.isalnum()) # True

# challenge = 'thirty days of python'
# print(challenge.isalnum()) # False

# challenge = 'thirty days of python 2019'
# print(challenge.isalnum()) # False

# # isalpha(): Checks if all characters are alphabets

# challenge = 'thirty days of python'
# print(challenge.isalpha()) # True
# num = '123'
# print(num.isalpha())      # False

# # isdecimal(): Checks Decimal Characters

# challenge = 'thirty days of python'
# print(challenge.find('y'))  # 5
# print(challenge.find('th')) # 0

# # isdigit(): Checks Digit Characters

# challenge = 'Thirty'
# print(challenge.isdigit()) # False
# challenge = '30'
# print(challenge.digit())   # True

# # isdecimal():Checks decimal characters

# num = '10'
# print(num.isdecimal()) # True
# num = '10.5'
# print(num.isdecimal()) # False


# # isidentifier():Checks for valid identifier means it check if a string is a valid variable name

# challenge = '30DaysOfPython'
# print(challenge.isidentifier()) # False, because it starts with a number
# challenge = 'thirty_days_of_python'
# print(challenge.isidentifier()) # True


# # islower():Checks if all alphabets in a string are lowercase

# challenge = 'thirty days of python'
# print(challenge.islower()) # True
# challenge = 'Thirty days of python'
# print(challenge.islower()) # False

# # isupper(): returns if all characters are uppercase characters

# challenge = 'thirty days of python'
# print(challenge.isupper()) #  False
# challenge = 'THIRTY DAYS OF PYTHON'
# print(challenge.isupper()) # True


# # isnumeric():Checks numeric characters

# num = '10'
# print(num.isnumeric())      # True
# print('ten'.isnumeric())    # False

# # join(): Returns a concatenated string

# web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
# result = '#, '.join(web_tech)
# print(result) # 'HTML# CSS# JavaScript# React'

# # strip(): Removes both leading and trailing characters

# challenge = ' thirty days of python '
# print(challenge.strip('y')) # 5

# # replace(): Replaces substring inside

# challenge = 'thirty days of python'
# print(challenge.replace('python', 'coding')) # 'thirty days of coding'

# # split():Splits String from Left

# challenge = 'thirty days of python'
# print(challenge.split()) # ['thirty', 'days', 'of', 'python']

# # title(): Returns a Title Cased String

# challenge = 'thirty days of python'
# print(challenge.title()) # Thirty Days Of Python

# # swapcase(): Checks if String Starts with the Specified String
  
# challenge = 'thirty days of python'
# print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
# challenge = 'Thirty Days Of Python'
# print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

# # startswith(): Checks if String Starts with the Specified String

# challenge = 'thirty days of python'
# print(challenge.startswith('thirty')) # True
# challenge = '30 days of python'
# print(challenge.startswith('thirty')) # False