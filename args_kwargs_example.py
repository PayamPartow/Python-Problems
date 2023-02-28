def Func(*args):  # adding this makes out function take anywhere from 0 to infinite arguments
    for arg in args:
        print(arg)


# Func(1,2,3,4,5,'ham')
l = [1, 2, 3, 4, 5, 'ham']
Func(l)  # prints the list as a whole
Func(*l)  # this will run through the list and prints out each individual argument in the list


# key word arguments (KWARGS)
def Func(x=234, y=9):  # setting default values for our arguments
    print(x, y)


Func()
Func(x=456, y=3)  # default vars are overwritten


def Func(**kwargs):
    for item in kwargs.items():  # treating it like a dictionary
        print(item)


Func(x=456, y=3)


def Func(*args, **kwargs):
    for arg in args:
        print(arg)
    for item in kwargs.items():  # treating it like a dictionary
        print(item)


Func(12, x=456, y=3)  # needs to be in order of the *args and **kwargs in the main function definition


