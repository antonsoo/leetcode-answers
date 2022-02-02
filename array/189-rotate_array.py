""" Medium problem
- Input: Array of ints above it's always about 1 in len
- Problem: rotate an array by k steps (rightwards and wrap). Ideally try to do it in O(1) space.
- Solution: The easiest way to do it is just to use a different array and append to starting from that value.
Use a modulus operator to know when you should wrap.
A better way is to just use two pointers, and swap numbers.
- Complexity: 
"""
class Solution:
    # swaps two numbers in an array given indices i and j
    def swap(self, nums: List[int], i: int, j: int) -> None:
        nums[i], nums[j] = nums[j], nums[i]
      
    
    # O(n) time, O(1) space. cyclic replacement. Ex: k=2: 1->3->5, 5->1)) 2->4->6, 6->2 ))
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        start = count = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1  
                if start == current:
                    break
            start += 1
    
    
    # O(n) time, O(1) space
    """
    rotate 1 steps to the right: [7,1,2,3,4,5,6]
    rotate 2 steps to the right: [6,7,1,2,3,4,5]
    rotate 3 steps to the right: [5,6,7,1,2,3,4]
    """
    def reverse(self, nums: list, start: int, end: int) -> None:
        while start < end:
            self.swap(nums, start, end)
            start, end = start + 1, end - 1           
    def rotate2(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
    
    
    
    # O(n) time I believe. O(n) space?
    def rotate3(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        nums[k:], nums[:k] = nums[:-k], nums[-k:]
    
    
    
    # O(n*k) time (too long for LC), O(1) space
    def rotate4(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  # cut down the k to speed up this algo.
        last = -1 # the last element in the array nums
        # k rotations
        for idx in range(k):
            # keeps swapping the current num (from 0 to last index) with the num at the last index
            # so this is actually 1 rotation. It puts the last number at the start, and shifts everything.
            for j in range(n):
                self.swap(nums, j, last)
    
    
    # my failed attempt.
    def rotate5(self, nums: List[int], k: int) -> None:
        n = len(nums)
        for idx in range(n - k - 1):
            newIdx = (idx + k) #% n 
            self.swap(nums, idx, newIdx)
            print(nums)
        
