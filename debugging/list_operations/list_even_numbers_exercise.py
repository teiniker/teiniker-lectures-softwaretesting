# TODO: Debugging
# A) Locate the bug by using an interactive debugger.
# B) Fix the bug.

def list_even_numbers(nums):
    result = []
    for n in nums:
        if n % 2 == 0:
            result = n
    return result

numbers = [5, 2, 1, 8, 4]
even = list_even_numbers(numbers)
print('Even elements = {}'.format(even))


