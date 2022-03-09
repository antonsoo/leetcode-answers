""" 108 - Convert Sorted Array to BST - 2022Q1: FB>Msft>Ora
input: **sorted** array
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # complexity: O(N) time, O(logN) space because it's balanced... technically it's O(N) space to store the output but we won't count it
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if left > right: # we passed right so time to return
                return None
            
            p = (left + right) // 2 # this will choose the left middle node as a root, changes at each call
            # if (left + right) % 2: p+= 1 # this will choose the right middle node as root, can also do: p += randint(0, 1)
            
            
            # preorder traversal: node -> left
            root = TreeNode(nums[p]) # initialize the tree with the middle node, note this changes each time (local root)
            root.left = helper(left, p - 1) # the left variable doesn't change at first, 0, same as the original input
            root.right = helper(p + 1, right) # the right variable doesn't change first, same as input (the last pointer in the array)
            return root
        
        return helper(0, len(nums) - 1)
    
    
    # same thing thing as above, but without a helper function
    def sortedArrayToBST2(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        i = len(nums) // 2
        root = TreeNode(nums[i])
        root.left = self.sortedArrayToBST(nums[:i])
        root.right = self.sortedArrayToBST(nums[i+1:])
        return root
    
    
    
    # my attempt, incomplete
    def sortedArrayToBST3(self, nums: List[int]) -> Optional[TreeNode]:
        # edge case, empty input
        if len(nums) == 0: 
            return None
        
        # initialize our output object, nums[0] will be the root
        tree = TreeNode(nums[0])
        
        for num in nums[1:]: # iterate after the nums[0] since we already use it above
            tree.left = nums
        
