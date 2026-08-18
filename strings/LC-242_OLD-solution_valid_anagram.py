""" 242. Valid Anagram. Best compl. so far: 94% faster, 77% space
- problem: Validate if two words are anagrams. 
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
class Solution:
    # O(s+t) time, O(1) space because there are only 26 letters for each word. O(c)->O(1)
    from collections import Counter
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = Counter(s) # count the occurences of each char in the first word
        d2 = Counter(t) # count the occurences of each char in the second word
        if len(d1) != len(d2): # we already know their chars are not the same
            return False 
        for ch, count in d1.items():
            if ch not in d2: # the key (char) doesn't exist in the second word 
                return False
            elif d1[ch] == d2[ch]: # equal counts for that char
                continue
            else:
                return False
        return True
    
    # actually this can be done in one line:
    # like this:
    #return collections.Counter(s) == collections.Counter(t)
