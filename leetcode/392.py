# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 
# of the characters without disturbing the relative positions of the remaining characters. 
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true

# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false

# Example 3:
# Input: s = "aec", t = "abcde"
# Output: false

# Example 4:
# Input: s = "ace", t = "abcde"
# Output: true
 
# Constraints:
# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.
 

# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?

s = "aec"
t = "abcde"

def isSubsequence(s: str, t: str) -> bool:
    if len(s) > len(t):return False
    if len(s) == 0:return True
    subsequence=0
    for i in range(0,len(t)):
        if subsequence <= len(s) -1:
            if s[subsequence]==t[i]:
                subsequence+=1

    return  subsequence == len(s)

def isSubsequence2(s, t):
    # less runtime
    t = iter(t)
    for char in s:
        print(char)
    return all(char in t for char in s)

def isSubsequence3(s, t):
    # less memory
    if len(s) == 0:
        return True
    if len(s) > len(t):
        return False
    window = ""
    i = 0
    k = 0
    while k < len(t):
        window += t[k]
        if s[i] in window:
            window = ""
            i += 1
            if i == len(s):
                return True
        k += 1
    return False


print(isSubsequence(s, t))
print(isSubsequence2(s, t))
print(isSubsequence3(s, t))