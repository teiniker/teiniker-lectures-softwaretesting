
def list_even_numbers(nums):
    result = []
    for n in nums:
        if n % 2 == 0:
            # Bug: result = n
            result.append(n)
    return result

numbers = [5, 2, 1, 8, 4]
even = list_even_numbers(numbers)
print('Sum of elements = {}'.format(even))


