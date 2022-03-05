""" 101 - symmetric tree - 2022Q1: FB>Amzn>Bloom/Msft
- solution: 
 go through each node on both sides
 define the base cases in which either both nodes (on each side) are None or both
 then compare their values and rerun the function on their children, first left and right
(in a mirror fashion), then right and left (in a mirror), so left of one parent, right of another parent
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # recursive solution: O(N) time and space. I believe it's DFS
    def isSymmetric2(self, root: Optional[TreeNode]) -> bool:
        
        # validate if the nodes A and B are symmetrical/mirrors on each other's side
        def validate(A, B): # Left and Right of the current node, or Right and Left depending on how it's set
            if not A and not B: # both are None, so return True. Empty tree returns True since they match
                return True
            
            elif not A or not B: # just one of them is None so not matching
                return False
            
            # note the order of the parameters you pass to this function doesn't remember
            return A.val == B.val and validate(A.left, B.right) and validate(A.right, B.left)  # elif and else

        return validate(root, root)
    
    
    
    # iterative solution: O(N) time and space
    def isSymmetric(self, root):
        if not root:
            return True
        stack = [(root.left, root.right)]
        while stack:
            l, r = stack.pop()
            if not l and not r:
                continue
            if not l or not r or (l.val != r.val):
                return False
            stack.append((l.left, r.right))
            stack.append((l.right, r.left))
        return True
