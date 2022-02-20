"""  387 - Easy -  First Unique Character in a String
- problem : return the first unique char in a string
"""
from collections import Counter
class Solution:
    # can also perhaps optimize this solution by removing or poping values we've already seen multiple times
    def firstUniqChar(self, s: str) -> int:
        charCounts = {}  #dictionary to keep of track of chars we've seen, dict has O(1) search time
        for i in range(len(s)):
            if s[i] in charCounts: # s[i] is the current char   # dict search is O(1)
                charCounts[s[i]][1] += 1
            else:
                # seeing it for the first time, add the entry: dictionary[key=char] = [index, count]
                charCounts[s[i]] = [i, 1]
        for key, vals in charCounts.items(): 
            if vals[1] == 1: # if the char was only seen 1 time
                return vals[0] # return the index of that char
        return -1 # no unique chars
    
    
    # this function just returns the letters, not indices 
    def firstUniqChar1(self, s: str) -> int:
        #seen = {}  #dictionary to keep of track of chars we've seen, dict has O(1) search time
        counts = Counter(s)
        print(counts) # print will actually print it from greatest to smallest, but dictionaries actually preserve the order in which the items appear in the input... if you want to print and preserve the order, do print(dict(counter))
        for key, val in counts.items():
            if val == 1: # finds the first one that returns
                return key
        return -1 # no unique chars

    
    """  not that actual problem, I didn't read carefully haha
    - problem : return the first repeating char
    """
    def firstRepeating2(self, s: str) -> int:
        seen = {} # dictionary to keep of track of chars we've seen, dict has O(1) search&access time, better than a string or a list. That's why we want to use a dict.
        for ind, ch in s:
            if ch in seen: # O(1) 
                return ind # return the index as the problem states
            else:
                seen[c] = 1 # can set the val to anything
        return 
