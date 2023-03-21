# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. 
# No two characters may map to the same character, but a character may map to itself.

# Input: s = "egg", t = "add"
# Output: true

# Input: s = "foo", t = "bar"
# Output: false

# Input: s = "paper", t = "title"
# Output: true

# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t consist of any valid ascii character.

s = "paper"
t = "title"

# find index of chars. example: 
# t_dict = {t: [0, 2], i: [1], l: [3], e: [4]}
# s_dict = {p: [0, 2], a: [1], e: [3], r: [4]}

def isIsomorphic(s: str, t:str) -> bool:
    if len(s) != len(t): 
        return False
    arr_len = len(s)
    s_dict, t_dict = {}, {}
    for i in range(arr_len):
        s_index_array = s_dict.get(s[i], [])
        t_index_array = t_dict.get(t[i], [])
        s_index_array.append(i)
        t_index_array.append(i)
        s_dict[s[i]] = s_index_array
        t_dict[t[i]] = t_index_array
        if [*s_dict.values()] != [*t_dict.values()]:
            return False

    print("\n", s_dict, "\n",t_dict)
    
    return True

def isIsomorphic2(s, t):
    # less runtime
    combined = []
    for i in range(len(s)):
        combined.append((s[i], t[i]))
    return len(set(combined)) == len(set(s)) == len(set(t))

def isIsomorphic3(s, t):
    # less runtime
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))

def isIsomorphic4(s, t):
    # less memory
    from collections import defaultdict
    if len(s) != len(t): return False
        
    translations = defaultdict(str)
    for char_s, char_t in zip(s,t):
        if char_s in translations:
            if translations[char_s] != char_t:
                return False
        else:
            translations[char_s] = char_t
    
    print("translation:", translations)
    if len(translations.values()) != len(set(translations.values())):
        return False
        
    return True


print(isIsomorphic(s, t))
print(isIsomorphic2(s, t))
print(isIsomorphic3(s, t))
print(isIsomorphic4(s, t))

