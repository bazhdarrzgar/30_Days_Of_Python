print('========================== Regular Expressions ==========================')
print('\n\n\n')
print('========================== The re Module ==========================')

# re = return
import re 



print('========================== Methods in re Module ==========================')
print('========================== Match ==========================')

'''
# Syntax

import re

re.match(regex, string, flag)


## some note
re.match  # span or this flag will return just start and end of index position for the matching regex, also retun matching regex

re.I # means case Ignore

re.match(regex, string, flag).span() # span or return just start and end of index position for the matching regex but like tuple array

variable_name1, variable_name2 = re.match(regex, string, flag).span() # putting start and end index position to this two variable depending of the order of the variable

string[variable_name1:variable_name2] # calling the character of my string using the start and end index position
'''

# re = return

import re

txt = 'I love to teach python and javaScript'
# It returns an object with match regex or in this case is text

# re.I = means calling the index position of the matching regex that we get from string (txt) variable
match = re.match('I love to teach', txt, re.I)
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>

# Return just starting and ending position of the ( match.re ) as tuple for span by using ( span() ) function
span = match.span()
print(span)     # (0, 15)

# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 0, 15

# calling the string character using the start and end of the index position
substring = txt[start:end]
print(substring)       # I love to teach




import re

txt = 'I love to teach python and javaScript'
match = re.match('I like to teach', txt, re.I)

print(match)  # None # this is for representing that is not finding your target in the string




print('========================== Search ==========================')

'''
# Syntax

re.search(regex, string, flag)

flag like ( re.I ) for case ignore

re.search # for finding the start and end of matching position in the string using index for representing this position

regex can be substring or any regular expression you like


## Note

# re.search # one time search

re.search # search in the string one time when it is find target return it but for other value that is matching the search and come after first target don't return it

'''


import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns an object with (span) and (match)
# span menas the start and ending index position of this regex or substring
match = re.search('first', txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>

# return just starting and ending index position of the ( match.re ) as tuple for span using ( span() ) function
span = match.span()
print(span)     # (100, 105)

# putting the start and ending index position of ( span() ) function to this two variable
start, end = span
print(start, end)  # 100 105

# calling the character of string using the starting and ending index position of the string this is done by using string[position_start:position_end]
substring = txt[start:end]
print(substring)       # first





print('========================== find all ==========================')

'''
# Syntax

re.findall(regex, string, flag)

re.findall = return find all
re.findall # return all the matching result of your regex or substring like (list) by using ( re.findall() ) function


## Note: 

re.findall() # this function is infinity time search in the string for finding the all the matching result 

'''

import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns the matching result like (list) array
matches = re.findall('python', txt, re.I)
print(matches)  # ['Python', 'python']





'''
# Some regex

| # means (or) use for doing this or this or both # this is use for character or word or substring

[] # means (or) use for doing this or this or both # this is mostly use for character if you want use it for word and substring then use this (|) regex with it 


## Example

first|second # means first or second or both
[fs] # means f or s or both
'''
import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# Python|python # means  'Python'  or  'python'  or both
matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']


# [Pp] # means (P) capital or (p) small or both
matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']




print('========================== Replacing a Substring ==========================')

'''
# Syntax

re.sub(find, replace, string)
re.sub = return subtraction

find # finding target to replace it # you can use regex
replace # replace this target that you find it # you can use regex


## Note:

re.sub() # this function will replace in the entire string

'''

import re

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

# replace this (%) with nothing ()
matches = re.sub('%', '', txt)
print(matches)





print('========================== Splitting Text Using RegEx Split ==========================')

'''
# Syntax

re.split(regex, string)
re.split() = return split

regex # is for done operation splite base on this regex


## Note:

re.split() # split is done in the entire line
re.split() # the returning value that is splited by this function will be inside the (list) array
'''

import re

txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''

print(re.split('\n', txt)) # splitting using \n - end of line symbol
# ['I am teacher and  I love teaching.', 'There is nothing as rewarding as educating and empowering people.', 'I found teaching more interesting than any other jobs.', 'Does this motivate you to be a teacher?']




print('========================== Writing RegEx Patterns ==========================')

'''
# typing regex in string

r'regex'

## Note:

r'regex' # without this (r) or with this (r) your regex work with any funciton module (re)

'''

import re

# To make case-insensitive add this ( re.I ) flag
# (r) before string means i use regex in this string
regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)  # ['apple']


regex_pattern = r'apple'
# re.I # case-insensative
matches = re.findall(regex_pattern, txt, re.I)
print(matches)  # ['Apple', 'apple']


# [Aa] # menas (A) or (a) small
regex_pattern = r'[Aa]pple'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']



