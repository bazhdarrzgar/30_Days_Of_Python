from ensurepip import version


print('========================== Python PIP - Python Package Manager ==========================')

# Installing (pip) using (pip)

'''
# 1. install python

# 2. install pip

pip install pip

'''


# check version of (pip)

'''
pip --version

'''


# Installing packages using (pip)
# # in this example we install (numpy)

'''
# what is numpy ?

    * NumPy is the fundamental package for scientific computing with Python.
    
    
# installing numpy
    
    pip install numpy

'''


# # some example about numpy if you like

'''

# check the version of numpy

numpy.version.version

# change list or tuple or ... to array

numpy_array = numpy.array(list...)

# calling length of the numpy array

len(numpy_array)

# work with value of array numpy

numpy_array + value
numpy_array / value
numpy_array * value
numpy_array - value
numpy_array ** value
numpy_array % value
...

'''

import numpy

print(numpy.version) # <module 'numpy.version' from '/home/soyansoon/.local/lib/python3.8/site-packages/numpy/version.py'>

print(numpy.version.version) # 1.21.3


lst = [1, 2, 3, 4, 5]
print(lst) # [1, 2, 3, 4, 5]

np_arr = numpy.array(lst)
print(np_arr) # [1 2 3 4 5]



print(len(np_arr)) # 5



print(np_arr * 2) # [ 2  4  6  8 10]
# [1*2  2*2  3*2  4*2  5*2] = [ 2  4  6  8 10]

print(np_arr + 2) # [3 4 5 6 7]
# [1+2  2+2  3+2  4+2  5+2] = [3 4 5 6 7]





# # another package is (panda)

'''
# Pandas is an open source library providing high-performance, easy-to-use
data structures and data analysis tools for the Python programming language.

pip install pandas

'''

import pandas





# # another package is (webbrowser) this is help us to open any website.
'''

# importing (webbrowser)

import webbrowser


# open link in different tab

webbrowser.open_new_tab(url..)

'''

import webbrowser

url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

# opens the above list of websites in a (different tab)
# first put all the data of the list to variable for loop
for url in url_lists:
    # second is put all this data one by one to the function ( open_new_tab() ) for open this data in different tab in browser
    # ( open_new_tab() ) function provided by (webbrowser) module
    webbrowser.open_new_tab(url)





# Uninstalling Packages

'''
pip uninstall package_name

'''



# List all the Packages installed in your environment

'''
pip list

'''



# Show deatail about Package that installed in your environment

'''
pip show package_name

'''


# show more detail information about this package that installed in your environment

'''
# word verbose is mean ( using more words than necessary to express thought )
pip show --verbose package_name

'''




print('========================== PIP Freeze ==========================')
# # show you the (name and version) of package that install your environment system

# # it is suitable to use it in a requirements file. A requirements.txt file is a file that should contain all the installed Python packages in a Python project.

'''
pip freeze

'''




print('========================== Reading from URL ==========================')

'''
# request module: use for read from a website using url or from an API. API stands for Application Program Interface.
It is a means to exchange structured data between servers primarily as json data.

# install the ( requests ) package

pip install requests


# importing the ( requests ) package

import requests


# get the (response) from the url or server using ( get() ) function

response = requests.get(url...)


# get just the (number of request) from the server using ( status_code ) keyword with ( get() ) function

response.status_code


# get the (header information) about target website using ( headers ) keyword with ( get() ) function

response.headers


# get the content of the website not code of the website using ( text ) keyword with ( get() ) function

response.text

'''


import requests

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt' # text from a website

response = requests.get(url) # opening a network and fetching a data

print(response) # <Response [200]>

print(response.status_code) # 200

print(response.headers)
# {'date': 'Wed, 07 Sep 2022 14:18:15 GMT', 'last-modified': 'Fri, 07 Nov 2003 05:51:11 GMT', 'etag': '"17e9-3cb82080711c0;50c0b26855880', 'accept-ranges': 'bytes', 'cache-control': 'max-age=31536000', 'expires': 'Thu, 07 Sep 2023 14:18:15 GMT', 'vary': 'Accept-Encoding,Origin', 'content-encoding': 'gzip', 'access-control-allow-origin': '*', 'content-length': '1616', 'content-type': 'text/plain', 'x-backend': 'ssl-mirrors', 'x-request-id': '6318a8270433a1f4', 'strict-transport-security': 'max-age=15552000; includeSubdomains; preload', 'content-security-policy': 'upgrade-insecure-requests'}

print(response.text) # gives all the text from the page





