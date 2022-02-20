""" 125. Valid Palindrome - "Easy" - Facebook/Microsoft/etc
- problem: valid palindrome, NOTE: without caring about the case AND non-alphanumeric characters (skip all the non-alphanumeric chars). Note: "5".lower() = "5" 
- Can also filter the list but it would waste space:
filtered_chars = filter(lambda ch: ch.isalnum(), s)
lowercase_filtered_chars = map(lambda ch: ch.lower(), filtered_chars)
"""
class Solution:
    # O(n/2)->~O(n) time, O(1) space
    def isPalindrome(self, s: str) -> bool:
        # note in Python we can also use str.isalnum() or str.isalpha() or str.isnumeric()
        # random note: isinstance(n, int) or type(n) will check the type of integer n
        alphanum = "abcdefghijklmnopqrstuvwxyz0123456789" 
        
        if len(s) == 2:
            ch1, ch2 = s[0].lower(), s[1].lower()
            if ch1 not in alphanum or ch2 not in alphanum:
                return True
            return ch1 == ch2
        
        # intialize the left and right pointers:
        p1 = 0 # left pointer
        p2 = len(s) - 1 # right pointer
        while p1 < p2:
            # chars on either side of the string, left and right
            ch1, ch2 = s[p1].lower(), s[p2].lower() # need to be lowercase as the problem states
            # first skip the non-alphanum chars, but don't go out of bounds
            if ch1 not in alphanum and p1 < len(s):
                p1 += 1  
                continue # or reassign the new ch1 # ch1 = s[p1].lower() 
            if ch2 not in alphanum and p2 > 0:
                p2 -= 1
                continue # or reassign
            # then compare the two halves
            elif ch1 == ch2:
                p1 += 1
                p2 -= 1
                continue
            else:
                return False
        return True
