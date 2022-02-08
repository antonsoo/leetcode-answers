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
