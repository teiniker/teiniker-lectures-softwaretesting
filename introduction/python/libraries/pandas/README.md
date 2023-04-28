# Pandas

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

