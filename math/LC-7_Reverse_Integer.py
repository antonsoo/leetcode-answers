# Date(s) worked on & submitted: Sep 19-20, 2025
# LC # 7: "Reverse Integer"
# Problem link: https://leetcode.com/problems/reverse-integer/
# Solution link: https://leetcode.com/problems/reverse-integer/solutions/5428589/video-using-remainder
class Solution:
    # One of many many solutitons:
    def reverse(self, x: int) -> int:
        is_negative = False

        if x < 0:
            is_negative = True
            x *= -1
        
        res = 0
        while x > 0:
            res = (res * 10) + (x % 10)
            x //= 10
        
        if res > 2 ** 31 - 1:
            return 0
        
        return res * -1 if is_negative else res
                

########################################################################
#########################################################################
# Very old submission:
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
