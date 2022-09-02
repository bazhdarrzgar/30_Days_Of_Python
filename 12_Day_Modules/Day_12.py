print('========================== Modules ==========================')
print('\n\n\n')
print('========================== Create a Module ==========================')

'''
# Syntax

## create file for putting this code inside

def function_name(parameter, parameter, ....):
  return parameter + parameter + ....


## create other file to put this code inside and run the code inside it

import file_name

print(file_name.function_name(value, value, ....))

'''

# mymodule.py
# simple function that have 2 parameter and we return value of that parameter
def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname





# main.py
# we are using (mymodule) to tell this file that i use other file resource that name is mymodule to return value from it when i call it or calling it with taking value to it
import mymodule

print(mymodule.generate_full_name('Asabeneh', 'Yetayeh')) # Asabeneh Yetayeh



'''
# calling value from other resource

import file_name

file_name.code.....

'''



print('========================== Import Functions from a Module ==========================')
'''
# Syntax

from file_name import variable_name, function_name, tuple_name, and ....

'''


# mymodule.py file

# simple function that have 2 parameter and we return value of this parameter
def generate_full_name(firstname, lastname):
    space = ' '
    fullname = firstname + space + lastname
    return fullname

# other function that have 2 parameter also i return value of this two parameter
def sum_two_nums(num1, num2):
    return num1 + num2

# simple integer
gravity = 9.81

# tuple
person = {
    "firstname": "Asabeneh",
    "age": 250,
    "country": "Finland",
    "city": 'Helsinki'
}





# main.py file

# from file (mymodule) we call this variable and function and tuple for there value or calling it by putting value to it
# generate_full_name # function
# sum_two_nums # function
# person # variable
# gravity # tuple
'''
# Note

we use this technique of calling resource file from other place like we do with variable and tuple and ... in this example
because i don't want specific the file_name before this variable and function and ...

## without specify the variable and function and  ... when import the file_name



import mymodule

print(mymodule.generate_full_name('Asabneh','Yetayeh')) # Asabneh Yetayeh

print(mymodule.sum_two_nums(1,9)) # 10

mass = 100;
weight = mass * mymodule.gravity # 100 * 9.81
print(weight) # 981.0

print(mymodule.person['firstname']) # Asabeneh





## with specify the variable and function and  ... when import the file_name



from mymodule import generate_full_name, sum_two_nums, person, gravity

print(generate_full_name('Asabneh','Yetayeh')) # Asabneh Yetayeh

print(sum_two_nums(1,9)) # 10

mass = 100;
weight = mass * gravity # 100 * 9.81
print(weight) # 981.0

print(person['firstname']) # Asabeneh

'''

from mymodule import generate_full_name, sum_two_nums, person, gravity

print(generate_full_name('Asabneh','Yetayeh')) # Asabneh Yetayeh

print(sum_two_nums(1,9)) # 10

mass = 100;
weight = mass * gravity # 100 * 9.81
print(weight) # 981.0

print(person['firstname']) # Asabeneh


'''
Asabneh Yetayeh
10
981.0
Asabeneh
'''



print('========================== Import Built-in Modules ==========================')
print('\n\n\n')
print('========================== OS Module ==========================')

import os
import pprint

# # Getting current working directory
# print(os.getcwd())
'''
/home/soyansoon/PycharmProjects/helloworld_final/3
'''




# # Executing a shell command
# os.system('ls')
'''
main1.py
main.py
mymodule.py
__pycache__
'''


# # # Get the users environment
#
# # print(os.environ)
# # pprint.pprint(dict(os.environ), width = 1)
# env_var = os.environ
# pprint.pprint(dict(env_var), width=1)
'''
...
...
...
'''



# # specify the environment variable using this bracket [] to put environment variable inside
# home = os.environ['HOME']
# print("HOME:", home)
#
# java_home = os.environ.get('JAVA_HOME')
# print("JAVA_HOME:", java_home)
'''
HOME: /home/soyansoon
JAVA_HOME: None
'''


# # Creating a directory
# os.mkdir('directory_name')




#  # Changing the current directory
# os.chdir(r'/home/soyansoon/Documents/test')




# # changing director with getting (pwd (get this path that i am in)) command after that
# os.chdir('/home/soyansoon/Documents/test')
#
# # verify the path using getcwd()
# cwd = os.getcwd()
#
# # print the current directory
# print("Current working directory is:", cwd)
'''
Current working directory is: /home/soyansoon/Documents/test
'''



