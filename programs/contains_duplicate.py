# Problem:
# Given an integer array nums, 
# return true if any value appears at least twice in the array,
# and return false if every element is distinct.

def contains_duplicate(nums: list[int]) -> bool:
    # create a set
    hashset = set()

    for n in nums:
        # if a number exists in set, we found a duplicate
        if n in hashset:
            return True
        # else add the number to the set
        hashset.add(n)

    return False

# Driver Code
arr = [1, 2, 3, 4, 4, 5]
result = contains_duplicate(arr) 

print(result)



