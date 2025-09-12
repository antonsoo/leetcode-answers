# 2025 Solution: credit: https://leetcode.com/problems/binary-tree-inorder-traversal/solutions/3169549/solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st = []
        res = []

        while root or st:
            while root:
                st.append(root)
                root = root.left
            
            root = st.pop()
            res.append(root.val)

            root = root.right
        
        return res 






''' 94. Binary Tree Inorder Traversal - Amzn>Msft>Appl
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # traverses top to bottom, and left to right, horizontal layer-wise
    # get all the values of the nodes in the list and store/return them to output
    def bfsTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: # very first initial check
            return []
        # have to initialize a set or list inside a deque like this: de([()])
        queue = collections.deque([(root, root.val)])
        output = [] # values of the nodes
        
        while queue: # while it's not empty
            currnode, currval = queue.popleft()
            if currnode: # if it's not None
                #currnode, currval = queue.popleft()
                output.append(currval)
                if currnode.left:
                    queue.append((currnode.left, currnode.left.val))
                if currnode.right:
                    queue.append((currnode.right, currnode.right.val))
        return output

    # starts from the very bottom, left, goes up to the immediate parent node,
# then goes to the right node of the parent. Does that until it does all of
# the left nodes then does the root node, and then the same thing for the right nodes.
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        def traverse(root):
            if not root:
                return
            traverse(root.left)
            output.append(root.val)
            traverse(root.right)  
        traverse(root)
        return output
    
    
    
    
    # someone's code:
    def inorderTraversal3(self, root):
        stack, result = [(False, root),], []
        while stack:
            read, node = stack.pop()
            if node:
                if not read:
                    stack.append((False, node.right))
                    stack.append((True, node))
                    stack.append((False, node.left))
                else:
                    result.append(node.val)
        return result
