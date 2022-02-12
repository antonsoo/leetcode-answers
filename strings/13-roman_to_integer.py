"""
- problem: convert a roman numerals string to an integer
- solution: go in twos if a value in front is smaller than the value after it, then subtract the largest - smallest. otherwise, add them and go one place forward.
- note: in my solution you can also put the two if's into one and two elses into one, but you'd need to get rid of the "nxt" value because you can't assign it before the if check.
- complexity: O(n) time-> O(1) time because max roman numeral is 3999, O(1) space because len(d) = 7
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        # define a dictionary of definitions of the symbols/chars to integers
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0 # output, i.e., the sum
        
        # iterate through the string, from highest values to lowest, in twos
        #if a value in front is smaller than the value after it, then subtract the largest -             smallest otherwise, add them.
        i = 0
        while i < len(s):
            curr = d[s[i]] # gets the actual int definitions for the roman vals
            if i + 1 < len(s): 
                nxt = d[s[i + 1]] # 1st) out-of-bounds check, so when computing the number in this second condition, we dont get an error.
                if curr < nxt: # 2nd) actually do the check of val in front being smaller than the next value. If so, add them.
                    print("here")
                    diff = nxt - curr 
                    total += diff
                    i += 2  # skip by two places because we've added
                else: # the number in front is bigger, just add and move along by 1
                    total += curr
                    i += 1         
            else: # only one number is left 
                total += curr
                i += 1
        
        return total
