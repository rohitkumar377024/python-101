# Problem:
# Given two strings s and t, 
# return true if t is an anagram of s, and false otherwise.

def valid_anagram(s: str, t: str) -> bool:
    # if lengths don't match, not valid anagram
    if len(s) != len(t):
        return False
    
    # check occurrence count for each element of s and t
    hash_s = {}
    for char in s:
        if char in hash_s:
            hash_s[char] += 1
        else:
            hash_s[char] = 1

    hash_t = {}
    for char in t:
        if char in hash_t:
            hash_t[char] += 1
        else:
            hash_t[char] = 1

    # if hashset for s and t are same, then valid anagram
    return hash_s == hash_t

# Driver Code
s = 'aacc'
t = 'ccac'

result = valid_anagram(s, t)
print(result)



 