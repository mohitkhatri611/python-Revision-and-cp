""" It describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. To prevent accidental change, an object’s variable can only be changed by an object’s method. Those types of variables are known as private variable. 

A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc

Consider a real-life example of encapsulation, in a company, there are different sections like the accounts section, finance section, sales section etc.  Using encapsulation also hides the data. In this example, the data of the sections like sales, finance, or accounts are hidden from any other section.
"""


"""  Protected members
   
   Protected members are those members of the class that cannot be accessed outside the class but can be accessed from within the class and its subclasses. To accomplish this in Python, just follow the convention by prefixing the name of the member by a single underscore “_”.
    Note: The __init__ method is a constructor and runs as soon as an object of a class is instantiated. 
   """

class Base:
    def __init__(self):

        #protected member
        self._a = 2

    #creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling proctected memeber of base class: ")
        print(self._a)

obj1=Derived()
obj2=Base()
# Calling protected member
# Outside class will  result in
# AttributeError
print(obj2.a)


""" .............. Private members......... 
Private members are similar to protected members, the difference is that the class members declared private should neither be accessed outside the class nor by any base class. In Python, there is no existence of Private instance variables that cannot be accessed except inside a class. However, to define a private member prefix the member name with double underscore “__”.

"""


# Python program to
# demonstrate private members

# Creating a Base class
class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"


# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)


# Driver code
obj1 = Base()
print(obj1.a)

# Uncommenting print(obj1.c) will
# raise an AttributeError

# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class



