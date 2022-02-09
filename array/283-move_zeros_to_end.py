""" difficulty: easy
- other possible solutions?: 1) have two pointers. 2) append to a list every time it's not a zero, and count all 
zeros, lalter add all the zeros like this: arr += [0] * numZeros
- this solution: keep track of the non-zero number's position, every time you see a zero number then switch it 
with the last encountered non-zero number.
"""

#  Do not return anything, modify nums in-place instead.
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pos = 0 # keep track of the last non-zero number's position 
        for i, num in enumerate(nums):
            if num != 0: # if non-zero
                if i != pos:  #and not in the same position then switch the two numbers
                    nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1 # always update the pos value to keep track of the last non-zero number's position
