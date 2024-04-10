# Operating System Interfaces

The **OS module** in Python provides functions for interacting with the operating system. 
OS comes under Python’s standard utility modules. 
This module provides a portable way of using operating system dependent functionality. 
The **os** and **os.path** modules include many functions to interact with the file system.

## Working with Files

* **os.path.exists('filename')**\
    Check wheter a file exists or not by passing the name of the file as a parameter.

* **os.path.getsize('filename')**\
    Give the size of a file in bytes.     
    To use this method we need to pass the name of the file as a parameter.

* **os.remove('filename')**\
    Remove a file from the filesystem.
    To remove a file we need to pass the name of the file as a parameter. 


## Working with Directories

* **os.getcwd()**\
    Get the location of the current working directory.
    Consider **Current Working Directory(CWD)** as a folder, where the Python is operating. Whenever the files are called only by their name, Python assumes that it starts in the CWD which means that name-only reference will be successful only if the file is in the Python’s CWD.

* **os.chdir('path')**\
    Change the current working directory.
    The method only takes a single argument, the new directory path.

* **os.mkdir('path')**\
    Create a directory named path with the specified numeric mode. 
    This method raise FileExistsError if the directory to be created already exists.

* **os.makedirs('path')**\
    Create a directory recursively. 
    That means while making leaf directory if any intermediate-level directory is missing, os.makedirs() method will create them all.

* **os.listdir('path)**\
    Get the list of all files and directories in the specified directory. 
    If we don’t specify any directory, then list of files and directories in the current working directory will be returned.

* **os.rmdir('path')**\
    This operation is used to remove or delete a empty directory. 
    OSError will be raised if the specified path is not an empty directory.


## High-Level File Operations

The **shutil module** offers a number of high-level operations on files and collections of files.

* **shutil.copyfile('src-path', 'dst-path')**\
    Copy the contents (no metadata) of the file named src to a file named dst and return dst in the most efficient way possible. src and dst are path-like objects or path names given as strings.
    The destination location must be writable; otherwise, an OSError exception will be raised.

* **shutil.rmtree(path)**\
   Delete an entire directory tree; path must point to a directory.



## References
* [OS Module in Python with Examples](https://www.geeksforgeeks.org/os-module-python-examples/)

* [OS — Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html)

* [shutil — High-level file operations](https://docs.python.org/3/library/shutil.html#module-shutil)
