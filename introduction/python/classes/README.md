# Classes

In **object-oriented programming** we write **classes** that represent real-world things 
and situations, and we create **objects** based on these classes.

When we write a class, we define the general behavior that a whole category of objects can have. 
When we create individual objects from the class, each object is automatically equipped with the 
general behavior; we can then give each object whatever unique properties we desire.

Making an object from a class is called **instantiation**, and we work with instances of 
a class (a.k.a. objects).

## Defining a Class
Class names should be written in CamelCaps.
Instance and module names should be written in lowercase with underscores between words. 
Every class should have a docstring immediately following the class definition.

_Example_: Resistor
```Python
class Resistor():
    """Simulates a resistor with a given tolerance."""

    def __init__(self, value, tolerance=2):
        self._value = value              
        self._tolerance = tolerance       
        # self.tolerance = 2

    def get_value(self):
        return self._value

    def get_tolerance(self):
        return self._tolerance

    def serial(self, resistor):
        self._value += resistor.get_value()

    def parallel(self, resistor):
        r1 = self._value
        r2 = resistor.get_value()
        self._value = r1 * r2 / float(r1 + r2)
``` 

### __init__() 
This method Python runs automatically whenever we create a **new instance of a class**.

The **self parameter** is required in the method definition, and it must come first before 
the other parameters.
Every method call associated with a class automatically passes self, which is a reference 
to the instance itself; 
it gives the individual instance access to the attributes and methods in the class.


### Attributes
Attributes created in `__init__()` are called **instance attributes**. 
An instance attribute’s value is specific to a particular instance of the class.

On the other hand, **class attributes** are attributes that have the same value for all 
class instances. 
We can define a class attribute by assigning a value to a variable name outside of `__init__()`.

**Private attributes** that cannot be accessed except from inside an object don't exist in Python.
There is a convention that is followed by most Python code: a **name prefixed with an underscore** 
(e.g. `_value`) 
should be treated as a non-public part of the API (whether it is a function, a method or a data member).

Every attribute in a class needs an initial value, even if that value is 0 or an empty string. 
In some cases, such as when setting a **default value**, it makes sense to specify this initial value in 
the body of the `__init__()` method.

We can **change an attribute’s value** in three ways: 
* We can change the value directly through an instance
* Set the value through a method
* Increment the value (add a certain amount to it) through a method.


### Methods
Instance methods are functions that are defined inside a class and can only be called from an instance 
of that class. 
Just like `__init__()`, an instance method’s first parameter is always self.


## Making an Class Instance

When Python reads the following line, it calls the `__init__()` method:
```Python
r1 = Resistor(1000)
```

The `__init__()` method has no explicit return statement, but Python automatically returns an instance.
We can create as many instances from a class as we need.


## Accessing Attributes and Calling Methods

To **access the attribute** of an instance, we use the **dot notation**.

To **call a method**, give the name of the instance and the method we want to call, separated by a dot.


## Inheritance
When one class inherits from another, it automatically takes on all the attributes and methods of the 
first class. The original class is called the **parent class**, and the new class is the **child class**.
The child class inherits every attribute and method from its parent class but is also free to define 
new attributes and methods of its own.

When we create a child class, the parent class must be part of the current file and must appear before 
the child class in the file. 
The name of the parent class must be included in parentheses in the definition of the child class.

The `super()` function is a special function that helps Python make connections between the parent and 
child class. The name super comes from a convention of calling the parent class a **superclass** and 
the child class a **subclass**.

The `__init__()` method for a child class needs help from its parent class, so it calls 
`super().__init__()` to inizialize the attributes of the parent class.

Once we have a child class that inherits from a parent class, we can 
**add any new attributes and methods** necessary to differentiate the child class from the parent class.

We can **override** any method from the parent class that doesn’t fit what we’re trying to model with the child class. 
To do this, we define a method in the child class with the same name as the method you want to override in the parent class.
Python will disregard the parent class method and only pay attention to the method you define in the child class.


## References
* [Object-Oriented Programming (OOP) in Python 3](https://realpython.com/python3-object-oriented-programming/)
* Eric Matthes. Python Crash Course. No Starch Press, 2016. Chapter 9: Classes

*Egon Teiniker, 2020-2021, GPL v3.0*