'''

# get the response information using   ( get() )   function with request module

response = request.get(url...)

# get just the number of respose from the server

response.status_code

# change this data that come to us to json

response.json

# calling the number of row in my json data

response.json[:number_of_row] # calling one row

# Example   ( response.json[:1] ) # calling one row

'''

import requests
import pprint

url = 'https://restcountries.com/v3.1/all'  # countries api
response = requests.get(url)  # opening a network and fetching a data

print(response) # <Response [200]>

print(response.status_code)  # 200

countries = response.json()
# pprint.pprint(countries) # alot of data as json
pprint.pprint(countries[:1])  # we call only one country
'''
[{'altSpellings': ['FI',
                   'Suomi',
                   'Republic of Finland',
                   'Suomen tasavalta',
                   'Republiken Finland'],
  'area': 338424.0,
  'borders': ['NOR', 'SWE', 'RUS'],
  'capital': ['Helsinki'],
  'capitalInfo': {'latlng': [60.17, 24.93]},
  'car': {'side': 'right', 'signs': ['FIN']},
  'cca2': 'FI',
  'cca3': 'FIN',
  'ccn3': '246',
  'cioc': 'FIN',
  'coatOfArms': {'png': 'https://mainfacts.com/media/images/coats_of_arms/fi.png',
                 'svg': 'https://mainfacts.com/media/images/coats_of_arms/fi.svg'},
  'continents': ['Europe'],
  'currencies': {'EUR': {'name': 'Euro', 'symbol': '€'}},
  'demonyms': {'eng': {'f': 'Finnish', 'm': 'Finnish'},
               'fra': {'f': 'Finlandaise', 'm': 'Finlandais'}},
  'fifa': 'FIN',
  'flag': '🇫🇮',
  'flags': {'png': 'https://flagcdn.com/w320/fi.png',
            'svg': 'https://flagcdn.com/fi.svg'},
  'gini': {'2018': 27.3},
  'idd': {'root': '+3', 'suffixes': ['58']},
  'independent': True,
  'landlocked': False,
  'languages': {'fin': 'Finnish', 'swe': 'Swedish'},
  'latlng': [64.0, 26.0],
  'maps': {'googleMaps': 'https://goo.gl/maps/HjgWDCNKRAYHrkMn8',
           'openStreetMaps': 'openstreetmap.org/relation/54224'},
  'name': {'common': 'Finland',
           'nativeName': {'fin': {'common': 'Suomi',
                                  'official': 'Suomen tasavalta'},
                          'swe': {'common': 'Finland',
                                  'official': 'Republiken Finland'}},
           'official': 'Republic of Finland'},
  'population': 5530719,
  'postalCode': {'format': '#####', 'regex': '^(?:FI)*(\\d{5})$'},
  'region': 'Europe',
  'startOfWeek': 'monday',
  'status': 'officially-assigned',
  'subregion': 'Northern Europe',
  'timezones': ['UTC+02:00'],
  'tld': ['.fi'],
  'translations': {'ara': {'common': 'فنلندا', 'official': 'جمهورية فنلندا'},
                   'bre': {'common': 'Finland', 'official': 'Republik Finland'},
                   'ces': {'common': 'Finsko', 'official': 'Finská republika'},
                   'cym': {'common': 'Finland',
                           'official': 'Republic of Finland'},
                   'deu': {'common': 'Finnland',
                           'official': 'Republik Finnland'},
                   'est': {'common': 'Soome', 'official': 'Soome Vabariik'},
                   'fin': {'common': 'Suomi', 'official': 'Suomen tasavalta'},
                   'fra': {'common': 'Finlande',
                           'official': 'République de Finlande'},
                   'hrv': {'common': 'Finska', 'official': 'Republika Finska'},
                   'hun': {'common': 'Finnország',
                           'official': 'Finn Köztársaság'},
                   'ita': {'common': 'Finlandia',
                           'official': 'Repubblica di Finlandia'},
                   'jpn': {'common': 'フィンランド', 'official': 'フィンランド共和国'},
                   'kor': {'common': '핀란드', 'official': '핀란드 공화국'},
                   'nld': {'common': 'Finland',
                           'official': 'Republiek Finland'},
                   'per': {'common': 'فنلاند', 'official': 'جمهوری فنلاند'},
                   'pol': {'common': 'Finlandia',
                           'official': 'Republika Finlandii'},
                   'por': {'common': 'Finlândia',
                           'official': 'República da Finlândia'},
                   'rus': {'common': 'Финляндия',
                           'official': 'Финляндская Республика'},
                   'slk': {'common': 'Fínsko', 'official': 'Fínska republika'},
                   'spa': {'common': 'Finlandia',
                           'official': 'República de Finlandia'},
                   'swe': {'common': 'Finland',
                           'official': 'Republiken Finland'},
                   'urd': {'common': 'فن لینڈ', 'official': 'جمہوریہ فن لینڈ'},
                   'zho': {'common': '芬兰', 'official': '芬兰共和国'}},
  'unMember': True}]
  
'''






