from typing import List # technically, this is unnecessary but this may be already imported automatically. So below we're using what's called "type hinting." "This import allows you to specify that a variable or function argument is a List containing elements of a specific type."" 

class Solution:
    # Aug 22, 2026 (own solution) # https://neetcode.io/problems/two-integer-sum/history?list=neetcode150&submissionIndex=1   # O(n) worst time & space (O(n) is possible in a very rare hash collision case) 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = {}
        for i, v in enumerate(nums):
            if v in diff_dict:
                return [diff_dict[v], i]
            else:
                diff_dict[target - v] = i


    # my solution from Aug 1 (mirroring the solution from ChatGPT)
    def twoSum222(self, nums: List[int], target: int) -> List[int]:
        need = {}
        for i, x in enumerate (nums):
            if x in need:
                return [need[x], i]
            need[target - x] = i


    # ChatGPT-5-Pro's suggested implementation #1 (Chat can be accessed thru: https://chatgpt.com/share/68b893bb-6a18-8003-a800-59323dc9c269)
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        need = {}  # number we need -> index of its partner so far
        for i, x in enumerate(nums):
            if x in need:               # <-- check current number, not its diff
                return [need[x], i]
            need[target - x] = i
        raise ValueError("No solution") # technically, not needed as there is always a solution for this problem... an assumption for this problem in LeetCode
    
    # ChatGPT-5-Pro's suggested implementation #2 (Conventional “seen-map” variant (equally good; keys are values already seen))
    def twoSum_2(self, nums: List[int], target: int) -> List[int]:
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

                
