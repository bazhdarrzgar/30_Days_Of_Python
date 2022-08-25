
'''

# different type of array

    list use this bracket [ ] for value
    tuple use this bracket ( ) for value
    set use this bracket { } for vlaue
    
# dictionary object use this bracket { } also use this bracket inside [ ] it but sometimes for key and value

'''


print('========================== Variables in Python ==========================')

'''
# Syntax variable

    variable_name = value



# Syntax array list

    variable_name = [value, value, ...]
   
   
    
# Syntax object

    variable_name = {
        'key': value,
        'key': value,
        'key': value,
        ....
    }

'''

first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'Asabeneh', 
    'lastname':'Yetayeh', 
    'country':'Finland',
    'city':'Helsinki'
    }

# Printing the values stored in the variables
'''
# Syntax get length of array or string

len(variable_name)

'''
print('First name:', first_name) # First name:  Asabeneh
print('First name length:', len(first_name)) # Last name length  8
print('Last name: ', last_name) # Last name:  Helsinki
print('Last name length: ', len(last_name)) # Last name length  8
print('Country: ', country) # Country:  Finland
print('City: ', city) #  City:  Helsinki
print('Age: ', age) # Age:  250
print('Married: ', is_married) # Married:  True 
print('Skills: ', skills) # Skills:  ['HTML', 'CSS', 'JS', 'React', 'Python']
print('Skills length: ', len(skills)) # Skills: 5
print('Person information: ', person_info) 
'''
# Person information:  person_info = {'firstname':'Asabeneh', 'lastname':'Yetayeh', 'country':'Finland','city':'Helsinki'}\

'''
print('Person information length: ', len(person_info)) # Person information length:  4



# Declaring multiple variables in one line using comma (,) also changing the value of this variable just by declaring the variable again
'''
# Syntax declaring multiple variable in one line and taking value of this variable

variable_1, variable_2, variable_3, .... = value_of_variable_1, value_of_variable_2, value_of_variable_3, ....


# Syntax of changing value of variable

variable_name_1 = 'hello'
print(variable_name_1) # world

variable_name_1 = 'world'
print(variable_name_1) # world


# Syntax changing value of array list

variable_name = [value, value, value, ...]
print(variable_name[0]) # value
print(variable_name[1]) # value
print(variable_name[2]) # value



variable_name[0] = new_value
variable_name[1] = new_value
variable_name[2] = new_value

print(variable_name[0]) # new_value
print(variable_name[1]) # new_value
print(variable_name[2]) # new_value

'''

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True
print(first_name, last_name, country, age, is_married) # Asabeneh Yetayeh Helsink 250 True
print('First name:', first_name) # First name:  Asabeneh
print('Last name: ', last_name) # Last name:  Yetayeh
print('Country: ', country) # Country:  Helsink
print('Age: ', age) # Age:  250
print('Married: ', is_married) # Married:  True


print('========================== change value of array ==========================')
array_list = ['hello', 'world', 'welcome', 'to', 30, 'days', 'of python']

print(array_list[0]) # hello 
print(array_list[1]) # world
print(array_list[2]) # welcome



array_list[0] = 'new hello'
array_list[1] = 'new world'
array_list[2] = 'new welcome'

print(array_list[0]) # new hello
print(array_list[1]) # new world
print(array_list[2]) # new welcome




print('========================== casting ==========================')

# Casting: Is Converting one data type to another data type. We use int(), float(), str(), list(), set(), ....


# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6

# str to list
first_name = 'Asabeneh'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']


print('========================== built in function in python ==========================')

