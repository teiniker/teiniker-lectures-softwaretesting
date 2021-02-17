# Python Setup

This document describes how we setup a Python environment, the
libraries, and tools we need to run the examples stored in this repository.

## Python 3 
(incuding pip3)


## Code Coverage Analysis Tool

* Raspberry Pi Desktop VM
```
    $ pip3 install coverage

    $ vi .bashrc
    export COVERAGE_HOME=/home/pi/.local/bin/
    export PATH=$COVERAGE_HOME/bin:$PATH

    $ coverage run --branch unittest unittests/fixture/OrderTest.py
```

* Fedora 30 VM
```
    $ python3 -m pip install coverage
    Requirement already satisfied: coverage in /usr/lib64/python3.7/site-packages (4.5.1)

    $ coverage3 --version
```

## SQLite3 Database (and SQLite Browser)

* SQLite3 Setup Fedora 30
 ```
    $ sudo yum install sqlite  // already installed
    $ sudo yum install sqlitebrowser
    $ sqlite3 test.db
    sqlite> .quit
```

*  SQLite3 Setup Raspberry Desktop
``` 
    # apt-get install sqlite3
    # apt-get install sqlitebrowser
```

## PyAutoGUI

* Setup for Fedora 30
```
    $ sudo yum install scrot
    $ sudo yum install python3-tkinter      # already installed
    $ sudo yum install python3-devel.x86_64 # already installed

    $ sudo python3 -m pip install python3-xlib
    $ python3 -m pip install pyautogui
```

* Automate the Boring Stuff with Python
```
    https://automatetheboringstuff.com/
    https://automatetheboringstuff.com/2e/chapter20/
```

## Selenium Webdriver

* Selenium
 ```
    https://www.selenium.dev
```
    
* Setup for Fedora 30
```
    $ sudo python3 -m pip install selenium

	URL: https://pypi.org/project/selenium/4.0.0a5/
	download: geckodriver-v0.26.0-linux64.tar.gz
	=> /home/student/local/webdriver/geckodriver

	$ geany .bashrc
		export WEBDRIVER=/home/student/local/webdriver
		export PATH=$JAVA_HOME/bin:$M2_HOME/bin:$ANT_HOME/bin:$SONAR_SCANNER/bin:$WEBDRIVER:$PATH

	$ source .bashrc  # or open a new terminal
	$ echo $WEBDRIVER
	$ echo $PATH

    Test the Webdriver from Python:
    $ python3
    >>> from selenium import webdriver
    >>> from selenium import webdriver
    >>> driver = webdriver.Firefox()
    >>> driver.quit()
    >>> exit()

    Start the PyCharm IDE from the command line to use the new settings:
    $ /opt/pycharm-community-2019.2.2/bin/pycharm.sh
    Python Console:
       >>> from selenium import webdriver
       >>> driver = webdriver.Firefox()
       >>> driver.quit()
```


## Radon 4.1.0
```
https://pypi.org/project/radon/
```
* Setup
 ```
    $ sudo python3 -m pip install radon
```

* Documentation
``` 
    https://radon.readthedocs.io/en/latest/index.html
```
