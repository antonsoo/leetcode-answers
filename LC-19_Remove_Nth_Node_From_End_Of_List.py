# Date: Sep 29-30, 2025
# LC # 19. "Remove Nth Node From End of List"
# Problem Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Solution Credit: LC user nick-named "Ogabek"
# Solution link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/solutions/4813340/beat-100-00-full-explanation-with-pictures

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        for _ in range(n + 1):
            first = first.next

        while first is not None:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next






#########################################################################################        
######################OLD solutions below
##########################################################################################

""" 19. Remove Nth Node From the end. Medium (Hard if you dont understand LL's). Currently: FB>>MSFT>>Amzn>GOGL 
- remove the n'th node *from the end*. It's counted starting from 1, not 0. so 1 is the tail node pointing to None.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # two pass solution:
    def removeNthFromEnd(self, head, n): 
        # first calculate the length:
        # note: setting currNode to head and modifying currNode will modify head!!!!!!!!!
        currNode = head # set the currNode to point to the first/head node
        length = 0
        while currNode:
            currNode = currNode.next # reset the currNode to now point to the next node
            length += 1 
            
        currNode = head # reset the currNode to point to the first/head node
        
        # in case the first/head node is to be deleted, just return the value right after it
        if n == length: 
            return head.next
        
        # now calculate where to remove the node
        remove_ind = length - n # calculate the index from left to right
        curr_ind = 1 # this has to start from 1 because we increase the currNode one more time 
        #we don't want to run over!!! 
        # exit out of the loop as soon as we find the node index we need to remove
        while curr_ind < remove_ind:
                curr_ind += 1
                currNode = currNode.next
                
        # when we exit out of the loop above, we can actually remove the one node needing removing
        currNode.next = currNode.next.next  
        #currNode.next.val = currNode.next.next.val
        return head # head
    
    
    
    
    # another way to write the solution:
    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        fast = head
        slow = head
        # advance fast to nth position
        for i in range(n):
            fast = fast.next
            
        if not fast:
            return head.next
        # then advance both fast and slow now they are nth postions apart
        # when fast gets to None, slow will be just before the item to be deleted
        while fast.next:
            slow = slow.next
            fast = fast.next
        # delete the node
        slow.next = slow.next.next
        return head
    
    
    
    
    def removeNthFromEnd3(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        # find len of LList:
        currNode = head
        while currNode:
            currNode = currNode.next
            length += 1  

        if length <= 1: # head = tail or an empty LL;; we probably dont need to do this since we will automatically do it later
            return ListNode([None]) # an empty LL
        
        curr_node = 0
        remove_ind = length - n # converting to a CS-readable index
        
        #if remove_ind == len(head): # this is the tail (last node) 
        #    node.va
        
        prevNode = head 
        ind = 0
        while head: # is not None
            if remove_ind == n: 
                prevNode.next = None
                prevNode.next.val = None
                break
            
            elif ind == remove_ind: # matching index of the node to remove
                # rewrite
                node.val = node.next.val
                node.next = node.next.next 
                break
        return head
