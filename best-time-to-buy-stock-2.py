# 122. Best Time to Buy and Sell Stock II
# O(n) time, O(1) space I believe
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            profit += max(prices[i] - prices[i - 1], 0)
        return profit
