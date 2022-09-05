# 409. Longest Palindrome - "easy" - 2022Q3: Amzn
# Problem: Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
# idea: count the number of letters, store the count in a dict
# only allow/count the odd letters once. i.e, only have one of 
#the odd letters be counted. 
# Can still count the letter if it can be cut off to the even number.
# Add the leftover at the end to allow one odd letter.

from collections import Counter
class Solution:
    # O(N)  time, O(1) space
    def longestPalindrome(self, s: str) -> int:
        length = 0
        odd = False # finds if there is at least one odd value
        counts = Counter(s)
        #print(counts)
        for value in counts.values():
            if value % 2 == 0: # even number
                length += value
            else:
                length += (value - 1) # add the even part 
                odd = True
        if odd == True: # add the leftover if there is one
            length += 1
        return length
    
    
    
    
    # official solution: (Only works on Python2)
    def longestPalindrome2(self, s):
        ans = 0
        for v in collections.Counter(s).itervalues():
            ans += v / 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans
        
    def longestPalindrome3(self, s):    # Py3 ver
        ans = 0
        for v in collections.Counter(s).values():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans

        
