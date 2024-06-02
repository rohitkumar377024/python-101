# Problem:
# Given an array of integers nums and an integer target, 
# return indices of two numbers such that add up to the target.

def twoSum(nums, target):
    # create a hashmap
    hashmap = {}

    for i in range(len(nums)):
        # if complement exists in hashmap
        # return indices for number and complement
        complement = target - nums[i]
        if complement in hashmap.keys():
            return [hashmap[complement], i]
        # else add the number in hashmap with its index
        else:
            # print('Not Exists')
            hashmap[nums[i]] = i

# Driver Code
nums = [2,7,11,15]
target = 9

result = twoSum(nums, target)
print(result)



 