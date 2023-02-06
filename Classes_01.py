# example 1

# class BaseClass(object):  # object is a base class that allows inheritance
#     def printHam(self):  # in our case this still works without typing object because we are not accessing any
#         # variables or attributes within BasClass
#         print('Ham')
#
#
# class InheritingClass(BaseClass):  # this class is inheriting from BaseClass
#     pass
#
#
# x = InheritingClass()
# x.printHam()


# example 2

# class Character(object):
#     def __init__(self, name):
#         self.health = 100
#         self.name = name
#
#     def printName(self):
#         print(self.name)
#
#
# class Blacksmith(Character):
#     def __init__(self, name, forgeName):
#         super(Blacksmith, self).__init__(name)  # calls the init function from the base class we inherited from
#         self.forge = Forge(forgeName)
#
#
# class Forge:
#     def __init__(self, forgeName):
#         self.name = forgeName
#
#
# bs = Blacksmith("Bob", "Rick\'s Forge")
# # print(bs.health)
# bs.printName()
# print(bs.forge.name)


# example 3

class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullName(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)  # this will make the Employee class handling these variables
        self.prog_lang = prog_lang


class Manager(Employee):
    # never pass mutable data types (list or dict) as default arguments
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullName())


dev_1 = Developer('Payam', 'Partow', 80000, 'Python')
dev_2 = Developer('Faraz', 'Shamshirdar', 200000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(isinstance(mgr_1, Developer))  # function to check if an object is an instance of a certain class or subclass
print(issubclass(Manager, Employee))  # to check if a class is a subclass of another class
mgr_1.add_emp(dev_2)
print(mgr_1.email)
mgr_1.print_emps()
# print(help(Developer)) #shows all the classes that developer is inheriting from and all the inherited methods and vars

# print(dev_1.email)
# print(dev_1.prog_lang)
# print(dev_2.email)
#
# print(dev_1.pay)
# dev_1.apply_raise()  # uses our Developers raise amount
# print(dev_1.pay)
