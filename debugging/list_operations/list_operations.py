
def sum_of_listelements(nums):
    sum = 0
    for n in nums:
        sum += n
    return sum

numbers = [5, 2, 1, 8, 4]
sum = sum_of_listelements(numbers)
print("Sum of elements: :", sum)


