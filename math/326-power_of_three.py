# problem: find if the number is a power of 3. I.e., n = 3**x  where you don't know what x is
class Solution:
    def isPowerOfThree3(self, n):   # this is the fastest method
        # max 32-bit signed int is m = (2**32) / 2 - 1 . 3**(|log_3(m)|) = 3**(|19.56|) 
        # 3**19 = 1162261467. 3**20 would already be larger than the largest int value.
	    # we can simply check our result against the largest power of 3 (i.e., 3**19).
	    # return true if n value is bigger than 0 and there is no remainder between the largest power of 3 and this num
        return n > 0 and (3**19) % n == 0

    def isPowerOfThree(self, n):
        # brute force: make a power list with a for loop (max size is 20 so ~O(1) space)
        powers = [3**i for i in range(20)] # pow(3, i)
        return n in powers
    
    from math import log  # log is little slow, so it's not as fast as the uppermost solution
    def isPowerOfThree2(self, n: int) -> bool:
        if n <= 0: # fail cases
            return False
        # input 3**x = n , we know n. ->  x = log_3(n)
        x = log(n, 3)  # Ex: returns 3.0 from 8 because 2**3 = 8
        # round(float, DecPlaceToRoundTo), by default rounds to the closest int value
        # done to account for log sometimes returning answers like .9999999999 or .000000001
        if round(x + 0.000000000001, 10) == round(x): # 3 == 3.0? if there is no remainder
            return True
