""" 98 - Validate a BST - Medium (Easy?) - 2022Q1: Amzn>BloomB>>MSFT>FB>G
- Definition: all of childrens' values on the right must be greater than the parent
and of all the childrens' values on the left must be less than the parent
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # recursive solution: O(n) time, O(n) space
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, low=-math.inf, high=math.inf):
            # an empty tree is valid by default, also hits this when it goes to edge of the Tree (base case)
            if not node:
                return True
            # current node.val must be between low and high
            if node.val <= low or node.val >= high:
                return False
            # check the left and right subtrees of the current node, returns True if condition matches
            # for node.right: low will be node.val. For node.left: high will be node.val
            # so node is the parent/previous node that gets used in the comparison 
            return ( validate(node.right, node.val, high) and 
                    validate(node.left, low, node.val) )
        
        return validate(root)
    
    
    
    # same thing as above, but iterative. O(n) time and space.
    def isValidBST2(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = [(root, -math.inf, math.inf)]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True
                    
    
    
    # recursive in-order traversal. O(n) time and space                
    def isValidBST3(self, root: TreeNode) -> bool:

        def inorder(root):
            if not root:
                return True
            if not inorder(root.left):
                return False
            if root.val <= self.prev:
                return False
            self.prev = root.val
            return inorder(root.right)

        self.prev = -math.inf
        return inorder(root)
    
    
    
    # iterative in-order traversal. O(n) time and space            
    def isValidBST4(self, root: TreeNode) -> bool:
        stack, prev = [], -math.inf

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right

        return True
    
    
    
    
    
    
    # my solution:
    def isValidBST5(self, root: Optional[TreeNode]) -> bool:
        prev = root
        self.validate(root, prev)     
    def validate2(self, root, prev):
        # base case
        if not root: # root is None
            return # None
        prev = root
        if root.left and node:
            left = self.validate(root.left, prev)
            right = self.validate(root.right, prev)
        
        
        
        
        
