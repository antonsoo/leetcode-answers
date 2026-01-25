# 162. Find Peak Element
# https://leetcode.com/problems/find-peak-element/solutions/6743944/video-binary-search-solution-by-niits-shu7/

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left
