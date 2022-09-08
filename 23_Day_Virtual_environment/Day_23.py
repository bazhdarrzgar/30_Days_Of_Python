print('========================== Setting up Virtual Environments ==========================')

'''

# installing   virtualenv  using pip
## pip install virtualenv

asabeneh@Asabeneh:~$ pip install virtualenv




# create a virtual env  ( linux & mac)
## virtualenv venv

asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project\$ virtualenv venv
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project\$ ls
===
venv
===




# create a virtual env  ( windows )
## python -m venv venv

C:\Users\User\Documents\30DaysOfPython\flask_project> python -m venv venv
C:\Users\User\Documents\30DaysOfPython\flask_project> ls
===
venv/
===




# activate the virtual environment ( linux & mac )
## source venv/bin/activate

asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ source venv/bin/activate


# activate the virtual environment ( windows )
## venv\Scripts\activate

C:\Users\User\Documents\30DaysOfPython\flask_project> venv\Scripts\activate




# activate the virtual environment ( windows git bash )
## venv\Scripts\. activate

C:\Users\User\Documents\30DaysOfPython\flask_project> venv\Scripts\. activate




# deactivate the virtual environment
## deactivate

(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython$ deactivate




# after activate the virtual environment you should see venv in front of your bash

(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$




# We are going to do a small flask project so let us install flask package to this project.
## pip install flask

(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ pip install Flask




# type pip freeze to see if flask is installed
## pip freeze

(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ pip freeze

'''