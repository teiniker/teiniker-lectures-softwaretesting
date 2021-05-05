# Code Coverage Analsis

Code coverage analysis is the process of:
* Finding areas of a program not exercised by a set of test cases.
* Creating additional test cases to increase coverage.
* Determining a quantitative measure of code coverage, which is an indirect measure of quality.
* Identifying redundant test cases that do not increase coverage.

Note that the primary goal is not to reach an ultimately high coverage rate, but to exploit coverage 
visualization for **identifying areas of the code that are not covered by tests yet**, but that are test-worthy.


## Code Coverage Metrics
We use coverage analysis to assure quality of our set of tests, not the quality 
of the actual product.

An analysis can use different coverage metrics:
* **Function coverage** is a measure for verifying that each function (method) 
    is invoked during test execution.

* **Block coverage** considers each sequence of non-branching statements as its 
    unit of code instead of individual statements.
    
* **Statement coverage (line coverage)** is a measure which indicates the degree to 
    which individual statements are getting executed during test execution.
    
* **Decision coverage (branch coverage)** is a measure based on whether decision 
    points, such as `if` and `while` statements, evaluate to both `true` and `false` during 
    test execution, thus causing both execution paths to be exercised. 
   
* **Condition coverage** extends the boolean evaluation of decision coverage into 
    the sub-expressions (separated by logical ANDs and ORs) as well, making sure 
    each of them is evaluated to both `true` and `false`.
   
* **Path coverage** measures whether each possible path from start (method entry) to 
    finish (return statement, thrown exception) is covered.

## Coverage.py
Coverage.py is a tool for measuring code coverage of Python programs. By default, **statement
coverage** will be measured.

There are a few different ways to use coverage.py. 
The simplest is the **command line**, which lets you run your program and see the results:

_Example_: Run coverage.py from the command line
```
$ coverage3 run -m unittest comparator_test.py
$ coverage3 report 
$ coverage3 html
```
Make sure you are in your project's directory when you execute the commands.
The **run** command executes all test cases in the specified file and records the coverage
information. **report** reads the recorded data and creates a command line summary of the 
coverage analysis.
With **html**, a HTML report will be generated, which can be reviewed with a web browser:
 
URL: `htmlcov/index.html` 

coverage.py also supports **branch coverage** measurement. 
Where a line in your program could jump to more than one next line, coverage.py tracks 
which of those destinations are actually visited, and flags lines that haven’t visited 
all of their possible destinations.

To measure branch coverage, run coverage.py with the `--branch` flag.

_Example_: Measure branch coverage
```
$ coverage run --branch -m unittest comparator_test.py
$ coverage3 report 
$ coverage3 html
```
When you report on the results with coverage report or coverage html, 
the percentage of branch possibilities taken will be included in the 
percentage covered total for each file. The coverage percentage for a 
file is the actual executions divided by the execution opportunities. 
Each line in the file is an execution opportunity, as is each branch destination.

The HTML report gives information about which lines had missing branches. 
Lines that were missing some branches are shown in yellow, with an annotation 
at the far right showing branch destination line numbers that were not exercised.


## References
* Stefan Berner, Roland Weber, Rudolf K. Keller. 
    **Enhancing Software Testing by Judicious Use of Code Coverage Information**. ICSE 2007

* [Coverage.py](https://coverage.readthedocs.io/en/coverage-5.5/)

*Egon Teiniker, 2020-2021, GPL v3.0*


