# TODO: Debugging
# A) Locate the bug by inserting log statements.
# B) Fix the bug.

def list_count_element(nums, e):
    count = 0
    for n in nums:
        if n == e:
            count += count + 1
    return count

numbers = [5, 2, 1, 8, 4, 3, 7, 1, 1, 4]
count = list_count_element(numbers, 1)
print('Count of elements = {}'.format(count))


