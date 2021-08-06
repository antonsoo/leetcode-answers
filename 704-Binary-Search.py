class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # iterative implementation, O(log(n)) time, O(1) space
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else: # nums[middle] < target:
                left = middle + 1
        return -1
