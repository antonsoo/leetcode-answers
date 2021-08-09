class Solution:
     def uniquePaths2(self, m: int, n: int) -> int:
        # O(nm) time, O(nm) space
        paths = [[1] * n for _ in range(m)] # make m rows of n  columns
        for row in range(1, m):
            for col in range(1, n):
                paths[row][col] = paths[row - 1][col] + paths[row][col - 1]
        return paths[-1][-1]
    
     def uniquePaths(self, m, n):
        # O(mn) time, O(n) space 
        if not m or not n:
            return 0
        current = [1] * n
        for row in range(1, m):
            for col in range(1, n):
                current[col] += current[col-1]
        return current[-1]
