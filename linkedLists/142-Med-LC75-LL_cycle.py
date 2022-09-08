# 142. Linked List Cycle II - Medium - LC75 - 2022Q3: Amzn
# Questions: Are the nodes' values all unique?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
     # O(N) time, O(1) space
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        if head is None: # fail case
            return None
        
        intersection = None
        # find the intersection
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                intersection = slow
                break
        
        if intersection is None:
            return None
        
        # find the entrance to the cycle
        p1 = head
        p2 = intersection
        while p1 != p2: 
            p1 = p1.next 
            p2 = p2.next
        return p1
        
        
        # second way:
    def detectCycle2(self, head):
        visited = set()

        node = head
        while node is not None:
            if node in visited:
                return node
            else:
                visited.add(node)
                node = node.next

        return None
    
    
