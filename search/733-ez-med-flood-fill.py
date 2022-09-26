# 733. Flood Fill - Ez/Med - 2022Q3: Amzn/Msft/etc...
# (sr, sc) are the coordinates. Fill everything (change everything to the number 'color') connected 4-directionally. But what you fill must also be of the same color as the original first pixel you fill. Note: there could be no fill required if it's the same already.
# Note: DFS requires stack space of O(mn) while BFS requires queue space of only O(min(m, n)).

class Solution:
    # dfs solution: O(MN) time and space
    def floodFill2(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig_color = image[sr][sc] # color to replace; don't replace others. Even if they're connected 4-directionally. 
        # fail case: nothing to fill cuz it's already filled in the desired color
        if orig_color == color: return image
        
        x_len, y_len = len(image), len(image[0]) 
        def dfs(x, y):
            if image[x][y] == orig_color: # only fill pixels that [had] the original color
                image[x][y] = color # modified the color
                # now try to run the same function We/S/E/N. Checking bounds each time.
                if x > 0: dfs(x - 1, y)
                if y > 0: dfs(x, y - 1)
                if x + 1 < x_len: dfs(x + 1, y)
                if y + 1 < y_len: dfs(x, y + 1)
        dfs(sr, sc)
        return image # return the same image we've modified
    
    
    
    
    # bfs solution: O(MN) time and O(min(M,N)) space, I believe. thx to user yanshengjia
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig_color = image[sr][sc] # color to replace; don't replace others. Even if they're connected 4-directionally. 
        # fail case: nothing to fill cuz it's already filled in the desired color
        if orig_color == color: return image
        x_len, y_len = len(image), len(image[0]) 
        queue = [(sr, sc)] # instantiate and initialize the queue
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # W, E, N, S 
        while len(queue) > 0:
            x, y = queue.pop()  # current = queue.pop() # current[0], current[1]  
            # test the boundary condition for those current coordinates:
            if 0 <= x < x_len and 0 <= y < y_len \
                    and image[x][y] == orig_color and image[x][y] != color:
                image[x][y] = color
                # can also do this manually: Just append every neighbor to the queue.
                neighbors = [(x + direct[0], y + direct[1]) for direct in directions]
                queue.extend(neighbors)
        return image
    
    
    
    # my wrong attempt:
    def floodFill2(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        x_len, y_len = len(image), len(image[0])
        orig_color = image[sr][sc] # color to replace; don't replace others. Even if they're connected 4-directionally.
        
        for x in range(x_len):
            for y in range(y_len):
                self.bfs(sr, sc, image, color, orig_color)
        
    # runs bfs: (x, y) are the coordinates to run from, x_l and y_l are bounds.... I think this is dfs not bfs:
    def bfs2(self, x, y, array, color, orig_color):
        x_len, y_len = len(array), len(array[0])
        #while (x > 0, y > 0, x < x_len, y < y_len): # check bounds
        if x - 1 > 0 and y < y_len and array[x - 1][y] == orig_color:
            array[x - 1][y] = color # update the color
            bfs(x - 1, y, array, color, orig_color)
        if x + 1 < x_len and y < y_len and array[x + 1][y] == orig_color:
            array[x + 1][y] = color # update the color
            bfs(x + 1, y, array, color, orig_color)
        if y - 1 > 0 and x < x_len and array[x][y - 1] == orig_color:
            array[x][y - 1] = color # update the color
            bfs(x, y - 1, array, color, orig_color)
        if y + 1 < y_len and x < x_len and array[x][y + 1] == orig_color:
            array[x][y + 1] = color # update the color
            bfs(x, y + 1, array, color, orig_color)
            