'''
## built in function in pythoin 


abs()			#Returns the absolute value of a number
all()			#Returns True if all items in an iterable object are true
any()			#Returns True if any item in an iterable object is true
ascii()			#Returns a readable version of an object. Replaces none-ascii characters with escape character
bin()			#Returns the binary version of a number
bool()			#Returns the boolean value of the specified object
bytearray()		#Returns an array of bytes
bytes()			#Returns a bytes object
callable()		#Returns True if the specified object is callable, otherwise False
chr()			#Returns a character from the specified Unicode code.
classmethod()	#Converts a method into a class method
compile()		#Returns the specified source as an object, ready to be executed
complex()		#Returns a complex number
delattr()		#Deletes the specified attribute (property or method) from the specified object
dict()			#Returns a dictionary (Array)
dir()			#Returns a list of the specified object's properties and methods
divmod()		#Returns the quotient and the remainder when argument1 is divided by argument2
enumerate()		#Takes a collection (e.g. a tuple) and returns it as an enumerate object
eval()			#Evaluates and executes an expression
exec()			#Executes the specified code (or object)
filter()		#Use a filter function to exclude items in an iterable object
float()			#Returns a floating point number
format()		#Formats a specified value
frozenset()		#Returns a frozenset object
getattr()		#Returns the value of the specified attribute (property or method)
globals()		#Returns the current global symbol table as a dictionary
hasattr()		#Returns True if the specified object has the specified attribute (property/method)
hash()			#Returns the hash value of a specified object
help()			#Executes the built-in help system
hex()			#Converts a number into a hexadecimal value
id()			#Returns the id of an object
input()			#Allowing user input
int()			#Returns an integer number
isinstance()	#Returns True if a specified object is an instance of a specified object
issubclass()	#Returns True if a specified class is a subclass of a specified object
iter()			#Returns an iterator object
len()			#Returns the length of an object
list()			#Returns a list
locals()		#Returns an updated dictionary of the current local symbol table
map()			#Returns the specified iterator with the specified function applied to each item
max()			#Returns the largest item in an iterable
memoryview()	#Returns a memory view object
min()			#Returns the smallest item in an iterable
next()			#Returns the next item in an iterable
object()		#Returns a new object
oct()			#Converts a number into an octal
open()			#Opens a file and returns a file object
ord()			#Convert an integer representing the Unicode of the specified character
pow()			#Returns the value of x to the power of y
print()			#Prints to the standard output device
property()		#Gets, sets, deletes a property
range()			#Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
repr()			#Returns a readable version of an object
reversed()		#Returns a reversed iterator
round()			#Rounds a numbers
set()			#Returns a new set object
setattr()		#Sets an attribute (property/method) of an object
slice()			#Returns a slice object
sorted()		#Returns a sorted list
staticmethod()	#Converts a method into a static method
str()			#Returns a string object
sum()			#Sums the items of an iterator
super()			#Returns an object that represents the parent class
tuple()			#Returns a tuple
type()			#Returns the type of an object
vars()			#Returns the __dict__ property of an object
zip()			#Returns an iterator, from two or more iterators

'''

print('========================== len() & type() & str() & int() & float() function ==========================')
print('Hello, World!') # Hello, World!
len('Hello, World!') # 13
print(type('Hello, World!')) # <class 'str'>
print(str(10)) # 10 # like int
print(int('10')) # 10 # like string
print(float(10)) # 10.0 # like float
# print(input('Enter your name:')) 
# Enter your name: ... 
# ...


print('========================== abs() ==========================')
a = 12
b = -4
c = 3+4j 
e = 3+80j 
f = 3+16j 
d = 7.90
print(abs(a)) # 12  # return actual value
print(abs(b)) # 4   # because abs() function change - to + for number that under 0
print(abs(c)) # 5
print(abs(e)) # 80.05623023850174
print(abs(f)) # 16.278820596099706
print(abs(d)) # 7.9 # abs() function will format the number if number of point is more than one (1) then it will remove all there just take it 1 number after dot (.)



print('========================== all() ==========================')
# Same as logical 'and' operator
tuple = (0, True, False)
x = all(tuple)
print(x)

tuple = (1, True, True)
x = all(tuple)
print(x)




print('========================== all() with object ==========================')
# same as logical 'and' operator
# true if we have the right rule for creating dictionary object
# 0 is true, 1 is false
sampledict = {0 : "Apple", 1 : "Orange"}
x = all(sampledict)
print(x) # False

