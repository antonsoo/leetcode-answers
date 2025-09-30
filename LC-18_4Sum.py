# Date: Sep 29-30, 2025
# LC # 18. "4Sum"
# Problem Link: https://leetcode.com/problems/4sum/
# Solution Credit: LC user nick-named "Mai Thanh Hiep"
# Solution link: https://leetcode.com/problems/4sum/solutions/1341213/c-python-2-solutions-clean-concise-follow-up-k-sum
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        i = 0
        while i < n:
            j = i + 1
            while j < n:
                l, r = j + 1, n - 1
                goal = target - nums[i] - nums[j]
                while l < r:
                    if nums[l] + nums[r] == goal:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        while l+1 < n and nums[l+1] == nums[l]: l += 1 # Skip duplicate nums[l]
                        l += 1
                        r -= 1
                    elif nums[l] + nums[r] > goal:
                        r -= 1
                    else:
                        l += 1
                
                while j+1 < n and nums[j+1] == nums[j]: j += 1 # Skip duplicate nums[j]
                j += 1
                        
            while i+1 < n and nums[i+1] == nums[i]: i += 1 # Skip duplicate nums[i]
            i += 1
        return ans
