class Solution:
    # inspired by this video: https://www.youtube.com/watch?v=IzHR_U8Ly6c
    def findMin(self, nums: List[int]) -> int:
        # O(log(n)) time, O(1) space
        if len(nums) < 2: # let n=len(nums): given 1 <= n <= 5000
            return nums[0]
        left = 0 
        right = len(nums) - 1
        
        # optional
        if nums[left] <= nums[right]: # no rotation, or equal numbers
            return nums[left] # so return the already min num 
        
        while left < right:
            middle = left + (right - left) // 2 # better than: (left + right) // 2 because it prevents int overflow (or something)
            if middle > 0 and nums[middle - 1] > nums[middle]: # found it, prev number is larger meaning we found where the list starts to increase again (because it's split there!)
                return nums[middle]
            elif nums[left] <= nums[middle] and nums[right] < nums[middle]: # left side is sorted correctly, but right is not, and right is smaller! so to find min, go there
                left = middle + 1 # go right, so move the left pointer
            else: # right side is sorted correctly, but left side is not, and left is smaller
                right = middle - 1 # go left, so move the right pointer
        return nums[left] # return min found, which is at the left/min pointer
