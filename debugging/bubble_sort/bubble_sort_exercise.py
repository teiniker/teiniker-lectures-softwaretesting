# TODO: Debug the following implementation to make the bubble sort
#       algorithm work.
#       [5, 2, 1, 8, 4] => [1, 2, 4, 5, 8]

def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True


# Verify it works
random_list_of_nums = [5, 2, 1, 8, 4]
bubble_sort(random_list_of_nums)
print(random_list_of_nums)
