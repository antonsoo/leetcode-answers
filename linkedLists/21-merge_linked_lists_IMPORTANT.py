""" 21 - Merge Two Sorted (Linked) Lists. Easy. Amzn>>Msft/FB>Adobe>Gogl
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # recursive solution: O(n + m) time, O(n + m) space
    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        # I believe we're modifying the two lists here to try to merge both of them 
        if l1 is None:
            return l2 
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            #print("l1", l1) #looks backwards because a stock pops t he last thing  first
            return l1
        else: # l1.val >= l2.val
            l2.next = self.mergeTwoLists(l2.next, l1)
            #print("l2", l2)
            return l2

     
    # iterative: O(n + m) time, O(1) space (if we dont count the output array) 
    def mergeTwoLists(self, l1, l2):
        # maintain an unchanging reference to node ahead of the return node.
        # this is the LL where we will store our answer
        prehead = ListNode(-1) 

        prev = prehead # actual 
        
        while l1 and l2:  # while they're not None
            # compare the two values, 
            # set the next value in the output array to be the head of the current
            # then iterate the head forward
            if l1.val <= l2.val: # compare
                prev.next = l1 # set the next value in the output list
                l1 = l1.next # continue the iteration
            else:
                prev.next = l2
                l2 = l2.next  # continue the iteration
            prev = prev.next

        # At least one of l1 and l2 can still have nodes at this point, so connect
        # the non-null list to the end of the merged list.
        # so here we're iterating through the leftover l1 or l2
        prev.next = l1 if l1 is not None else l2

        return prehead.next # return the head (after the dummy -1 node we made at first)
