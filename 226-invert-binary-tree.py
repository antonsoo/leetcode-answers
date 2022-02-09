# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree2(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        tmp = self.invertTree(root.right)
        tmp2 = self.invertTree(root.left)
        root.left = tmp
        root.right = tmp2
        return root
    
    def invertTree(self, root: TreeNode) -> TreeNode:
        # worst: O(n) time, O(n) space because of the recursive calls using space
        if not root: 
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
        