sampledict = {0 : "Apple",0 : "Orange"}
x = all(sampledict)
print(x) # True

## ????!!!
sampledict = {1 : "Apple",1 : "Orange"}
x = all(sampledict)
print(x) # True

sampledict = {'firstname' : "Apple", 'lastname' : "Orange"}
x = all(sampledict)
print(x) # True




print('========================== any() ==========================')
#  For an empty iterable object, any() returns False.
'''

any(2,3,4,5,9) – True
Any(2,0,9,1,8) – Returns False

'''
myset = {0, 1, 0}
x = any(myset)
print(x)


myset = {}
x = any(myset) 
print(x) # false





print('========================== bin() ==========================')
# This function returns the binary value of a number
a = 5
print(bin(a)) # 0b101

# b = 'a'
# print(bin(b)) # error


print(bin(4)) # 0b100
print(bin(9)) # 0b1001






print('========================== round() ==========================')
# if point after dot (.) is greater than 5 then one number is increase if not then not increase
print(round(4.5)) # 4
print(round(-7.7)) # -8






print('========================== bool() ==========================')
# greater than 0 is True for boolean 
# less than 0 is false for boolean
# 0 is not the number means it will be false

# 'False' or False is True for boolean
# False is False for boolean

# 'True' or True is True for boolean
# True or True is True for boolean
print(bool(0)) # False
print(bool(4.5)) # True
print(bool(-4.5)) # True
print(bool(None)) # False
print(bool("False")) # True
print(bool("True")) # True
print(bool(False)) # False
print(bool(True)) # True




print('========================== bytearray() ==========================')
# This function returns a new array of bytes, i.e. a mutable sequence of integers from range 0 to 256.

# Syntax: bytearray(source,encoding,errors)
# source is value can be empty or number or string but in double quotes or single quotes
# endcoding like   utf-8   utf-16   utf-32
'''
The values to function are optional.
If any non-ascii value is given to the function, it gives the error -TypeError: string argument without an encoding.
'''

print(bytearray()) # bytearray(b'') # we get byte code this is empty ''
print(bytearray('Python','utf-8')) # bytearray(b'Python') # we get byte code this is (Python)
print(bytearray('2500','utf-8')) # bytearray(b'Python') # we get byte code this is (Python)




print('========================== compile()  with   exec() ==========================')
#  \n   means new line

# Syntax: 
    # variable_name = Compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
    # exec(variable_name)

myCode = 'a = 7\nb=9\nresult=a*b\nprint("result =",result)'
'''
a = 7
b = 9
result = a * b
print("result = ", result)

'''
# i use   (exec)   mod because i want see my string like code not like text string
codeObject = compile(myCode, 'anything...', 'exec')
## execute the compiler result using   ( exec() ) function
exec(codeObject) # result = 63





print('========================== list() ==========================')
# changing string to list of character using   ( list() )   function
# or changing tuple to list using   ( list() )   function
# or changing list to list using   ( list() )   function
# Syntax: list([iterable])
    # Ex: 
        # list('string')
        # list([1, 2, 3])
        # list((1,2,3,4))

print(list()) # [] # returns empty list 
stringobj = 'PALINDROME'
print(list(stringobj)) # ['P', 'A', 'L', 'I', 'N', 'D', 'R', 'O', 'M', 'E']
tupleobj = ('a', 'e', 'i', 'o', 'u')
print(list(tupleobj)) # ['a', 'e', 'i', 'o', 'u']
listobj = ['1', '2', '3', 'o', '10u']
print(list(listobj)) # ['1', '2', '3', 'o', '10u']





print('========================== len() ==========================')
# return length of string or array or object dictionary
# Syntax: len([object])

stringobj = 'PALINDROME' # string
print(len(stringobj)) # 10
tupleobj = ('a', 'e', 'i', 'o', 'u') # tuple
print(len(tupleobj)) # 5
listobj = ['1', '2', '3', 'o', '10u'] # list
print(len(listobj)) # 5



