print('========================== Python Web Scraping ==========================')
# Web scraping is the process of extracting and collecting data from websites and storing it on a local machine or in a database.

'''
pip install requests
pip install beautifulsoup4

'''


import requests
from bs4 import BeautifulSoup





'''
#  Syntax

# # import requests module

import requests

# # fetch the data from url using   get()   function
# # Note: the output is normal Response if it is (200) means success of fetching data if it is (404) means unsuccess

requests.get(url...)

# # get just back the number 200 for success or 404 for unsuccess by just using ( status_code ) keyword with get() function

requests.get(url...).status_code
'''

import requests

url = 'https://archive.ics.uci.edu/ml/datasets.php'

# Lets use the requests get method to fetch the data from url
response = requests.get(url)
print(response) # <Response [200]>

# lets check the status
status = response.status_code
print(status) # 200 # means the fetching was successful





'''
# # fetching data of url in the server using (requests) module

import requests
response = requests.get(url...)


# # get the content of the website using (content) keyword

content = response.content


# # beautify this data that we get from content of the website using (BeautifulSoup) module

import BeautifulSoup
soup = BeautifulSoup(content, 'html.parser') # if you parse each tag of the website then ( 'html.parser' ) is good choice


# # get the title of the webiste using (title) keyword

soup.title


# # get just clean text of title in the website using ( title.text() )

soup.title.text()


# # get anything that inside the body of the website using (body) keyword

soup.body


# # get the status code of the website if 200 means success of fetching data if it is 404 means unsuccess of fetching data from the website using (status_code)

response.status_code

'''

import requests
from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)
content = response.content # we get all the content from the website
soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
print(soup.body) # gives anything inside  the body of the page
print(response.status_code)

# 'table' # we are finding all the content that is inside the (table) tag
# 'cellpadding' : '3' # we are only targetting 3 cell of the table 
# all the data is come to as in one row and none format
tables = soup.find_all('table', {'cellpadding' : '3'})
table = tables[0] # all the data is provided in one row this is why we just specify the index [0] only # the result is a list, we are taking out data from it
# by using this data that we get, we find all   <tr>   tag and we want find all the tag   <td>   inside this tag
# this is done by using   ( find() )  function with   <tr>  tag and (find_all) keyword with   <td>   tag
# it is mean find    <tr>   tag and find all the tag that is   <td>   tag inside   <tr>   tag
'''
# find
<tr>
    # find_all
    <td></td>
    <td></td>
    <td></td>
</tr>

# find
<tr>
    # find_all
    <td></td>
    <td></td>
    <td></td>
</tr>

# find
<tr>
    # find_all
    <td></td>
    <td></td>
    <td></td>
</tr>

'''
for td in table.find('tr').find_all('td'):
    # in the end we just print this text that we get inside   <td>   tag
    print(td.text)






