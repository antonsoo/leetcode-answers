class Solution:
    # 121. https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    # one pass: O(n) time, O(1) space, I think
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf') # math.inf
        max_profit = 0
        for price in prices:
            diff = price - min_price
            if price < min_price: # if it's the smallest value we've seen
                min_price = price
            elif diff > max_profit: # if it's not the smallest value we've seen *and* 
                max_profit = diff
        return max_profit
