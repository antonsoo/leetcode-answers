class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # O(nlogn) time, O(n) space technically for sorting, but others might call it O(1) since we modify the original array
        if len(nums) < 4:
            return 0
        nums.sort() # sort in place if allowed, to save memory
        print(nums)
        return min(nums[-4] - nums[0], nums[-3] - nums[1], nums[-2] - nums[2], nums[-1] - nums[3])
