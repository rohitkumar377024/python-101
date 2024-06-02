# Problem:
# Given an array of integers nums and an integer target, 
# return indices of two numbers such that add up to the target.

def twoSum(nums, target):
    # create a hashmap
    prevMap = {} # val : index

    for i, n in enumerate(nums):
        # if complement exists in hashmap
        # return indices for number and complement
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        # else add the number in hashmap with its index
        prevMap[n] = i

# Driver Code
nums = [2,7,11,15]
target = 9

result = twoSum(nums, target)
print(result)



 