# # Return the real group id of the current process.
# print(os.getgid())
'''
1000
'''



# # # do this with sudo previledge
# # # changing group id using   os.setgid(number..)
# gid = 23
# os.setgid(gid)
#
# gid = os.getgid()
# print("Group id of the current process:", gid)
'''
Group id of the current process: 1000
Group id changed
Group id of the current process: 23
'''



# # Return the current process’s user id.
# print(os.getuid()) # 1000



# # do this with sudo previledge
# # changing this current process for the user id using    os.setuid(number...)
# uid = 1500
# os.setuid(uid)
# print("Real user ID changed: ", os.getuid())
'''
Real user ID changed: 1500
'''



# # Returns the real process ID of the current process.
# print(os.getpid()) # 29358




# # Set the current numeric umask and return the previous umask.
# print(os.umask(18))
'''
2
'''

# print(os.umask(0o777))
'''
2
'''



# # Return information identifying the current operating system.
# print(os.uname())
'''
posix.uname_result(sysname='Linux', nodename='soyansoon-Blade', release='5.15.0-46-generic', version='#49~20.04.1-Ubuntu SMP Thu Aug 4 19:15:44 UTC 2022', machine='x86_64')
'''



# # Change the root directory of the current process to path.
# # Set current root path to /Geeks/gfg
# os.chroot("/Geeks/gfg")




# # Return a list of the entries in the directory given by path.
# print(os.listdir('/home/soyansoon/Documents'))
'''
['100DaysOfCode', 'Program', 'roll_back', 'pc city', 'WPS Capture', 'malware room', 'note.md', 'password_*_*', 'Test_Program', 'ViberDownloads', 'bashdar rzgar.docx', 'php-crash-course-2020', '.note.md.swp', 'my_project', 'github', 'q', 'windows 10 format', 'pdf_for_lesson', 'project web.md', 'Trash', 'MyProgram_And_Note', 'hacking_tools', 'test', 'VsCode', 'ali_abdulla.md', '.vscode', '.note.md.swo', 'social-engineer-toolkit', 'oh-my-fish', 'best book', 'Ryzen 7000.md', 'Study', 'my font style.md', 'test.md']
'''

# dir_list = os.listdir('/')
# print(dir_list)
'''
Files and directories in ' / ' :
['cdrom', 'libx32', 'boot', 'sbin', 'mnt', 'lost+found', 'usr', 'lib32', 'var', 'directory-to-open', 'lib', '0', 'srv', 'home', 'snap', 'etc', 'opt', 'sys', 'run', 'media', 'bin', 'tmp', 'crud', 'dev', 'root', 'lib64', 'swapfile', 'proc']
'''




# # Create a directory named path with numeric mode.
# os.mkdir('directory name')




# # Recursive directory creation function.
# os.makedirs('hi')




# # Remove (delete) the file using path of the file.
# os.remove('file1.py')




# # Remove directories recursively.
# os.removedirs('hi')




# # Rename the file or directory src to dst.
# # src path means source path with name of the file or folder
# # dst path means destination path with name of the file or folder
# # os.rename(src_path, dst_path)
# os.rename('file1.py', 'file2.py')




# # Remove (delete) empty directory using path of the folder.
# os.rmdir('hi')

# os.rmdir('/home/soyansoon/Documents/test/hi')





print('========================== Sys Module ==========================')

import sys

print(sys.argv[0], sys.argv[1], sys.argv[2])  # main.py Asabeneh 30DaysOfPython
'''
python3 main.py Asabeneh 30DaysOfPython

main.py Asabeneh 30DaysOfPython

'''

print(sys.argv[0]) # main.py
'''
python3 main.py Asabeneh 30DaysOfPython

main.py

'''

print(sys.argv[1]) # Asabeneh
'''
python3 main.py Asabeneh 30DaysOfPython

Asabeneh

'''

print(sys.argv[2]) # 30DaysOfPython
'''
python3 main.py Asabeneh 30DaysOfPython

30DaysOfPython

'''

print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))
'''
python3 main.py Asabeneh 30DaysOfPython

Welcome Asabeneh. Enjoy  30DaysOfPython challenge!

'''



print('========================== Sys Module ==========================')

