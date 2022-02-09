# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# worst: O(n) time, O(n) space where n is height of the tree
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is not None:
            # invert child nodes
            self.invertTree(root.left)
            self.invertTree(root.right)
            # swap children. if there is no right child, it will just swap None and node or None and None
            # but as soon as it hits the None node, it will also start going up to the child nodes and then it can finally swap the child nodes.
            temp = root.right
            root.right = root.left
            root.left = temp
        return root # base case itself is to return the root node, at first it will find the first None node and return that, and it will continue so, then it will return the first furthest child node it finds, and so on. this is BFS. 
    
    
    def invertTree2(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        tmp = self.invertTree(root.right)
        tmp2 = self.invertTree(root.left)
        root.left = tmp
        root.right = tmp2
        return root
    
    def invertTree3(self, root: TreeNode) -> TreeNode
        if not root: 
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
        
