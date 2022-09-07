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
