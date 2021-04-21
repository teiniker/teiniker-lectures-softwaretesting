# Python Tools & Libraries Setup


## Coverage.py
Coverage.py is a tool for **measuring code coverage** of Python programs. 

It monitors your program, noting which parts of the code have been executed, 
then analyzes the source to identify code that could have been executed but 
was not.
```
$ pip3 install coverage
```

```
$ vi .bashrd
    export COVERAGE=/home/student/.local
    export PATH=$JAVA_HOME/bin:$ANT_HOME/bin:$M2_HOME/bin:$COVERAGE/bin:/opt/bin:$PATH
```

```
$ coverage --version
Coverage.py, version 5.5 with C extension
Full documentation is at https://coverage.readthedocs.io
```

## References
* [Coverage.py](https://coverage.readthedocs.io/en/coverage-5.5/)