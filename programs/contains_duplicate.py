# Problem:
# Given an integer array nums, 
# return true if any value appears at least twice in the array,
# and return false if every element is distinct.

def contains_duplicate(nums: list[int]) -> bool:
    # create a set
    num_set = set()

    for i in range(len(nums)):
        # if a number exists in set, we found a duplicate
        if nums[i] in num_set:
            return True
        # else add the number to the set
        num_set.add(nums[i])

    return False

# Driver Code
arr = [1, 2, 3, 4, 4, 5]
result = contains_duplicate(arr) 

print(result)



