""" 206 - Reverse a LL.   Easy.   Currently: Bloomberg>MSFT>APPL>AMZN>FB
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

    
"""
- Basically the arrow is the .next.  You're starting at: 1 -> 2 -> 3 -> None   (head is 1, that's the node/value that points/holds all the other nodes in the memory).   
- You make a new None (call it prevNode) and then reverse the arrow (currentNode.next to point to the None) like this:  None <- 1  . Then you move those two pointers (prevNode and currNode, each by 1. Since it's a LL, you can't just use an index, you have assign them using .next or other values). So then it does None <- 1 <- 2
Then finally None <- 1 <- 2 <- 3    (it stops at the None after 3, so the last iteration was at 3)
"""  
#same thing as above but easier to understand
class Solution:    
    def reverseList(self, head): #iterative: O(n) time,  O(1) space
        # first start with the previous node being the None node since we need the tail to point to None.
        #So the first next node will be head (now the new tail). It will run up until the node 5, 
        #and never get to the None node since we dont want the new head to have None.
        #1. Reverse  (curr.next = prev)
        #2. Update Current and Update previous (in any order)
        prevNode = None
        currNode = head
        while currNode: # while currNode != None
            currNode.next, currNode, prevNode = prevNode, currNode.next, currNode
            #currNode.next, prevNode, currNode = prevNode, currNode, currNode.next # order matters!!
        return prevNode # return this since that's what we're modifying
    
    
    def reverseList3(self, head: ListNode) -> ListNode:  #recursive: O(n) time, O(n) space
        first = head
        if (not first) or (not first.next): 
            return first

        first.next, curr, prev = None, first.next, first
        
        # first start with the previous node being the None node since we need the tail to point to None.
        #So the first next node will be head (now the new tail). It will run up until the node 5, 
        #and never get to the None node since we dont want the new head to have None.
        #1. Reverse  (curr.next = prev)
        #2. Update Current and Update previous (in any order)
        
        while curr.next:
            curr.next, curr, prev = prev, curr.next, curr

        curr.next = prev
        return curr
    
    
    # stack solution
    # put everything onto the stack, make a new LL and append to it from the stack
    def reverseList2(self, head: ListNode) -> ListNode:
        stack = []
        while (head != None):
            stack.append(head)
            head = head.next
        reversedLL = ListNode()
        prevhead = 0
        while (len(stack) != 0):     
            currhead = stack.pop()
            reversedLL.head.next = currhead
            prevhead=currhead
        return reversedLL
