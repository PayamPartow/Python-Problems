
#practice 1 : create a function that returns ham then create a function that adds sandwitch to all functions passed in
#apply decorators to first function

def addSandwitch(my_func):
    def add_Sandwitch_here():
        return my_func() + ' ' + 'Sandwich'
    return add_Sandwitch_here()

@addSandwitch
def printHam():
    return 'Ham'


print(printHam)



#practice 2: do the same thing with random float values

def addToFloat(myFunc):
    def addToFloatHere():
        return myFunc() + 3.567
    return addToFloatHere()

@addToFloat
def random_float(x=3.14):
    return x

print(random_float)