print('========================== input() ==========================')
# Syntax: input()
# input("input something: ")




print('========================== callback() ==========================')
# callable(function_name) function will return if function is return or not
# Syntax: callable(Object)

'''
# Syntax create function

def function_name():
    .....code problem

# calling function
function_name

'''
def myFun(): 
    return 5

res = myFun 
print(callable(res)) # function is called to get this value # True
num1 = 15 * 5
print(callable(num1)) # no function is called # False




print('========================== type() ==========================')
# Syntax: type(Object)
# Syntax: type(name,bases,dict)

tupleObj=(3, 4, 6, 7, 9)
print(type(tupleObj)) # <class 'tuple'>

new1 = type('')
print(type(new1)) # <class 'type'> 





print('========================== bytes() ==========================')
x = bytes(4)
print(x) # b'\x00\x00\x00\x00'





print('========================== bytes()  with  str() ==========================')
# Syntax: str(object, encoding, errors)

print(str('A1323')) # A1323
b = bytes('pythön', encoding='utf-8') # The bytes() function returns a bytes object.
print(str(b, encoding='ascii', errors='ignore')) # pythn # because this character   ö   is ot in ascii code

# Note:
# errors='ignore' helps interpreter to ignore when it found a non Ascii charact
# if you want use encoding and errors parameter with function str then the string you are using it should be changed to bytes first using  bytes()  funciton






print('========================== sum() ==========================')

# sum function will calculate all this value that is in the list or tuple or set
# Syntax: sum([iterable], start)

num = [2.5, 3, 4, -5]
numSum = sum(num) 
print(numSum) # 4.5
numSum = sum(num, 20) # adding value to the list by just using comma (,) for typing next value for the list
print(numSum) # 24.5



num = (2.5, 3, 4, -5)
numSum = sum(num) 
print(numSum) # 4.5
numSum = sum(num, 20) # adding value to the list
print(numSum) # 24.5




num = {2.5, 3, 4, -5}
numSum = sum(num) 
print(numSum) # 4.5
numSum = sum(num, 20) # adding value to the list
print(numSum) # 24.5





print('========================== sorted() ==========================')
# The sorted() function returns a sorted list of the specified iterable object.
# Syntax: sorted(iterable, key, reverse)

sampleObj = (3, 6, 8, 2, 5, 8, 10) # tuple
print(sorted(sampleObj)) # [2, 3, 5, 6, 8, 8, 10] # we change it to list
print(sorted(sampleObj, reverse = True)) # [10, 8, 8, 6, 5, 3, 2] # we change it to list and reverse the sort using parameter    reverse
sampledict = {'a':'sss','g':'wq','t':2} # dictionary object
print(sorted(sampledict)) # ['a', 'g', 't'] # we change it to list
# print(sorted(sampledict, key = len)) # ['a', 'g', 't'] # we change it to list # using   key   parameter allow us to just print the key but by default is actually just print the key 




print('========================== different way to print something ========================== ')
print("line 1 "
      "line 2 "
      "line 3 ") # line 1 line 2 line 3




print('========================== oct() ========================== ')
# The oct() function converts an integer into an octal string. Octal strings in Python are prefixed with 0o .
# Syntax: oct(number)
# link: https://www.rapidtables.com/convert/number/decimal-to-octal.html?x=32 # online converting decimal to octal

print("The octal representation of 32 is " + oct(32)) # 0o40 # changing 32 to octal
print("The octal representation of the"
" ascii value of 'A' is " + oct(ord('A'))) # 0o101 # changing A to octal
print("The octal representation of the binary" " of 32 is " + oct(100000)) # 0o303240 # changing 100000 to octal
print("The octal representation of the binary"
                " of 23 is " + oct(0x17)) # 0o27 # changing 0x17 to octal # ???




