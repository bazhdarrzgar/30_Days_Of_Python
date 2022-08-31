print('========================== Dictionaries ==========================')
print('\n\n')
print('========================== If Condition ==========================')

'''
# Syntax

if condition:
    ...code problem
    
'''

a = 3

if a > 0:
  print('A is a positive number')

if a < 0:
  print('A is negative number')

if a == 0:
  print('A is 0')



print('========================== If Else ==========================')

'''
# Syntax

if condition:
    ...code problem
    
else:
    ...code problem

'''

a = 3
            
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')



print('========================== If Elif Else ==========================')

'''
# Syntax

if condition:
    ...code problem
    
elif condition:
    ...code problem
    
else:
    ...code problem
    
'''

a = 0

if a > 0:
    print('A is a positive number')
    
elif a < 0:
    print('A is a negative number')

else:
    print('A is zero')



print('========================== Short Hand ==========================')


'''
# Syntax

...code problem_1 if condition else ...code problem_2
# note we don't use this symbol (:) with if and else because this is the rule for this trick
# note this technique of condition not use ( elif )
# we just write all the condition in one line

## Explain

if first condition is true then print (...code problem_1)
else print (...code problem_2)

'''

a = 3

print('A is positive') if a > 0 else print('A is negative') 
# A is positive

print('A is positive') if a > 0 else print('A is negative') 
# A is negative



print('========================== Nested Conditions ==========================')
# if statement inside another or this is also inside another or .... 

'''
# Syntax

if condition:
    ...code problem
    
    if condition:
      ...code problem
      
      ..............
    
elif:

    if condition:
      ...code problem
            
      ..............
        
      if condition:
        ...code problem
        
        .............
    
    else:
      ...code problem
      
        .............
      
      

elif:

    if condition:
      ...code problem

      ............
    
    else:
      ...code problem
      
      ............
      
..........
   
'''

a = 0 # A is zero 
a = 1 # A is a positive and odd integer
a = 2 # A is a positive and even integer

if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
        
    elif a % 2 != 0:
        print('A is a positive and odd integer')

    else:
        print('A is a positive number')

elif a == 0:
    print('A is zero')

else:
    print('A is a negative number')




print('========================== If Condition and Logical Operators ==========================')

'''
# Syntax

if condition and condition:
    ...code problem
    
'''

a = 0 # A is zero
a = 1 # A is an odd and positive integer
a = 2 # A is an even and positive integer

if a > 0 and a % 2 == 0:
    print('A is an even and positive integer')

elif a > 0 and a % 2 != 0:
    print('A is an odd positive integer')

elif a == 0:
    print('A is zero')

else:
    print('A is negative')



print('========================== If and Or Logical Operators ==========================')

'''
# Syntax

if condition or condition:
    ...code problem

'''



user = 'James'

access_level = 5

if user == 'admin' or access_level >= 4:
    print('Access granted!')

else:
    print('Access denied!')

# Access granted!



