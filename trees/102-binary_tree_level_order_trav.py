""" 102 - Binary Tree Level-Order Traversal
- traverse the tree level by level (up to down, right to left), append it to a list of levels and return it
- solution: append the current value to the appropriate level and call the function recursively on its children
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # recursive sol: O(N) time and space
    def levelOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        # initialize the output array
        levels = []
        
        # edge case, empty input
        if not root: 
            return levels
        
        def traverse(node: Optional[TreeNode], level: int) -> None: # level is the current level, an int value
            if len(levels) == level:
                levels.append([]) # add a new array representing a new level
            
            # append the current value
            levels[level].append(node.val)
            
            # do the same thing on the left and right children if they exist
            L, R = node.left, node.right
            if L: traverse(L, level + 1)
            if R: traverse(R, level + 1)
        
        traverse(root, 0) # start with the root and levels 0
        return levels
    
    
    # iterative solution, we will use a deque because a queue will add extra features which will slow down the performance
    # "overkill since it's designed for a safe exchange between multiple threads and hence requires locking"
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = [] # initialize the output
        if not root: return levels  # edge case, empty input
        
        level = 0 # initialize the current level variable 
        queue = deque([root, ]) # keep the current values in a deque
        while queue:
            levels.append([]) # start the current level, we will append to this value
            
            # keep iterating until we have values here, notice the queue will change every time by the loop that's more outer
            for i in range(len(queue)): 
                node = queue.popleft() # pop the oldest value in the queue, so top to bottom, right to left
                levels[level].append(node.val) # append the current value to the level
                # do the same thing with the children (on the next iteration), by simply adding them to the queue
                L, R = node.left, node.right
                if L: queue.append(L)
                if R: queue.append(R)
                    
            level += 1
            
        return levels
  
