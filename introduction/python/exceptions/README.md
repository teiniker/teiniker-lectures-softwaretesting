# Exceptions

Python uses **special objects called exceptions to manage errors** that arise during a program’s execution. 
Whenever an error occurs that makes Python unsure what to do next, it creates an exception object.

If we write code that **handles the exception**, the program will continue running. 
If we don’t handle the exception, the program will halt and show a **traceback**, which includes a report 
of the exception that was raised.

Exceptions are handled with `try ... except`blocks. 
A `try ... except` block asks Python to do something, but it also tells Python what to do if an exception is raised.


## Raising an Exception

We can use `raise` to throw an exception if a condition occurs. 
The sole argument to `raise` indicates the exception to be raised. 
This must be either an **exception instance** or an **exception class** (a class that derives from Exception). 
If an exception class is passed, it will be implicitly instantiated by calling its constructor.

_Example_: Input validation
```Python
    def __init__(self, value, tolerance=2):
        if value < 0:
            raise ValueError('Invalid value!')
        if tolerance < 0:
            raise ValueError('Invalid tolerance!')

        self.value = value              
        self.tolerance = tolerance  
```

### Build-In Exceptions

#### Base Classes
* **Exception** \
    All built-in, non-system-exiting exceptions are derived from this class. 
    All **user-defined exception**s should also be derived from this class.
    
* **BaseException** \
    The base class for all built-in exceptions. 
    It is not meant to be directly inherited by user-defined classes (for that, use Exception). 

* **ArithmeticError** \
    The base class for those built-in exceptions that are raised for various arithmetic errors: 
    OverflowError, ZeroDivisionError, FloatingPointError.

#### Concrete Exceptions

* **IndexError** \
    Raised when a sequence subscript is out of range.

* **TypeError** \
    Raised when an operation or function is applied to an object of inappropriate type. The 
    associated value is a string giving details about the type mismatch.
    
* **ValueError** \
    Raised when an operation or function receives an argument that has the right type but an 
    inappropriate value, and the situation is not described by a more precise exception such 
    as `IndexError`.
    
* **NotImplementedError** \
    This exception is derived from `RuntimeError`. 
    In user defined base classes, abstract methods should raise this exception when they require 
    derived classes to override the method, or while the class is being developed to indicate that 
    the real implementation still needs to be added.    


### User Defined Exceptions
Programs may name their own exceptions by creating a new exception class. 
Exceptions should typically be derived from the `Exception` class, either directly or indirectly.

Most exceptions are defined with names that end in “`Error`”, similar to the naming of the standard exceptions.

Exception classes can be defined which do anything any other class can do, but are usually kept simple, 
often only offering a number of attributes that allow information about the error to be extracted by 
handlers for the exception.

_Example_: User defined exception without attributes
```Python
class DataAccessError(Exception):
    pass
```

When creating a module that can raise several distinct errors, a common practice is to create a base 
class for exceptions defined by that module, and subclass that to create specific exception classes for 
different error conditions.


## Handling Exceptions
It is possible to write programs that handle selected exceptions. 

```Python
    try:
        r1 = Resistor(-1000)
        #...
    except ValueError as e: 
        print("Resistor object can't be created: {}".format(e))  
```
The `try` statement works as follows.
* First, the `try` clause (the statement(s) between the `try` and `except` keywords) is executed.
* If no exception occurs, the `except` clause is skipped and execution of the `try` statement is finished.
* If an exception occurs during execution of the `try` clause, the rest of the clause is skipped. 
    Then if its type matches the exception named after the `except` keyword, the `except` clause is executed, 
    and then execution continues after the try statement.
* If an exception occurs which does not match the exception named in the `except` clause, it is passed on 
    to outer `try` statements; if no handler is found, it is an unhandled exception and execution stops 
    with a message.

A `try` statement may have more than one except clause, to specify handlers for different exceptions. 
At most one handler will be executed.

The last `except` clause may omit the exception name(s), to serve as a wildcard. 

### The `else` Block
The `try ... except` statement has an optional `else` clause, which, when present, must follow all except clauses. 
It is useful for **code that must be executed if the `try` clause does not raise an exception**.

_Example_: `try` with `else`
```Python
try:
    r1 = Resistor(1000)
    #...
except ValueError as e: 
    print("Resistor object can't be created: {}".format(e))    
else:    
    print("No exception thrown.")
```

### The `finally` Block
The `try` statement has another optional clause which is intended to define **clean-up actions** that 
**must be executed under all circumstances**. 

_Example_: `try` with `finally`
```Python
try:
    r1 = Resistor(-1000)
    #...
except ValueError as e: 
    print("Resistor object can't be created: {}".format(e))    
finally:    
    print("Do some clean-up.")    
```
If a `finally` clause is present, the `finally` clause will execute as the last task before the `try` statement completes. 
The `finally` clause runs whether or not the `try` statement produces an exception.

### Predefines Clean-up Actions
The `with` statement allows objects like files to be used in a way that ensures they are always cleaned up promptly 
and correctly.

`Example`: Open a file
```Python
   try:
        with open(self.filename, 'r') as f:
            reader = csv.reader(f, delimiter=',')
            data = list(reader)
        values = []
        for value in data:
            values.append(float(value[1]))
        return values
   except FileNotFoundError:
       raise DataAccessError('File not found: ' + self.filename)
```
After the statement is executed, the file `f` is always closed, even if a problem was encountered while 
processing the lines.

## References
* [The Python Tutorial: Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)

* [The Python Standard Library: Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)

* Eric Matthes. Python Crash Course. No Starch Press, 2016. 
    * Chapter 10: Files and Exceptions

* [Object-Oriented Programming (OOP) in Python 3](https://realpython.com/python3-object-oriented-programming/)

* [Python Exceptions: An Introduction](https://realpython.com/python-exceptions/)



*Egon Teiniker, 2020-2021, GPL v3.0*