class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # top down DP: O(mn) time and space
        # inspired by: https://leetcode.com/problems/count-square-submatrices-with-all-ones/discuss/441620/DP-with-figure-explanation
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        ans = 0
        for row in range(m):
            for col in range(n):
                if matrix[row][col]: # if it's not 0
                    dp[row+1][col+1] = min(dp[row+1][col], dp[row][col+1], dp[row][col]) + 1
                    ans += dp[row+1][col+1]
        return ans
    
    
    # another great answer in O(1) space: https://leetcode.com/problems/count-square-submatrices-with-all-ones/discuss/643429/Python-DP-Solution-%2B-Thinking-Process-Diagrams-(O(mn)-runtime-O(1)-space)
