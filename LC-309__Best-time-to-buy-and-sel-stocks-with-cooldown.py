# Problem: 309. Best Time to Buy and Sell Stock with Cooldown
# Answer [?]: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solutions/761981/pythongojavajsc-on-by-dp-and-state-machi-76cy/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = -10 ** 9
        s = 0
        s2 = 0      # s[i - 2]
        for i in range(len(prices)):
            b = max(b, s2 - prices[i])
            s2 = s  # update s[i - 2] for next iteration
            s = max(s, b + prices[i])
        return s