print('========================== pow() ========================== ')
# The pow() function returns the value of x to the power of y (xy). If a third parameter is present, it returns x to the power of y, modulus z.
# Syntax: pow(num1,num2)

print(pow(2,-3)) # 0.125 # 2^-3 = 0.125
print(pow(2,4.5)) # 22.627416997969522 # 2^4.5 = 22.627416997969522
print(pow(3,0)) # 1 # 3^0 = 1




print('========================== read() ========================== ')
# The read() method returns the specified number of bytes from the file. Default is -1 which means the whole file.
# Syntax: 
    # variable_name = open(file.extension, mode)
    # variable_name.read()
    
f = open("myFile.txt", "r") #  r  read mode
print(f.read()) 
'''
hello world
welcome to 30 days of python
''' 



print('========================== map() ========================== ')
# map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
# Syntax: 
    # variable_name = map(fun, [Iterable])
    # 

numList = (11, 21, 13, 41)
res = map(lambda x: x + x, numList) # we use parameter     lambda x: x + x or x * x or anything   to work with your tuple or list or set
print(res) # <map object at 0x7fb481fba400> # none readable format but this is actually the result but if you want see the actuall result of your work use   list()   function 
print(list(numList)) # [11, 21, 13, 41]
print(list(res)) # [22, 42, 26, 82]  # 11 + 11, 21 + 21, 13 + 13, 41 + 41




print('========================== max() ========================== ')
# using max() function to find the biggest number in the list or tuple or set
# Syntax: max(iterable) or max(num1,num2…)

num = [11, 13, 12, 15, 14]
print('Maximum is:', max(num)) # Maximum is: 15 # which one is biggest number  ( 11  13  12  15  14 ) ? 15




print('========================== min() ========================== ')
# using min() function to find the minimum number in the list or tuple or set
# Syntax: min([iterable])

print(min(2,5, 3, 1, 0, 99)) # 0
sampleObj = ['B','a','t','A'] # A # because it have number 65 in ascii table but (a) small has number 97 in ascii table
print(min(sampleObj))


'''
ASCII Table
Dec  = Decimal Value
Char = Character

'5' has the int value 53
if we write '5'-'0' it evaluates to 53-48, or the int 5
if we write char c = 'B'+32; then c stores 'b'


Dec  Char                           Dec  Char     Dec  Char     Dec  Char
---------                           ---------     ---------     ----------
  0  NUL (null)                      32  SPACE     64  @         96  `
  1  SOH (start of heading)          33  !         65  A         97  a
  2  STX (start of text)             34  "         66  B         98  b
  3  ETX (end of text)               35  #         67  C         99  c
  4  EOT (end of transmission)       36  $         68  D        100  d
  5  ENQ (enquiry)                   37  %         69  E        101  e
  6  ACK (acknowledge)               38  &         70  F        102  f
  7  BEL (bell)                      39  '         71  G        103  g
  8  BS  (backspace)                 40  (         72  H        104  h
  9  TAB (horizontal tab)            41  )         73  I        105  i
 10  LF  (NL line feed, new line)    42  *         74  J        106  j
 11  VT  (vertical tab)              43  +         75  K        107  k
 12  FF  (NP form feed, new page)    44  ,         76  L        108  l
 13  CR  (carriage return)           45  -         77  M        109  m
 14  SO  (shift out)                 46  .         78  N        110  n
 15  SI  (shift in)                  47  /         79  O        111  o
 16  DLE (data link escape)          48  0         80  P        112  p
 17  DC1 (device control 1)          49  1         81  Q        113  q
 18  DC2 (device control 2)          50  2         82  R        114  r
 19  DC3 (device control 3)          51  3         83  S        115  s
 20  DC4 (device control 4)          52  4         84  T        116  t
 21  NAK (negative acknowledge)      53  5         85  U        117  u
 22  SYN (synchronous idle)          54  6         86  V        118  v
 23  ETB (end of trans. block)       55  7         87  W        119  w
 24  CAN (cancel)                    56  8         88  X        120  x
 25  EM  (end of medium)             57  9         89  Y        121  y
 26  SUB (substitute)                58  :         90  Z        122  z
 27  ESC (escape)                    59  ;         91  [        123  {
 28  FS  (file separator)            60  <         92  \        124  |
 29  GS  (group separator)           61  =         93  ]        125  }
 30  RS  (record separator)          62  >         94  ^        126  ~
 31  US  (unit separator)            63  ?         95  _        127  DEL
'''





