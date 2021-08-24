class Solution:
    def fib2(self, n: int) -> int:
        # dp solution: O(n) time and space
        if n == 0:
            return 0
        elif n == 1:
            return 1
        # because we'll be returning dp[n], we need to have our list be of size n+1
        # this is since the 0th index will be = 0, and 1'th will be 1 and so on
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[n]
    
    def fib(self, n: int) -> int:
        # recursive solution: O(2**n) time and O(n) space
        # this code will go from 1 to n+1 to account for the input index not starting at 0 like normal
        if n == 0:
            return 0
        elif n == 1:
            return 1
        return self.fib(n-1) + self.fib(n-2)
