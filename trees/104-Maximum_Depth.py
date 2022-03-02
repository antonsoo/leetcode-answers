""" 104 - Maximum Depth of a Binary Tree - Easy - 2022 Q1: LinkedIn>Google>Amzn
- problem: find the depth (deepest/lowest level of a binary tree)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # recursive solution: O(n) time, O(n) space
    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        # base case, if we hit the child of a node with no children. so the end of a branch
        if root is None:
            return 0
        # use DFS
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        # when it hits none, it will equal to zero, so max(0,0) + 1, it will store 1 for that upper/parent node
        # it will keep evaluating the parent nodes and go up, remembering the values so far.
        # eventually this will be run on the root node and return our final answer
        return 1 + max(left, right)
    
    
    # iterative solution, uses a stack: O(n) time, O(n) space (average space is Sigma(log(N)))
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []
        # initialize root if possible:
        if root is not None:
            stack.append((1, root)) 
        
        max_depth = 0
        while stack != []: # while the stack is not empty
            current_depth, root = stack.pop() # assign the two values from the tuple at the top of the stack
            if root is not None: # the root variable is set each time, as you can see in the line above
                max_depth = max(max_depth, current_depth)  # overall max depth to return
                # note, if one of these new root values are None
                #they'll just be skipped by our condition above after popping
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))
        return max_depth
