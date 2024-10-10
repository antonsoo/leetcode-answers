# 2024 Oct solution:
# note, it can possibly be optimized further by using a variable replacement method, thus saving space.
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        dict = {}
        dict[0] = 1
        dict[1] = 2
        for i in range(2, n):
            dict[i] = dict[i - 2] + dict[i - 1]
        return dict[n - 1]
        



# 2022 solution:
""" 70 - Climbing Stairs - 2022Q1: Amzn>>Expe>>Goog/Msft>etc
"""
class Solution:
    
    # memoization O(N) time and space
    def __init__(self):
        # define the values you get as output per each type of input, construct the rest from them
        # these are the number of steps you go (output) from climbing a particular number of steps (input)
        self.memo = {1:1, 2:2}

    def climbStairs2(self, n: int) -> int:
        #is n in memo already?: 
        #if n in self.memo:
        #    return self.memo[n]
        #base case, dont actually need these
        #elif n == 0 or n == 1:
        #    return 1
        #else:
        if n not in self.memo:
            # we can add the two prev numbers to make a current num and store
            self.memo[n] = self.climbStairs(n-2) + self.climbStairs(n-1)
        return self.memo[n]
    
    
    # DP solution O(N) time and space
    def climbStairs3(self, n: int) -> int:
        # take care of edge cases, small n (we're told it will at least be 1)
        if n == 1:
            return 1

        # n+1 range because we will first put in a zero, I think we don't have to do it but it's more intuitive when reading it
        dp = [i for i in range(n + 1)] 
        # base cases 
        dp[0], dp[1], dp[2] = 0, 1, 2 # 0 means no stairs
        
        for i in range(3, n + 1): # don't go through the first dummy variable, and the two we set
            dp[i] = dp[i - 2] + dp[i - 1]
        
        return dp[-1]
    
    
    
    # Fibonacci number solution: O(N) time, O(1) space
    def climbStairs(self, n: int) -> int:
        # edge case, small N
        if n == 1:
            return 1
        
        first, second = 1, 2
        for i in range(3, n + 1):
            # update the third value (the addition of the previous two)
            third = first + second 
            # move the first and second values along by one index
            first = second 
            second = third
        return second
    
    
    # other methods: 
    # Binets method: O(logn) time, O(1) space
    # Fibonacci formula: O(logn) time, O(1) space


