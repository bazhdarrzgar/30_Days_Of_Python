print('========================== Classes and Objects ==========================')


num = 10 # int
print(type(num))
# <class 'int'>

string = 'string' # str # string
print(type(string))
# <class 'str'>

boolean = True # bool # boolean
print(type(boolean))
# <class 'bool'>

lst = [] # list
print(type(lst))
# <class 'list'>

tpl = () # tuple
print(type(tpl))
# <class 'tuple'>

set1 = set() # set
set1 = {1, 2, 3} # set
print(type(set1))
# <class 'set'>

dct = {} # dictionary
dct = {'key': 'value', 'key_1': 'value'} # dict # dictionary
print(type(dct))
# <class 'dict'>






print('========================== Creating a Class ==========================')

'''
# Syntax

class Class_Name:
  ...code problem

'''


class Person:
    # pass menas not error in this block and passed the test
    pass

print(Person) # <class '__main__.Person'>





print('========================== Creating an Object ==========================')

'''
# Syntax

class Class_Name:
  ...code problem

Class_Name()

'''

class Person:
    pass

print(Person) # <class '__main__.Person'> # main class Person is class


# Creating  object for class
p = Person()

print(p) # <__main__.Person object at 0x7fa420310130> # main class Person is an object





print('========================== Class Constructor ==========================')

class Person:
    # self is keyword that use to attach the parameter to the class
    # this is usefull because any value is send to the class the keyword (self) is put it in the parameter (name)

    # The __init__ function is called every time an object is created from a class
    def __init__(self, name):
        # self allows to attach parameter to the class
        self.name = name

p = Person('Asabeneh')
print(p.name)  # Asabeneh
print(p)  # <__main__.Person object at 0x7fdb8f5340a0>




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)  # Object definition

print(p1.name)  # John
print(p1.age)  # 36


class Person:
    # The __init__ function is called every time an object is created from a class
    # the self keyword is attack parameter to the class
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

Person1 = Person("Isabella", 27, "female")
Person2 = Person("Mikkel", 29, "male")

People = [Person1, Person2]
print(People)  # [<__main__.Person object at 0x7fa12067a7f0>, <__main__.Person object at 0x7fa12067a550>] # both of the variable is Object

People = [Person1.name, Person1.age, Person1.gender, Person2.name, Person2.age, Person2.gender]  # putting all the value to the list
print(People)  # ['Isabella', 27, 'female', 'Mikkel', 29, 'male']

print(Person1.name)  # Isabella
print(Person1.age)  # 27
print(Person1.gender)  # female

print(Person2.name)  # Mikkel
print(Person2.age)  # 29
print(Person2.gender)  # male






class Person:
    # __init__ function is called every time the object is created for class for sending value to the class
    # the __init__ function in this case is wait for get value from class to there parameter
    
    # self keyword is attach-value to the parameter
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city


# sending all this value to the class
p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)






print('========================== Object Methods ==========================')

class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city


    # if you use (self) keyword in place of paramter then it is use value of paramter   __init__   function
    # or in another word we call the value from   __init__   funtion to this funciton to put it in the exactl parameter that also we have this parameter in   __init__   function
    # we just use this value for there parameter to make it more readable 
    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'

# send this value to (Person) class
p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
# we also calling the (person_info) function value using object of   Person()  
print(p.person_info()) # Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland





print('========================== Object Default Methods ==========================')

class Person:
    # each parameter can have there own value by using equal ( = ) operator
    def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'


# not value is send to the class ( Person ) just calling the class ( Person ) by creating object for the ( Person ) class under the ( Person ) class name
p1 = Person()
print(p1.person_info()) # Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland.
# override this value that function   __init__   have for there parameter
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info()) # John Doe is 30 years old. He lives in Noman city, Nomanland.





print('========================== Method to Modify Class Default Values ==========================')

class Person:
    # each parameter can have own value by using equal ( = ) operator
    def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        # we are using this declaration variable as list because we want used by other function to send it value to it in this case is function ( add_skill )
        # if we don't declare this variable as list then this error is happen for function ( add_skill ) because it is use this (variable) to send it value
            # AttributeError: 'Person' object has no attribute 'skills'
        self.skills = []

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

    def add_skill(self, skill):
        # self.skills # is calling value of (skills) variable that is inside function   __init__
        # append(skill) # we send value from (skill) parameter to (skills) variable of function   __init__   by using   ( append() ) function
        # ( append() ) funciton will send value to variable (skills) as list
        self.skills.append(skill)


