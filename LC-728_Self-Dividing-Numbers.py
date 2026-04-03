# Solution: https://leetcode.com/problems/self-dividing-numbers/solutions/7643380/best-optimal-solution-full-explanation-j-f8o2/
# 728. Self Dividing Numbers

class Solution:
    def selfDividingNumbers(self, left, right):

        result = []

        for num in range(left, right + 1):
            if self.isDivisible(num):
                result.append(num)

        return result


    def isDivisible(self, num):

        temp = num

        while temp > 0:

            rem = temp % 10

            if rem == 0 or num % rem != 0:
                return False

            temp //= 10

        return True
