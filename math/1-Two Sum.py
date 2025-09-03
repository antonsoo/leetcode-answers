# New solutions (Sept 2025):
from typing import List # technically, this is unnecessary but this may be already imported automatically. So below we're using what's called "type hinting." "This import allows you to specify that a variable or function argument is a List containing elements of a specific type."" 

class Solution:
    # ChatGPT-5-Pro's suggested implementation #1 (Chat can be accessed thru: https://chatgpt.com/share/68b893bb-6a18-8003-a800-59323dc9c269)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need = {}  # number we need -> index of its partner so far
        for i, x in enumerate(nums):
            if x in need:               # <-- check current number, not its diff
                return [need[x], i]
            need[target - x] = i
        raise ValueError("No solution") # technically, not needed as there is always a solution for this problem... an assumption for this problem in LeetCode
    
    # ChatGPT-5-Pro's suggested implementation #2 (Conventional “seen-map” variant (equally good; keys are values already seen))
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: dict[int, int] = {}    # value -> index
        for i, x in enumerate(nums):
            comp = target - x
            j = seen.get(comp)
            if j is not None:
                return [j, i]
            seen[x] = i
        # Can add a ValueError here if really necessary

    # my own implementation
    def my_twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {} # difference or num to index pairs (difference is the key, index is the value)
        for ind, num in enumerate(nums):
            diff = target - num
            if len(mydict) > 0:
                if num in mydict:
                    return [mydict[num], ind] # [old_ind, curr_ind]
                else:
                    mydict[diff] = ind
            else:
                mydict[diff] = ind

    # my own implementation tightened up by ChatGPT-5-Pro (need-map, one lookup, no extra branch)
    def my_twoSum_tightened_up(self, nums: List[int], target: int) -> List[int]:
        need: dict[int, int] = {}  # value we need -> index of partner
        for i, x in enumerate(nums):
            j = need.get(x)          # one lookup; may be 0, so check None explicitly
            if j is not None:
                return [j, i]
            need[target - x] = i
        # On LeetCode this path is unreachable because a solution is guaranteed.

                






###################################
###################################
###################################
###################################
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





###################################
###################################
###################################
###################################


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
