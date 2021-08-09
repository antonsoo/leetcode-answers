class Solution:
     def uniquePaths(self, m: int, n: int) -> int:
        # O(nm) time, O(nm) space
        paths = [[1] * n for _ in range(m)] # make m rows of n  columns
        for col in range(1, m):
            for row in range(1, n):
                paths[col][row] = paths[col - 1][row] + paths[col][row - 1]
        return paths[-1][-1]
