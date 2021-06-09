# Setup Python, Tools & Libraries 

The following setup steps are described from the perspective of the [Debian VM](). 
For other platforms, the respective manuals must be used as an aid.

## Python 

Make sure that you have installed Python on your machine. If you use the Virtual Lab,
the following commands should work out of the box:
```
    $ python --version 
    Python 2.7.16

    $ python3 --version 
    Python 3.7.3

    $ sudo apt update
    $ sudo apt install python3-pip
    $ pip3 --version
    pip 18.1 from /usr/lib/python3/dist-packages/pip (python 3.7)
```

Basically, we could work directly with the command line Python interpreter like:
```    
    $ python3
    Python 3.7.3 (default, Jul 25 2020, 13:03:44) 
    [GCC 8.3.0] on linux 
    Type "help", "copyright", "credits" or "license" for more information.
    >>> print('Hello world!')
    Hello world!
    >>> exit()
```    
But for more sophisticated examples we use a more comfortable editor ...


## Coverage.py
Coverage.py is a tool for **measuring code coverage** of Python programs. 

It monitors your program, noting which parts of the code have been executed, 
then analyzes the source to identify code that could have been executed but 
was not.
```
$ pip3 install coverage
```

```
$ vi .bashrc
    [i]
    
    export COVERAGE=/home/student/.local
    export PATH=$JAVA_HOME/bin:$ANT_HOME/bin:$M2_HOME/bin:$COVERAGE/bin:/opt/bin:$PATH

    [ESC] [:] [w]
```
Now, start a new terminal (to activate your settings) and type:
```
$ coverage --version
Coverage.py, version 5.5 with C extension
Full documentation is at https://coverage.readthedocs.io
```

## Selenium

Selenium is a project for a range of tools and libraries that enable and support the automation of web browsers.

### Web Driver 
WebDriver drives a browser natively, as a user would, either locally or on a remote machine using the Selenium server, 
marks a leap forward in terms of browser automation.

Selenium WebDriver refers to both the language bindings and the implementations of the individual browser 
controlling code. This is commonly referred to as just WebDriver.

**Install Web Driver**:
* Download the binary package [geckodriver-v0.29.1-linux64.tar.gz](https://github.com/mozilla/geckodriver/releases) 
* Unzip the tar file and store the binary in a local directory:
    ```
    $ cd Downloads
    $ tar xvzf geckodriver-v0.29.1-linux64.tar.gz
    $ mkdir ~/local/webdriver
    $ mv geckodriver ~/local/webdriver/
    ```
* Add the webdriver directory to the PATH environment variable:
    ```
    $ vi ~/.bashrc
    [i]
    export WEBDRIVER=/home/student/local/webdriver/
    export PATH=$JAVA_HOME/bin:$ANT_HOME/bin:$M2_HOME/bin:$COVERAGE/bin:/opt/bin:$WEBDRIVER/:$PATH
    [ESC] [:] [w][q]
    ```

**Install the selenium module for Python**
    ```
    $ pip3 install selenium  
    ```

## Selenium IDE
Selenium IDE is an integrated development environment for Selenium tests. 
It is implemented as a Firefox extension, and allows you to record, edit, and debug tests.

**Install Selenium IDE addon for Firefox**:
* Using Firefox, vistit the page: https://addons.mozilla.org/en-US/firefox/addon/selenium-ide/
* Click the button **[Add to Firefox]**


## References
* [https://www.python.org/](https://www.python.org/)

* [Coverage.py](https://coverage.readthedocs.io/en/coverage-5.5/)

* [Selenium Browser Automation Project](https://www.selenium.dev/documentation/en/)

* [Selenium IDE - Getting Started](https://www.selenium.dev/selenium-ide/docs/en/introduction/getting-started)

*Egon Teiniker, 2020-2021, GPL v3.0*