'''

[]: A set of characters
  [a-c] means, 'a or b or c'
  [a-z] means, any letter from 'a to z'
  [A-Z] means, any character from 'A to Z'
  [0-3] means, '0 or 1 or 2 or 3'
  [0-9] means any number from '0 to 9'
  [A-Za-z0-9] any single character, that is 'a to z, A to Z or 0 to 9'


\: uses to 'escape special characters'
  \d means: match where the string contains 'digits' (numbers from 0-9)
  \D means: match where the string does 'not contain digits'


. : 'any character' except new line character(\n)


^: 'starts' with
  r'^substring' eg r'^love', a sentence that 'starts with a word love'
  r'[^abc]' means 'not a, not b, not c'.


$: 'ends' with
  r'substring$' eg 'love$', sentence that 'ends with a word love'


*: 'zero or more' times
  r'[a]*' means a optional or it can occur many times.


+: means "one or more" times
  r'[a]+' means at least once (or more)


?: 'zero or one' time
  r'[a]?' means 'zero times or once'


{3}:   Exactly 3 characters
{3,}:  At least 3 characters
{3,8}: At least 3 and no more than 8 characters
|:     Either or r'apple|banana' means either apple or a banana or both


(): means 'Capture and group'

'''




print('========================== Square Bracket ==========================')

'''
# Syntax

[] # this bracket mostly use for character and means this or this or both

## Example

[ab] # means a or b or both

'''

import re

regex_pattern = r'[Aa]pple' # this square bracket mean either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'

matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']





import re

regex_pattern = r'[Aa]pple|[Bb]anana' # this square bracket means # either A or a # either B or b
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'

matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'banana', 'apple', 'banana']





print('========================== Escape character(\) in RegEx ==========================')

'''
\d  # return any single number number

'''

import re 

regex_pattern = r'\d'  # d is a special character which means digits
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'

matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1'], this is not what we want



print('========================== One or more times(+) ==========================')

import re

# we use (+) not (*) because we want find at least one number and demage it with this numbet that is with each other and not have space or letter between them
regex_pattern = r'\d+'  # d is a special character which means digits, + mean one or more times
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'

matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021'] - now, this is better!




print('========================== Period(.) ==========================')

import re

regex_pattern = r'[a].'  # this square bracket means (a) and (.) means any character except new line after (a)
txt = '''Apple and banana are fruits'''

matches = re.findall(regex_pattern, txt)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']




import re

txt = '''Apple iiiiiand banana are fruits then done'''

# we use + or you can use * because at least we want find my regex matching and after that anything is come after my result demage with it and return
regex_pattern = r'[a].+'  # (.) any character, + any character one or more times
matches = re.findall(regex_pattern, txt)

print(matches)  # ['and banana are fruits']




import re

txt = '''Apple iiiiiand banana are fruits then done'''

# * is not different from + in both of the case
regex_pattern = r'[a].*'  # (.) any character, + any character one or more times
matches = re.findall(regex_pattern, txt)

print(matches)  # ['and banana are fruits']



print('========================== Zero or more times(*) ==========================')

import re

# we use star * because i want find my regex matching result and after that anything is come demage with my matching result and return for me
regex_pattern = r'[a].*'  # (.) any character, * any character zero or more times
txt = '''Apple and banana are fruits'''

matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']




print('========================== Zero or one time(?) ==========================')

import re

txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''

# if i want take something as option in my regex i use this (?) because it is means zero or one ( means come at least one or not )
regex_pattern = r'[Ee]-?mail'  # ? means this symbol '-' is optional come or not

matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']





print('========================== Quantifier in RegEx ==========================')

import re

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'  # \d means digit (number) # exactly 4 times

matches = re.findall(regex_pattern, txt)
print(matches)  # ['2019', '2021']




import re

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{1,4}'   # \d means digit (number) # not less than (1) and no more than (4)

matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']




import re

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{,4}'   # \d means digit (number) # nothing () means take me anything untile you get to the next condition and no more than (4)

matches = re.findall(regex_pattern, txt)
print(matches)  # ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '6', '', '', '', '2019', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '8', '', '', '2021', '']



import re

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{1,}'   # \d means digit (number) # not less than 1 and nothing means unlimited number after that

matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']





print('========================== Cart ^ ==========================')
# Starts with

import re

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This'  # ^ means starts with this that come after that it can be word or character

matches = re.findall(regex_pattern, txt)
print(matches)  # ['This']






# Negation

import re

txt = 'This regular expression example was made on December 6,  2019 a2019 and revised on July 8, 2021'
regex_pattern = r'[^A-Za-z ]+'  # ^ in set character means inside this bracket [] is means negation, not A to Z, not a to z, no space # + means except this negation that come first of this demage other one and return it

matches = re.findall(regex_pattern, txt)
print(matches)  # ['6,', '2019', '2019', '8,', '2021']



