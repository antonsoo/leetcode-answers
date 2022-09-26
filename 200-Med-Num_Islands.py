# 200. Number of Islands - Med - 2022:Amzn/Bloom/Goog/etcetcetc

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # O(M x N) time and space compl. M = row #, N = col #
        if not grid: # if it's empty
            return 0

        count = 0
        for i in range(len(grid)): # x-axis
            for j in range(len(grid[0])): # y-axis
                if grid[i][j] == '1':
                    self.dfs(grid, i, j) # gets rid of all 1's connected to that "1"
                    count += 1 # increments the counter
                    # goes back up to the loop and repeats if it didn't terminate
        return count 

    def dfs(self, grid, i, j):
        # check that nothing is out of bounds and not zero or something else
        # can also make the condition below the opposite, and put everything below under it
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return # if the if condition is met, the function doesn't return (returns None), just stops running
        # now modify all adjacent island pieces ("1"'s) into something else so we don't count it again when we do our loop
        grid[i][j] = '#' # can make this anything, like -1, or any char, this will let us skip this part of the grid next time we look at it
        # search left/right/up/down
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
