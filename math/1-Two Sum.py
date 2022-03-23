class Solution:
    # assuming it exists
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(N) time and space
        dicti = {}
        for ind, num in enumerate(nums):
            diff = target - num # the diff is the actual number we're looking for
            if diff in dicti: 
                # and we're returning the val of the dicti[diff] which is the index of it
                return [dicti[diff], ind]
            else: 
                dicti[num] = ind
