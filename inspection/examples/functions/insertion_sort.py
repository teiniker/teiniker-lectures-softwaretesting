"""
Example used to measure software metrics via radon:
    CCN = 5
    LOC: 21
    LLOC: 13
"""
def insertion_sort(data):
    """
    Implementation of the assertion sort algorithm.
    Sort the given list data.
    """
    for j in range(1, len(data)):
        key = data[j]
        i = j - 1
        while (i >=0) and (data[i] > key):
            data[i+1] = data[i]
            i = i - 1
        data[i+1] = key


x = [2,7,3,8,1]
insertion_sort(x)
print(x)
