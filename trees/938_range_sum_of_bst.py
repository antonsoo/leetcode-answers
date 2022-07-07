# 938. Range Sum of BST - "Easy" - 2022Q2Facebook

# Assuming low!=high ??

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # iterative solution (DFS), so we must use a stack
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0 
        stack = [root] # initialize the stack at the root of the tree
        while stack: # while it's not empty, keep running/popping
            node =  stack.pop() # pop a node from the top, then start to checks
            if not node: # skip the empty node, can also put this as an outer condition
                continue
            if low <= node.val <=  high: # if the value falls between the bounds, add it
                ans += node.val
            if low < node.val: # as long as it doesn't go out of bounds on the low side
                stack.append(node.left)
            if high > node.val:
                stack.append(node.right) # as long as it doesn't go out of bounds on the high
        return ans
    
    # recursive solution (DFS)
    def rangeSumBST2(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # need for all statements to be if, not elif since we might do them again 
        def helper(root): # the passed "root" parameter changes
            nonlocal ans
            if not root: # if it's empty
                return
            if low <= root.val <= high:
                ans += root.val
            if root.val > low: # only go to the left if it's doesn't go over our bound
                helper(root.left)
            if root.val < high: # only go to the right if it's smaller than the high bound 
                helper(root.right)
        ans = 0
        helper(root)
        return ans
        
    
    # my broken solution
    def rangeSumBST3(self, root: Optional[TreeNode], low: int, high: int) -> int:
        range_array = [] # keep track of values we should sum over to get the result
        # traverse the tree iteratively:
        # initialize the base cases
        currval = root.val
        nextval = root.val  
        # loop
        #...
        if currval <= low:
            range_array.append(currval)
            nextval  = root.left
        #else: 
        #    if
            
        