p1 = Person()
# calling the function (person_info) in class  ( Person ) by object p1
print(p1.person_info()) # Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland.

# send this value to the function (add_skill) in class ( Person ) by object p1
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')

# send this value or override this value to class ( Person ) for function   __init__
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
# calling function (person_info) in class ( Person ) by object p2
print(p2.person_info()) # John Doe is 30 years old. He lives in Noman city, Nomanland.


# calling just value of (skills) variable in class ( Person ) in the funciton   __init__   after sending this value that we send by object p1
print(p1.skills) # ['HTML', 'CSS', 'JavaScript']

# calling (skills) variable in class ( Person ) in function   __init__   after sending this value that we send by object p2
# not value is send to the (skills) because it is not the parameter
print(p2.skills) # []





print('========================== Inheritance ==========================')

class Person:
    def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        # we use this variable to be used by other function because i want send value to this variable by other funciton inside class (Person)
        # in this case is (add_skill)
        self.skills = []

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

    def add_skill(self, skill):
        # self.skills # is calling value of (skills) variable that is inside function   __init__
        # append(skill) # we send value from (skill) parameter to (skills) variable of function   __init__   by using   ( append() ) function
        # ( append() ) funciton will send value to variable (skills) as list
        self.skills.append(skill)


class Student(Person):
    # pass keyword means test is pass and not error happen
    pass


s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
# calling function (person_info) in class (Person) by object s1
print(s1.person_info())  # Eyob Yetayeh is 30 years old. He lives in Helsinki, Finland.
# send this value to the function (add_skill) in class (Person) by object s1
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
# calling value of (skills) variable in class (Person) in function (__init__) by object s1
print(s1.skills)  # ['JavaScript', 'React', 'Python']

# calling function (person_info) in class (Person) by object s2
print(s2.person_info())  # Lidiya Teklemariam is 28 years old. He lives in Espoo, Finland.
# send this value to the function (add_skill) in class (Person) by object s2
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
# calling value of (skills) variable in class (Person) in function (__init__) by object s2
print(s2.skills)  # ['Organizing', 'Marketing', 'Digital Marketing']





print('========================== Overriding parent method ==========================')

class Person:
    def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

    def add_skill(self, skill):
        self.skills.append(skill)



# this class is use content class (Person) it is like you have this content inside class (Student)
class Student(Person):
    def __init__(self, firstname='ameze', lastname='karem', age=250, country='Kurdistan', city='sulimany', gender='female'):
        self.gender = gender
        # all that parameter that you have here is super class for class (Person)
        # super()   function is used to give access to methods and properties of a parent or sibling class.
        super().__init__(firstname, lastname, age, country, city)
        '''
        # it is like you are do this
        
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        '''

    def person_info(self):
        # if self.gender == 'male': self.gender = 'He' else: self.gender = 'She'
        self.gender = 'He' if self.gender == 'male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {self.gender} lives in {self.city}, {self.country}.'
        # # you can also do that
        # gender = 'He' if self.gender == 'male' else 'She'
        # return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'


s3 = Person()
s4 = Student()
print(s3.person_info()) # Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland.
print(s4.person_info()) # ameze karem is 250 years old. She lives in sulimany, Kurdistan.


# Send or Override this value to the class Student
s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki', 'male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info()) # Eyob Yetayeh is 30 years old. He lives in Helsinki, Finland.

# send this value to the function (add_skill) in class (Student) by using object s1
# Note: we don't have funciton (add_skill) in class (Student) but because class (Student) use class (Person) as parameter then it is like this function is inside class (Student)
# it is mean that function (add_skill) is point to the class (Student)
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
# calling value of (skills) variable of class (Student) by using object s1
print(s1.skills) # ['JavaScript', 'React', 'Python']
print(s2.person_info()) # Lidiya Teklemariam is 28 years old. She lives in Espoo, Finland.

# send this value to the function (add_skill) in class (Student) by using object s1
# Note: we don't have funciton (add_skill) in class (Student) but because class (Student) use class (Person) as parameter then it is like this function is inside class (Student)
# it is mean that function (add_skill) is point to the class (Student)
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
# calling value of (skills) variable of class (Student) by using object s2
print(s2.skills) # ['Organizing', 'Marketing', 'Digital Marketing']


