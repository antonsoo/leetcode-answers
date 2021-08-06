class Solution:
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        # works for small numbers but exceeds time limit for very large arrays
        # can optimize it further by adding memoization (previously computed products won't be computed again)
        # assume input is >= 2 in len
        ans = [0 for _ in nums]
        for i in range(len(nums)):
            #print(i, math.prod(nums[:i]), math.prod(nums[i+1:]))
            ans[i] = math.prod(nums[:i]) * math.prod(nums[i+1:])
        return ans
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) time, O(1) space
        # construct an array which stores the products to the left of each num
        # then multiple those products backwards with products to the right
        answer = [0 for _ in nums]
        # both left and right multiples are 1 because there is nothing to the left of the first, and nothing to the right of the last
        answer[0] = 1
        R = 1
        for i in range(1, len(nums)):
            answer[i] = nums[i-1] * answer[i-1] # previous i'th product * previous num #left
        for i in reversed(range(len(nums))): # calculate the right answer at the same time as multiplying it to the previous answer
            answer[i] = answer[i] * R
            R = R * nums[i]
        return answer
