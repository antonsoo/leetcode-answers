"""234 - Palindrome LL - Easy (O(1) space is Med+) - Facebook>>Amzn>MSFT>etc 
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # easy iterative solution: O(n) time, O(n) space. 
    # Can easily optimize it further to O(n/2) space by only iterating up to the half of the list 
    def isPalindrome2(self, head: ListNode) -> bool:
        currentNode = head # set it to point to head so we don't modify head
        L = [] # a list to store the LL 
        while currentNode: # while not None
            L.append(currentNode.val) # append the value
            currentNode = currentNode.next # go forward in the iteration
        return L == L[::-1]
    
      
    
    
    # reverse in place: O(n) time, O(1) space
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        # Find the end of first half and reverse second half.
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # Check whether or not there's a palindrome.
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # Restore the list and return the result.
        first_half_end.next = self.reverse_list(second_half_start)
        return result    

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous
