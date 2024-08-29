#Old:
"""
- problem: find the only number that isn't repeated in the array. Every other element is repeated *exactly twice.*
- solution: hash map, sorting, brute force, math. Best: bit manipulation: a xor 0 = a. a xor a = 0. a xor b xor a = b
- complexity: O(N) time, O(1) space
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a

###############################

# New: 2024-Aug-29:
class Solution:
    # def singleNumber(self, nums: List[int]) -> int:
    #     nums_dict = {}
    #     for num in nums:
    #         if num not in nums_dict:
    #             nums_dict[num] = 1
    #         else: 
    #             nums_dict[num] = 2 
        
    #     for key, val in nums_dict.items():
    #         if val == 1:
    #             return key

    ## genius solution from sunakshi132: 
    # def singleNumber(self, nums: List[int]) -> int:
    #   return 2 * sum(set(nums)) - sum(nums))

    ## genius solution 3 from satyamsinha93 and explained by umetaloper: 
    ## 1 xor 2 xor 3 xor 1 xor 2 xor 3 xor 4 = (1 xor 1) xor (2 xor 2) xor (3 xor 3) xor 4 (commutative & associative) = 0 xor 0 xor 0 xor 4 = 4
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor
