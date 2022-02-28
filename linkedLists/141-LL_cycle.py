""" 141. Linked List Cycle. Easy (Easy+ for the O(1) space sol.).  Msft/Amzn>Visa>etc
- input: head (which contains list of values for all the nodes in the list) and 
the position where the last node (AKA, tail) should be pointing to
- return false if there are 0 or 1 nodes.
- return true if tail 
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # dictionary/hash table approach: O(n) time, O(n) space
    def hasCycle(self, head: ListNode) -> bool:
        dictionary = {} # a dictionary or a set to store *nodes* we already saw (not values of nodes)
        while head: # goes through each node, making it a head
            # check if we already saw this head/node before. 
            if head in dictionary: 
                return True 
            else: # save this head so that we know if we saw it for later
                dictionary[head] = True # the "value" of the node is not important I think, can make it anything. 
            head = head.next # iterate the head to equal the next value in the ListNode obj, which is the head.next
        return False # if none of the nodes was never in the list already/twice, it tells us

    # Two Pointers approach, O(n nodes+ k cycles)->~O(n) time, O(1) time. 
    # Eventually pointer/hare catches up to the same node as slow/turtle node as it goes back to it in the cycle. 
    #Or one of them hits a None node proving there isn't a cycle. 
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next: 
            return False        
        slow, fast = head, head.next
        while slow != fast:
            if not fast or not fast.next: # hits None
                return False
            slow, fast = slow.next, fast.next.next
        return True #if slow==fast so it has a cycle
    
"""
    Two turtles start off at node's 0 and 1, and the rabbit starts off at node 1.
Each turn, the rabbit moves 2 nodes forward and each turtle only moves 1 node forward.
If there is a cycle, eventually the rabbit must land on a turtle because it cannot move more
than 2 spaces at a time, and the two turtles (side by side) cover 2 spaces.
If the rabbit lands on the same node as a turtle, then there is a cycle.
If the rabbit runs out of nodes, then there is no cycle.
"""   
