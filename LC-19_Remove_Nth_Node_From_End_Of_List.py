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
