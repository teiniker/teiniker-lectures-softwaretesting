# Complexity Metrics

The following metrics are measured using [Radon](https://pypi.org/project/radon/), a Python metrics tool.

## Lines of Code (LOC)
```
Usage: $ radon raw <path1> <path2>
```

This command analyzes the given Python modules in order to compute raw metrics. These include:
* **LOC**: the total number of lines of code
* **LLOC**: the number of logical lines of code
* **SLOC**: the number of source lines of code - not necessarily corresponding to the LLOC [Wikipedia]
* **comments**: the number of Python comment lines (i.e. only single-line comments #)
* **multi**: the number of lines representing multi-line strings
* **blank**: the number of blank lines (or whitespace-only ones)

The following options can be used:

* `-s`, `--summary`\
    If given, at the end of the **analysis a summary** of the gathered metrics will be shown.

* `-j`, `--json`\
    If given, the **results will be converted into JSON**.

* `-O`, `--output-file`\
    **Save output** to the specified output file.


## Cyclomatic Complexity Number (CCN)

```
Usage: $ radon cc <path> -s
```

This command analyzes Python source files and compute Cyclomatic Complexity.

By default, the complexity score is not displayed, the option `-s` (show complexity) toggles this behaviour.
Every block will be ranked from **A** (best complexity score) to **F** (worst one).
```
    CC score	Rank	Risk
    1  - 5	A	low - simple block
    6  - 10	B	low - well structured and stable block
    11 - 20	C	moderate - slightly complex block
    21 - 30	D	more than moderate - more complex block
    31 - 40	E	high - complex block, alarming
    41+  	F	very high - error-prone, unstable block
```

Blocks are also classified into three types: functions, methods and classes.
```
    Block type	Letter
    Function	  F
    Method	      M
    Class	      C
```

The following options can be used:

* `-s`, `--show-complexity`\
   If given, **show the complexity score along with its rank**. Value can be set in a configuration file using the show_complexity property.

* `-j`, `--json`\
   If given, the **results will be converted into JSON**. This is useful in case you need to export the results to another application.

* `--xml`\
   If given, the **results will be converted into XML**. Note that not all the information is kept. 
   This is specifically targeted to Jenkin’s plugin CCM.

* `-O`, `--output-file`\
   **Save output** to the specified output file.

## References
* [Radon](https://pypi.org/project/radon/)			


# Static Code Analysis 

**Pylint** is a tool that checks for errors in Python code, tries to enforce a coding standard and looks for code smells. 
It can also look for certain type errors, it can recommend suggestions about how particular blocks can be refactored 
and can offer you details about the code's complexity

Install Pylint, we can use the `pip` command:
```
pip3 install pylint
```

Pylint is usually installed with the Visual Studio Code **Python Extension**.

```
Usage: $ pylint <path> 
```

In the simplest case, Pylint is called for a single Python file.

_Example_: Pylint analysis for a single file
```
$ pylint simple_caesar.py 
************* Module simple_caesar
simple_caesar.py:1:0: W0301: Unnecessary semicolon (unnecessary-semicolon)
simple_caesar.py:24:0: C0304: Final newline missing (missing-final-newline)
simple_caesar.py:1:0: C0114: Missing module docstring (missing-module-docstring)
simple_caesar.py:3:0: C0103: Constant name "shift" doesn't conform to UPPER_CASE naming style (invalid-name)
simple_caesar.py:7:0: C0103: Constant name "encoded" doesn't conform to UPPER_CASE naming style (invalid-name)
simple_caesar.py:12:12: C0103: Constant name "encoded" doesn't conform to UPPER_CASE naming style (invalid-name)
------------------------------------------------------------------
Your code has been rated at 6.84/10 (previous run: 9.47/10, -2.63)
```


## References 
* [Pylint](https://pypi.org/project/pylint/)

* [Pylint User Manual](http://pylint.pycqa.org/en/latest/)