print('========================== range() ========================== ')
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
# Syntax: range(start, stop, step)

res = 1
# range(1, 10) = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) 
# range(1, 10, 2) = (1, 3, 5, 7, 9)
'''
range(4)        # [0, 1, 2, 3] 0 through 4, excluding 4
range(1, 4)     # [1, 2, 3] 1 through 4, excluding 4
range(1, 10, 2) # [1, 3, 5, 7, 9] 1 through 10, counting by 2s
'''


for i in range(1, 10, 2): 
       res = res * i 
       '''
       1 * 1 = 1
       1 * 3 = 3
       3 * 5 = 15
       15 * 7 = 105
       105 * 9 = 945
       
       '''
       print(res) # 1  3  15  105  945

print("multiplication of first 10 natural number :", res) # multiplication of first 10 natural number : 945





print('========================== reversed() ========================== ')
'''
# To reverse a list use simply: reverse() method

# Example 
list = [1, 2, 3]
list.reverse()

# Output
[3, 2, 1]
'''
# Syntax: reversed([sequence] or [collection])
tupleObj=(3, 4, 6, 7, 9)
for i in reversed(tupleObj): 
       print(i, end=' ') # 9 7 6 4 3 #    end = "end with ..."    parameter use to put something to the end of this value that back to for loop and using   print()   function to using feature   end   parameter for print the value in one line
    #    print(i) 
    #    '''
    #    9
    #    7
    #    6
    #    4
    #    3
    #    ''' 



print('\n========================== help()   ( we don''t use help ) ========================== ')
# we don't use help 

# printing all python reserved words using   help('keywords')
# help('keywords')

'''
Here is a list of the Python keywords.  Enter any keyword to get more help.

False               break               for                 not
None                class               from                or
True                continue            global              pass
__peg_parser__      def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
'''

# giving information about string using  help(str)
# help(str)
'''
...
...
'''


# give information about string using dir(str)
# dir(str)

'''
['__add__', 
'__class__', 
'__contains__', 
'__delattr__', 
'__dir__', 
'__doc__', 
'__eq__', 
'__format__', 
'__ge__', 
'__getattribute__', 
'__getitem__', 
'__getnewargs__', 
'__gt__', 
'__hash__', 
'__init__', 
'__init_subclass__', 
'__iter__', 
'__le__', 
'__len__', 
'__lt__', 
'__mod__', 
'__mul__', 
'__ne__', 
'__new__', 
'__reduce__', 
'__reduce_ex__', 
'__repr__', 
'__rmod__', 
'__rmul__', 
'__setattr__', 
'__sizeof__', 
'__str__', 
'__subclasshook__', 
'capitalize', 
'casefold', 
'center', 
'count', 
'encode', 
'endswith', 
'expandtabs', 
'find', 
'format', 
'format_map', 
'index', 
'isalnum', 
'isalpha', 
'isascii', 
'isdecimal', 
'isdigit', 
'isidentifier', 
'islower', 
'isnumeric', 
'isprintable',
'isspace',
'istitle',
'isupper',
'join',
'ljust',
'lower',
'lstrip',
'maketrans',
'partition',
'removeprefix',
'removesuffix',
'replace',
'rfind',
'rindex',
'rjust',
'rpartition',
'rsplit',
'rstrip',
'split',
'splitlines',
'startswith',
'strip',
'swapcase',
'title',
'translate',
'upper',
'zfill',
]
 
'''


print('========================== reversed() ========================== ')