print('========================== Creating a Package ==========================')

# mypackage/greet.py

def greet_person(firstname, lastname):
    # f   flag means i use variable inside string and the variable is represented inside this bracket   {variable_name}
    print(f'{firstname} {lastname}, welcome to 30DaysOfPython Challenge!')







# mypackage/arithmatic.py

# start (*) means any value is send to this function put it in (args) parameter
def add_numbers(*args):
    # we declared (total) variable outside the for loop because i want return the value of this variable to the function after done there work in for loop
    total = 0
    for num in args:
        total += num
        # total = total + num

    print(total)


def subtract(a, b):
    print(a - b)


# accept only 2 value
def multiple(a, b):
    print(a * b)


# accept only 2 value
def division(a, b):
    print(a / b)


# accept only 2 value
def remainder(a, b):
    print(a % b)


# accept only 2 value
def power(a, b):
    print(a ** b)







# mypackage/__init__.py

'''
# The folder structure of your package should look like this:

─ mypackage
    ├── __init__.py
    ├── arithmetic.py
    └── greet.py

'''

# from folder (mypackage) calling file (arithmetic)
from mypackage import arithmetic

arithmetic.add_numbers(1, 2, 3, 5)
# 11

'''
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print(total)

add_numbers(1, 2, 3, 5) # 11

'''

arithmetic.subtract(5, 3)
# 2

'''
def subtract(a, b):
    print(a - b)

subtract(5, 3) # 2

'''

arithmetic.multiple(5, 3)
# 15

'''
def multiple(a, b):
    print(a * b)

multiple(5, 3)

'''

arithmetic.division(5, 3)
# 1.6666666666666667

'''
def division(a, b):
    print(a / b)

division(5, 3) # 1.6666666666666667

'''

arithmetic.remainder(5, 3)
# 2

'''
def remainder(a, b):
    print(a % b)

remainder(5, 3) # 2

'''

arithmetic.power(5, 3)
# 125

'''
def power(a, b):
    print(a ** b)
    
power(5, 3)

'''




from mypackage import greet

greet.greet_person('Asabeneh', 'Yetayeh') # 'Asabeneh Yetayeh, welcome to 30DaysOfPython Challenge!'

'''
def greet_person(firstname, lastname):
    return f'{firstname} {lastname}, welcome to 30DaysOfPython Challenge!'

print(greet_person('Asabeneh', 'Yetayeh')) # 'Asabeneh Yetayeh, welcome to 30DaysOfPython Challenge!'

'''






print('========================== Further Information About Packages ==========================')

'''
* Database

  * SQLAlchemy or SQLObject - Object oriented access to several different database systems

    * pip install SQLAlchemy


* Web Development

  * Django - High-level web framework.

    * pip install django

  * Flask - micro framework for Python based on Werkzeug, Jinja 2. (It's BSD licensed)
  
    * pip install flask


* HTML Parser

  * Beautiful Soup - HTML/XML parser designed for quick turnaround projects like screen-scraping, will accept bad markup.

    * pip install beautifulsoup4

  * PyQuery - implements jQuery in Python; faster than BeautifulSoup, apparently.

  
* XML Processing

  * ElementTree - The Element type is a simple but flexible container object, designed to store hierarchical data structures, such as simplified XML infosets, in memory. --Note: Python 2.5 and up has ElementTree in the Standard Library


* GUI

  * PyQt - Bindings for the cross-platform Qt framework.
  * TkInter - The traditional Python user interface toolkit.


* Data Analysis, Data Science and Machine learning

  * Numpy: Numpy(numeric python) is known as one of the most popular machine learning library in Python.
  
  * Pandas: is a data analysis, data science and a machine learning library in Python that provides data structures of high-level and a wide variety of tools for analysis.
  
  * SciPy: SciPy is a machine learning library for application developers and engineers. SciPy library contains modules for optimization, linear algebra, integration, image processing, and statistics.
  
  * Scikit-Learn: It is NumPy and SciPy. It is considered as one of the best libraries for working with complex data.
  
  * TensorFlow: is a machine learning library built by Google.
  
  * Keras: is considered as one of the coolest machine learning libraries in Python. It provides an easier mechanism to express neural networks. Keras also provides some of the best utilities for compiling models, processing data-sets, visualization of graphs, and much more.

  
* Network:

    * requests: is a package which we can use to send requests to a server(GET, POST, DELETE, PUT)

      * pip install requests

'''



