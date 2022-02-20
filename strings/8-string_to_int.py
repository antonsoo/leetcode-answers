""" 8. String to Integer. "Medium" (I think it's very easy). Facebook>>Microsft>Amazon>Google>etc
- problem: convert a string to myatoi according to the 6 rules given.
"""
class Solution:
    # O(len(s))->O(n) time. O(len(num))->O(1)? space assuming the num is not much larger/smaller than max int values.
    def myAtoi(self, s: str) -> int:
        s = s.strip() # 1) ignore any leading whitespaces. assuming we can overwrite input.
        
        # edge case:
        if len(s) == 0: # null string
            return 0
        
        # 2) keep track of pos or neg
        sign = 1 # keep track of pos or neg
        start = 0 # keep track starting index of the integer in the stripped string
        if s[0] == "-":
            sign = -1
            start += 1
        elif s[0] == "+": # dont change the sign
            start += 1

        numstr = ""
        for i in range(start, len(s)): # 3) read num until the end
            if s[i].isnumeric(): # also can be done like: if ch is in "1234567890"
                numstr += s[i]
            else: 
                break
        
        if len(numstr) == 0: # 4) nothing was read
            return 0
        
        ans = sign * int(numstr) # 5) convert
        
        # 6) out of range, clamp
        if ans > 2**31 - 1:
            ans = 2 ** 31 - 1
        elif ans < -2**31:
            ans = -2**31
            
        return ans
