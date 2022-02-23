""" 237 - Delete Node in a LL . Easy  . Currently: Microsoft>Apple. Past: Adobe>Google etc
- Not a good question. This is just to test if you know what deleting in a LL does, without doing much else.
-These are the assumptions:
  The number of the nodes in the given list is in the range [2, 1000].
  -1000 <= Node.val <= 1000
  The value of each node in the list is unique.
  The node to be deleted is in the list and is not a tail node
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
