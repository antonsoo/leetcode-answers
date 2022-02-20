# 7. Easy (noted as Medium on leetcode)
# O(1) time and space because we know n will always be a small constant 
# one of the runtimes I got is 99% faster than all Python solutions
# note: we don't care about input being too big because we will reverse it
class Solution:
    def reverse(self, x: int) -> int: 
        rev = int(str(abs(x))[::-1]) # reversed, abs value so we dont reverse a neg sign
        if abs(rev) >= 2**31 - 1: # output int value is too big or too small
            return 0
        if x < 0: # negative
            return rev * -1
        else:
            return rev
          
   # the official solution is in O(log(n)) time... which actually it should be in O(1) time technically.. I believe
