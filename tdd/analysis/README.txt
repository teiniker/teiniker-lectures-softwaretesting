
How to run the test cases?
-------------------------------------------------------------------------------
$ pwd
teiniker-lectures-softwaretesting

Tip: Make sure that the path to the data file is 'tdd/analysis/data.csv'

$ python3 -m unittest tdd/analysis/DataAnalysisTest.py
......
----------------------------------------------------------------------
Ran 6 tests in 0.002s
OK


How to run the code coverage analysis?
-------------------------------------------------------------------------------
$ pwd
teiniker-lectures-softwaretesting

$ coverage3 run -m unittest tdd/analysis/DataAnalysisTest.py

$ coverage3 report -m
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
tdd/DataAnalysis.py          36      0   100%
tdd/DataAnalysisTest.py      31      0   100%
-------------------------------------------------------
TOTAL                        67      0   100%

$ coverage3 html
=> Browser: file:///home/student/github/teiniker-lectures-softwaretesting/htmlcov/index.html

