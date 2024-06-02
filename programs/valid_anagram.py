# Problem:
# Given two strings s and t, 
# return true if t is an anagram of s, and false otherwise.

def valid_anagram(s: str, t: str) -> bool:
    # create new sets of s and t
    s_set = set(s)
    t_set = set(t)

    # if lengths don't match, not valid anagram
    if len(s_set) != len(t_set):
        return False

    # else check if every set element of s exist in set of t
    for item in s_set:
        if item not in t_set:
            return False

    return True

# Driver Code
s = 'anagram'
t = 'nagaram'

result = valid_anagram(s, t)
print(result)



 