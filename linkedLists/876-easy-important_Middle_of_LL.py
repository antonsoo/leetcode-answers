# 876. Middle of the Linked List - Easy - Amzn/Apple/Adobe


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.dict = {}

    # Two pointers solution: O(N) time, O(1) space.
    # advance two pointers. The fast pointer will advance twice as fast
    # by the time the fast pointer finishes, the slow pointer will be in the middle.
    def middleNode(self, head): 
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow   
        
        
        
        
    # Output to array solution: O(N) time and space.
    def middleNode2(self, head: ListNode) -> ListNode:
        arr = [head]
        while arr[-1].next:
            arr.append(arr[-1].next)
        return arr[len(arr) // 2]    
        
        
        
        
    #helper function for measuring number of elements in the linked list
    #I should store the counts in a dict to reuse them later (DP), and just return it later
    def getCount(self, head: ListNode) -> int:
        count = 0
        temp = head
        while temp:
            self.dict[count] = temp
            count += 1
            temp = temp.next
        return count
    
    def middleNode3(self, head: ListNode) -> ListNode:
        #half index is either the exact middle for an odd-num'd array or for even it's +1 val
        half_ind = self.getCount(head) // 2  
        return self.dict[half_ind] #fetch the head we stored for that halfind

    ''' same thing as above but in one function
      def middleNode(self, head: ListNode) -> ListNode:
        count = 0
        temp = head
        while temp:
            self.dict[count] = temp
            count += 1
            temp = temp.next
        #half index is either the exact middle for an odd-num'd array or for even it's +1 val
        half_ind = count // 2 #Solution.getCount(self.head) // 2  
        return self.dict[half_ind] #fetch the head we stored for that halfind 
    '''
