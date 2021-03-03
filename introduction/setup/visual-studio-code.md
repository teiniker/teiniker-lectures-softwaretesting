# Visual Studio Code for Python

Visual Studio Code is a **source code editor** with support for development operations like debugging, 
task running, and version control. 
It aims to provide just the tools a developer needs for a quick code-build-debug cycle.

![Visual Studio Code](figures/VS-Code.png)

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
 
## Setup VS Code for Python

* Install the **Python Extension** from Microsoft (**ms-python.python**) including 
  the **pylint** package.
* Select your **Python interpreter** by clicking on the VS Code **status bar**: `/bin/python3`
* Configure the **debugger** through the **Debug Activity Bar**: create a `launch.json` file: 
 ```      
    launch.json 
    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Python: Current File",
                "type": "python",
                "request": "launch",
                "program": "${file}",
                "console": "integratedTerminal",
                "cwd": "${fileDirname}"
            }
        ]
    }	
```       

## References
* [Visual Studio Code](https://code.visualstudio.com/)

*Egon Teiniker, 2020-2021, GPL v3.0*