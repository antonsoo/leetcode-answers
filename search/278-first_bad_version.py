""" 278 - first bad version - easy - search -  2022Q1: Goog>FB>Amzn>etc
- find the "bad version," it's the True value that returns from the API function call
- every other value after the "bad version" will also return as True, i.e., they will all be bad version (on the right hand side)
"""

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
class Solution:
    # O(log(n)) time, O(1) space
    def firstBadVersion(self, n: int) -> int:
        L = 1
        R = n
        while L < R:
            midpoint = L + (R - L) // 2  # this is better than (L+R)//2
            # if we find the badVersion (the True) value, then we check everything from L to that midpoint we just found it at
            # so what we're doing is we're trying to find the next badVersion to the left of this midpoint, 
            #the first value that changed all the rest, so we know everything to the left of R is already True
            if isBadVersion(midpoint): # == True
                R = midpoint # reset the midpoint to be on the left
            # this is we don't find a True value, the bad version, the algorithm will continue cutting down our search 
            #to search on more and more of the right side (right of L), but before L
            # IF WE never find the next or any True value, the L will eventually equal R, the first bad version we found
            else: # isBadVersion(midpoint) == False
                L = midpoint + 1
        return L # returns the last bad version we found (after changing L many times)
    
    
    # linear scan: O(n) time, O(1) space
    def firstBadVersion2(self, n: int) -> int:
        for i in range(1, n + 1):
            if isBadVersion(i): # returns True if the current version is bad
                return i # returns the version number that's bad/matched as True
        return n # last one is the bad version (we assumed there is at least one bad version)
    
    
    
        
    # efficient Python library call
    import bisect
    def __getitem__(self, i: int):
        return isBadVersion(i)
    def firstBadVersion3(self, n: int):
        return bisect.bisect_left(self, True, 1, n)
    
        
            
            
