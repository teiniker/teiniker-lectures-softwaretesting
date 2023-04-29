# Pandas

Python Pandas is a widely used open-source data manipulation and analysis library. It provides powerful data structures and data analysis tools for efficiently working with structured data. 

Pandas offers a wide range of functionality, including **data manipulation, cleaning, filtering, reshaping, merging, grouping, and aggregating data**. 
It provides flexible indexing and slicing capabilities, making it convenient to access and modify data. Additionally, pandas supports reading and writing data in various formats such as CSV, Excel, SQL databases, and more.

Pandas is built on top of the **NumPy** library and provides two primary data structures: 

* A **Series** is a one-dimensional labeled array capable of holding any data type. It is similar to a column in a spreadsheet or a traditional database table. Each value in a Series is associated with a unique label or index.

* A **DataFrame** is a two-dimensional table of data with rows and columns. It is similar to a spreadsheet or a SQL table. A DataFrame can be thought of as a collection of Series objects, where each Series represents a column of the DataFrame.


## Data Frame


## Comma Separated Values (CSV) Files 

import pandas as pd

df = pd.read_csv("file.csv")

df.head(number_of_lines)
df.tail(number_of_lines)


## Tab Separated File

df = pd.read_csv("file.txt", delimiter='\t')



## Excel Files 

df = pd.read_excel("file.xlsx")

## Setup Pandas

```
$ pip3 install pandas
$ pip3 install openpyxl
```

## References
* [YouTube (Keith Galli): Complete Python Pandas Data Science Tutorial!](https://youtu.be/vmEHCJofslg)

* [Pandas: User Guide](https://pandas.pydata.org/docs/user_guide/index.html)
