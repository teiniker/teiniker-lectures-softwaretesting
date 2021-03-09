# TODO: Debugging
# A) Locate the bug by using systematic debugging techniques.
# B) Fix the bug.
def insertion_sort(arr):  
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j] = key 

# Verify 
list_of_nums = [5, 2, 1, 8, 4]
insertion_sort(list_of_nums)
print(list_of_nums)
assert list_of_nums == [1, 2, 4, 5, 8]