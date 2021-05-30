"""
Data abstraction in python
Abstraction is used to hide the internal functionality of the function from the users. The users only interact with the basic implementation of the function, but inner working is hidden. User is familiar with that "what function does" but they don't know "how it does.

n simple words, we all use the smartphone and very much familiar with its functions such as camera, voice-recorder, call-dialing, etc., but we don't know how these operations are happening in the background. Let's take another example - When we use the TV remote to increase the volume. We don't know how pressing a key increases the volume of the TV. We only know to press the "+" button to increase the volume.

Abstraction is an important aspect of object-oriented programming. In python, we can also perform data hiding by adding the double underscore (___) as a prefix to the attribute which is to be hidden. After this, the attribute will not be visible outside of the class through the object.

Consider the following example.

"""
#Example
class Employee:
    __count = 0;
    def __init__(self):
        Employee.__count = Employee.__count+1
    def display(self):
        print("The number of employees",Employee.__count)
emp = Employee()
emp2 = Employee()
try:
    print(emp.__count)
finally:
    emp.display()
"""Output:

The number of employees 2
AttributeError: 'Employee' object has no attribute '__count'"""


"""Abstraction classes in Python"""
"""
                Points to Remember
Below are the points which we should remember about the abstract base class in Python.

An Abstract class can contain the both method normal and abstract method.
An Abstract cannot be instantiated; we cannot create objects for the abstract class.
Abstraction is essential to hide the core functionality from the users.

A class that consists of one or more abstract method is called the abstract class. Abstract methods do not contain their implementation. Abstract class can be inherited by the subclass and abstract method gets its definition in the subclass. Abstraction classes are meant to be the blueprint of the other class. An abstract class can be useful when we are designing large functions. An abstract class is also helpful to provide the standard interface for different implementations of components. Python provides the abc module to use the abstraction in the Python program. Let's see the following syntax.

An abstract base class is the common application program of the interface for a set of subclasses. It can be used by the third-party, which will provide the implementations such as with plugins. It is also beneficial when we work with the large code-base hard to remember all the classes.
"""
#Working of the Abstract Classes
"""Unlike the other high-level language, Python doesn't provide the abstract class itself. We need to import the abc module, which provides the base for defining Abstract Base classes (ABC). The ABC works by decorating methods of the base class as abstract. It registers concrete classes as the implementation of the abstract base. We use the @abstractmethod decorator to define an abstract method or if we don't provide the definition to the method, it automatically becomes the abstract method."""

# Python program demonstrate
# abstract base class work
from abc import ABC, abstractmethod


class Car(ABC):
    def mileage(self):
        pass


class Tesla(Car):
    def mileage(self):
        print("The mileage is 30kmph")


class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25kmph ")


class Duster(Car):
    def mileage(self):
        print("The mileage is 24kmph ")


class Renault(Car):
    def mileage(self):
        print("The mileage is 27kmph ")

    # Driver code


t = Tesla()
t.mileage()

r = Renault()
r.mileage()

s = Suzuki()
s.mileage()
d = Duster()
d.mileage()

"""Output:

The mileage is 30kmph
The mileage is 27kmph 
The mileage is 25kmph 
The mileage is 24kmph
"""
"""In the above code, we have imported the abc module to create the abstract base class. We created the Car class that inherited the ABC class and defined an abstract method named mileage(). We have then inherited the base class from the three different subclasses and implemented the abstract method differently. We created the objects to call the abstract method."""

#Example 2


# Python program to define
# abstract class

from abc import ABC


class Polygon(ABC):

    # abstract method
    def sides(self):
        pass


class Triangle(Polygon):

    def sides(self):
        print("Triangle has 3 sides")


class Pentagon(Polygon):

    def sides(self):
        print("Pentagon has 5 sides")


class Hexagon(Polygon):

    def sides(self):
        print("Hexagon has 6 sides")


class square(Polygon):

    def sides(self):
        print("I have 4 sides")

    # Driver code


t = Triangle()
t.sides()

s = square()
s.sides()

p = Pentagon()
p.sides()

k = Hexagon()
k.sides()
"""Output:

Triangle has 3 sides
Square has 4 sides
Pentagon has 5 sides
Hexagon has 6 sides"""
"""In the above code, we have defined the abstract base class named Polygon and we also defined the abstract method. This base class inherited by the various subclasses. We implemented the abstract method in each subclass. We created the object of the subclasses and invoke the sides() method. The hidden implementations for the sides() method inside the each subclass comes into play. The abstract method sides() method, defined in the abstract class, is never invoked."""