class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # works for small numbers but exceeds time limit for very large arrays
        # can optimize it further by adding memoization (previously computed products won't be computed again)
        # assume input is >= 2 in len
        ans = [0 for _ in nums]
        for i in range(len(nums)):
            #print(i, math.prod(nums[:i]), math.prod(nums[i+1:]))
            ans[i] = math.prod(nums[:i]) * math.prod(nums[i+1:])
        return ans
