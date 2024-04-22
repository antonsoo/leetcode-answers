# New solutions (2024, April):
class Solution:
    # Solution 1: An optimized solution
    # Complexity: O(n) time, O(n) space.
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]
        differences_dict = {} # {difference_value i.e. the corresponding_num   :  index_value of that num}
        for ind, num in enumerate(nums):
            diff = target - num
            if diff in differences_dict:
                # so if the difference is already in the dictionary of differences, 
                # then return the index of the indeces of the two nums that add up to the target number
                return [ind, differences_dict[diff]]
            else:
                differences_dict[num] = ind
        return [] # in the case that nothing was found


    # Solution 2: a simple, unoptimized, solution:
    # Complexity: O(n^2) time, O(1) space.
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)):
    #         x = abs(target - nums[i])
    #         for j in range(i + 1, len(nums)):
    #             if x == nums[j]:
    #                 return [i, j]





# Old solutions (2022 and earlier):
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