import sys
# Python version you are using
print(sys.version)
'''
3.8.10 (default, Jun 22 2022, 20:18:18) 
[GCC 9.4.0]
'''



# Informantion
print(sys.version_info) # sys.version_info(major=3, minor=8, micro=10, releaselevel='final', serial=0)



# operating system name
print(sys.platform) # linux




# to exit sys
msg = "bye bye"
sys.exit(msg)




# in this example you can see that first one is print but other not
print(sys.maxsize)
sys.exit()
print(sys.path)
print(sys.version)
'''
9223372036854775807
'''



# another example
age = 17

if age < 18:
    # exits the program
    sys.exit("Age less than 18")
else:
    print("Age is not less than 18")




# # To know the largest integer variable it takes
print(sys.maxsize) # 9223372036854775807



# # To know environment path
print(sys.path) 
'''
['/home/soyansoon/PycharmProjects/helloworld_final/3', '/home/soyansoon/PycharmProjects/helloworld_final', '/usr/lib/python38.zip', '/usr/lib/python3.8', '/usr/lib/python3.8/lib-dynload', '/home/soyansoon/.local/lib/python3.8/site-packages', '/usr/local/lib/python3.8/dist-packages', '/usr/lib/python3/dist-packages']

'''






print('========================== Statistics Module ==========================')
# statistics package use for finding ( means, mode, mediam, stdev ( standard devition ))

# from statistics import * # importing all the statistics modules

from statistics import mean, mode, median, stdev # or you can just import this package that you want use

# list, wright answear
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]

print(mean(ages))       # 21.09090909090909
print(median(ages))     # 22
print(mode(ages))       # 20
print(stdev(ages))      # 6.106628291529549



print('\n\n')
# tuple, wright answear
ages = (20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26)

print(mean(ages))       # 21.09090909090909
print(median(ages))     # 22
print(mode(ages))       # 20
print(stdev(ages))      # 6.106628291529549



print('\n\n')
# Note: Don't use set for finding the mean and mode and .... because it take you wrong answear why ? i don't know why
ages = {20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26}

print(mean(ages))       # 20.571428571428573
print(median(ages))     # 23
print(mode(ages))       # 4
print(stdev(ages))      # 7.5687326736854885




print('========================== Math Module ==========================')

import math

# pi = π
print(math.pi)           # 3.141592653589793, pi constant
# sqrt = square root
print(math.sqrt(2))      # 1.4142135623730951, square root
# pow = power
print(math.pow(2, 3))    # 8.0, exponential function
# floor = remove the number after dot (.)
print(math.floor(9.81))  # 9, rounding to the lowest
# ceil = take the number to the nearest number possible ( 0.5 = 0   0.5(more) = 1   0.5(less) = 0 )
print(math.ceil(9.81))   # 10, rounding to the highest
# log10 = log of the number with 10 is the base
print(math.log10(100))   # 2, logarithm with 10 as base




# we importing just pi from package math to not use   (math.pi)   every time
from math import pi
print(pi) # 3.141592653589793





# we import this function from package math because i don't want use name of math before each of the function
from math import pi, sqrt, pow, floor, ceil, log10

print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(log10(100))         # 2.0




# we are now importing all the function from package math using start  ( * )
from math import *

print(pi)                  # 3.141592653589793, pi constant
print(sqrt(2))             # 1.4142135623730951, square root
print(pow(2, 3))           # 8.0, exponential
print(floor(9.81))         # 9, rounding to the lowest
print(ceil(9.81))          # 10, rounding to the highest
print(log10(100))          # 2.0





# importing function pi from package math as PI means instaid calling   (pi)   for using it you can use   (PI)   inside of that this customizable you can calling pi as anything you want
from math import pi as PI
print(PI) # 3.141592653589793





print('========================== String Module ==========================')

# this package is use for calling anything that is string but in organize way means
# ascii_letters  # is organized function that just contain ascii code
# digits         # is organized function that just contain digits (number)
# punctuation    # is organized function that just contain punctuation letters  # https://en.wikipedia.org/wiki/Punctuation

import string

print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~




print('========================== Random Module ==========================')

# random package is use for make random number if it is integer or float or bytes or bits or ...
# from random package we are using   random   and   randint   function
from random import random, randint

print(random())   # make random number between 0 and 0.9999...
print(randint(5, 20)) # make random integer number between [5, 20] inclusive
