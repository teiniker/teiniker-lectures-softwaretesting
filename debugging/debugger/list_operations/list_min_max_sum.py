
def list_min(nums):
    min = nums[0]
    for n in nums:
        if n < min:
            min = n
    return min

def list_max(nums):
    max = nums[0]
    for n in nums:
        if n > max:
            max = n
    return max

def list_sum(nums):
    sum = 0
    for n in nums:
        sum += n
    return sum

numbers = [5, 2, 1, 8, 4]

min = list_min(numbers)
max = list_max(numbers)
sum = list_sum(numbers)
print('min = {}, max = {}, sum = {}'.format(min, max, sum))


