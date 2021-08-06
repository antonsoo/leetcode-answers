class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) < 2: # let n=len(nums): given 1 <= n <= 5000
            return nums[0]
        left = 0 
        right = len(nums) - 1
        if nums[left] <= nums[right]: # no rotation, or equal numbers
            return nums[left] # so return the already min num 
        while left < right:
            middle = left + (right - left) // 2 # (left + right) // 2
            if middle > 0 and nums[middle - 1] > nums[middle]: # found it, sorting order
                return nums[middle]
            elif nums[left] <= nums[middle] and nums[right] < nums[middle]: # left side is sorted correctly, but right is not
                left = middle + 1 # go right, so move the left pointer
            else: # right side is sorted correctly, but left side is not
                right = middle - 1 # go left, so move the right pointer
        return nums[left] # return min found
