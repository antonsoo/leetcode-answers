class Solution:
    # LC-242. Valid Anagram (Aug 18, 2026)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict, t_dict = {}, {}

        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1
            # or do it in one line by: s_dict[char] = s_dict.get(char, 0) + 1

        for char in t:
            if char in t_dict:
                t_dict[char] += 1
            else:
                t_dict[char] = 1
            # or do it in one line by: t_dict[char] = t_dict.get(char, 0) + 1
            
        
        return s_dict == t_dict


    ###### solution of doing the above but with a single string:
    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = {}

        for s_char, t_char in zip(s, t):
            counts[s_char] = counts.get(s_char, 0) + 1
            counts[t_char] = counts.get(t_char, 0) - 1

        return all(count == 0 for count in counts.values())


    ###### the most Pythonic solution:
    ###### must first import Counter, like: 
    ###### from collections import Counter
    def isAnagram3(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
