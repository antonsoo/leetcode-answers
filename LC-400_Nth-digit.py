p# Problem link: 400. Nth Digit (Medium)
# Solution link: https://leetcode.com/problems/nth-digit/solutions/7677620/nth-digit-mathematical-index-mapping-dig-cb6i/

class Solution:
    def findNthDigit(self, n: int) -> int:

        digit = 1
        start = 1
        count = 9

        while n > digit * count:
            n -= digit * count
            digit += 1
            start *= 10
            count *= 10

        number = start + (n - 1) // digit

        return int(str(number)[(n-1) % digit])
