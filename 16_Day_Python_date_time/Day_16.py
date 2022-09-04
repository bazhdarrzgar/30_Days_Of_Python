print('========================== Python datetime ==========================')

'''
this function that you can use with datetime module

*   MAXYEAR
*   MAXYEAR
*   MINYEAR 
*   __builtins__ 
*   __cached__ 
*   __doc__ 
*   __file__ 
*   __loader__ 
*   __name__ 
*   __package__ 
*   __spec__ 
*   date 
*   datetime 
*   datetime_CAPI 
*   sys 
*   time 
*   timedelta 
*   timezone 
*   tzinfo

'''


import datetime

# dir()  function use for taking information about keyword or function in python
print(dir(datetime))

'''
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
'''



print('========================== Getting datetime Information ==========================')

'''
# Note: now() function will get back the time that we are now in exactly this time ( year month day hour:minute:second ) 
# now() function dynamic change when each time ms you are calling it for time


datetime.now() = year / month / day  hour:minute:second
datetime.now().day = day
datetime.now().month = month
datetime.now().hour = hour
datetime.now().minute = minute
datetime.now().second = second
datetime.now().timestamp() = timestamp  # YYYY-MM-DDT HH:MM:SSZ # all this with number of day and hour and minute and second and ..
'''

from datetime import datetime

now = datetime.now()
print(now)                      # 2022-09-04 13:20:43.750026
day = now.day                   # 8
month = now.month               # 7
year = now.year                 # 2021
hour = now.hour                 # 7
minute = now.minute             # 38
second = now.second
timestamp = now.timestamp()
print('timestamp', timestamp) # timestamp 1662286843.750026
print(day, month, year, hour, minute)  # 4 9 2022 13 20
# (f) before the double or single quotes means i use variable inside the string
# the variable is declared inside this bracket {}
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 4/9/2022, 13:20




print('========================== Formatting Date Output Using strftime ==========================')

'''
datetime(2020, 1, 2) # this is custome date time you can put anything you want

datetime(2020, 1, 2).day    # 2
datetime(2020, 1, 2).month  # 1
datetime(2020, 1, 2).year   # 2020
datetime(2020, 1, 2).hour   # 0
datetime(2020, 1, 2).minute # 0
datetime(2020, 1, 2).second # 0

'''

from datetime import datetime

new_year = datetime(2020, 1, 2) # custome date time
print(new_year)      # 2020-01-01 00:00:00 # because datetime function is handle the (hour and minute and second) then in place of this we are using zero by default

day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second

print(day, month, year, hour, minute, second) # 2 1 2020 0 0
print(f'{day}/{month}/{year}, {hour}:{minute}:{second}')  # 1/1/2020, 0:0




'''
# strftime() use string formating time for calling the time and format it to this way that you like
# strftime() use this keyword for calling this time you like

%H %M %S    hour minute second
%d/%m/%Y    day month full_year


# more keyword

%s          timestamp

%D          month day mini_year

%Y          full year
%y          mini year

%h          for month but using string way

# Note: between this keyword you can use anything you like for example this symbol (:) or this (/) or (//) or .... anything you can type in the string format
'''


from datetime import datetime

now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t) # time: 14:17:49


time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one) # time one: 09/04/2022, 14:17:49


time_two = now.strftime("%D, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two:", time_two) # time two: 09/04/2022, 14:17:49

time_three = now.strftime("%h/%d/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time three:", time_three) # time two: sep/09/2022, 14:17:49


time_four = now.strftime("%s, %H:%M:%S")
# timestamp H:M:S format
print("time four:", time_four) # time two: 1662290595, 14:17:49



print("mini year: ", now.strftime("%y, %H:%M:%S")) # time two: 22, 14:17:49
print("full year: ", now.strftime("%Y, %H:%M:%S")) # time two: 2022, 14:17:49




print('========================== String to Time Using strptime ==========================')

'''
# Note: (datetime) read the time from right to left if you want change time to (datetime) then if it is left to right the (datetime) function will change it to the right to left


# Syntax change manual time to datetime using datetime function
datetime('datetime...., format')
'''

from datetime import datetime

date_string = "5 December, 2019"
print("date_string =", date_string) # date_string = 5 December, 2019

# this will change ( 5 December, 2019 ) to ( %d (day) %B (Month with name), %Y (full year)
# we use (strptime) =  (string portable time)
# means the format just for specify that this string is how standarded they time and format tell (strptime) in where the string is use day or month or year or ..
# and (strptime) change it to portable format means just standard time that is just number to represent the time
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object) # date_object = 2019-12-05 00:00:00





print('========================== Using date from datetime ==========================')

'''
# Syntax

date().today() # return exactly (FullYear-month-day)
date().year  # return full year of today() function
date().month # return month of today() function
date().day   # return day of today() function
'''

from datetime import date

d = date(2020, 1, 2) # custome date
print(d) # 2020-01-02
print(d.year) # 2020
print(d.month) # 1
print(d.day) # 2

# print(date().today())              # error # TypeError: function missing required argument 'year' (pos 1)
print(date(2020, 1, 2).today())      # 2022-09-04

# today()   use for taking the    date()   function today time
print('Current date:', d.today())    # 2022-09-04 # ( today() ) function will override the value of ( date() ) function because they have own value and not return value of other funciton

# date object of today's date
today = date.today()
print("Current year:", today.year)   # 2022
print("Current month:", today.month) # 9
print("Current day:", today.day)     # 4




print('========================== Time Objects to Represent Time ==========================')

'''
# time() function use for taking the custome time (hour and minute and second and microsecond and day and month and year ...) depending of this position that they have or this key that they have
'''

from datetime import time

# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a) # a = 00:00:00


# time(value_hour, value_minute, value_second)
b = time(10, 30, 50) # just taked value depending of the order of (hour and minute and second and microsecond)
print("b =", b) # b = 10:30:50


# time(hour = value_hour, value_minute = minute, second = value_second, microsecond = value_microsecond)
c = time(hour=10, minute=30, second=50, microsecond=22) # taking value depending of this key that the value is have in this way you can change the position of any value if you want
print("c =", c) # c = 10:30:50.000022


# time(value_hour, value_minute, value_second, value_microsecond)
d = time(10, 30, 50, 200555) 
print("d =", d) # d = 10:30:50.200555






print('========================== Difference Between Two Points in Time Using ==========================')

from datetime import date, datetime

# you can use   date()   function value for calculation but the format should be the same between each of the value you have in the   date()   function
today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today

# Time left for new year:  27 days, 0:00:00
print('Time left for new year: ', time_left_for_newyear) # Time left for new year:  27 days, 0:00:00



# you can also use   datetime()   function value for calculation but the format should be the same between each of the value you have in the   datetime()   function
t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1

print('Time left for new year:', diff) # Time left for new year: 26 days, 23:01:00



# t1 = datetime(year = 2019, hour = 0, minute = 59, second = 0) 
# t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
# diff = t2 - t1

# print('Time left for new year:', diff) # error # TypeError: function missing required argument 'month' (pos 2)



print('========================== Difference Between Two Points in Time Using timedelata ==========================')
# timedelta() function use for calculation between one or more time means there value can be use for calculation and calculation can be in any format you like


from datetime import timedelta

# with   timedelta()   you can use default format but it is much nicer if you are use key of the value in this case
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
# this will culculate between this two time that we have in   timedelta()   function the calculation in this case is minize t1 to t2
t3 = t1 - t2

print("t3 =", t3) # t3 = 86 days, 22:56:50
