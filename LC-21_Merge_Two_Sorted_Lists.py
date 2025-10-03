# Date: Oct 2-3, 2025
# LC # 21. "Merge Two Sorted Lists"
# Problem Link: https://leetcode.com/problems/merge-two-sorted-lists/
# Solution Credit: LC user nick-named "dp228"
# Solution link: https://leetcode.com/problems/merge-two-sorted-lists/solutions/1826693/python3-merging-explained

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next
