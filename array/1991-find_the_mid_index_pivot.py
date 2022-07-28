# 1991. Find the Middle Index in Array # same as 724. Find Pivot Index
# Easy/med: 2022Q2: FB  (etc)
class Solution:
    # O(N) time, O(1) space
    def findMiddleIndex(self, nums: List[int]) -> int:
        totSum = sum(nums)
        leftSum = 0
        for i, num in enumerate(nums):
            rightsum = totSum - leftSum - num # totalSum - leftSum - num (possible pivot)
            if leftSum == rightsum:
                return i # that's the index of our current num (the pivot)
            leftSum += num
        return -1 # no pivot was found        
