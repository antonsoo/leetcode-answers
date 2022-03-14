""" 198 - House Robber - Medium (easy?) - 2022Q1: Amzn>>Appl>Cisc>Goog>etc 
- you're not keeping track of which houses were robbed, just the max value.
- don't hit houses adjacent to one another.
"""
class Solution:
    # O(n) time, O(1) space
    def rob(self, nums: List[int]) -> int:
        # official answer:
        prevMax, currMax = 0, 0
        for num in nums:
            # the current_max is max value between the current_max or previous_Max + current_number 
            #temp = currMax
            prevMax, currMax = currMax, max(currMax, prevMax + num) # the pythonic way needs no temps
            #prevMax = temp
        return currMax
    
    
    # dp solution : O(N) time, O(N) space
    def rob2(self, nums: List[int]) -> int:
        # Special handling for empty case.
        if not nums:
            return 0

        maxRobbedAmount = [None for _ in range(len(nums) + 1)]
        N = len(nums)
        # Base case initialization.
        maxRobbedAmount[N], maxRobbedAmount[N - 1] = 0, nums[N - 1]
        # DP table calculations.
        for i in range(N - 2, -1, -1):
            # Same as recursive solution.
            maxRobbedAmount[i] = max(maxRobbedAmount[i + 1], maxRobbedAmount[i + 2] + nums[i])
        return maxRobbedAmount[0]   
    
    
    # optimized DP (basically same as my first solution^): O(N) time, O(1) space
    def rob3(self, nums: List[int]) -> int:
        # Special handling for empty case.
        if not nums:
            return 0
        N = len(nums)
        rob_next_plus_one = 0
        rob_next = nums[N - 1]
        # DP table calculations.
        for i in range(N - 2, -1, -1):
            # Same as recursive solution.
            current = max(rob_next, rob_next_plus_one + nums[i])
            # Update the variables
            rob_next_plus_one = rob_next
            rob_next = current  
        return rob_next
        
    
    
    # memoization solution: O(N) time and space
    def __init__(self):
        self.memo = {}
    def rob2(self, nums: List[int]) -> int:
        self.memo = {}
        return self.robFrom(0, nums)
    def robFrom(self, i, nums):
        # No more houses left to examine.
        if i >= len(nums):
            return 0
        # Return cached value.
        if i in self.memo:
            return self.memo[i]
        # Recursive relation evaluation to get the optimal answer.
        ans = max(self.robFrom(i + 1, nums), self.robFrom(i + 2, nums) + nums[i])
        # Cache for future use.
        self.memo[i] = ans
        return ans
