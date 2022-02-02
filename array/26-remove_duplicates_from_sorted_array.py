"""
- Problem: Remove all duplicates (in place) from a SORTED array and return the number of unique integers there
- Solution: Use two pointers, one pointer keep increasing until the number changes, then the second pointer will increase and 
put the duplicate to one index over (to the second duplicate's place), and it will continue on from that first pointer.
- Complexity: O(N) time, O(1) space
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 0: # edge case
            return 0
        j = 0
        for i in range(len(nums)): # i and j start the same
            # if this conditions is not satisfied, so if they equal, then i will just keep increasing
            if nums[i] != nums[j]:
                j += 1 # if the condition is met, j increases
                nums[j] = nums[i] # the number at index j will be replaced with the number at index i
        return j + 1
    
# Ex: 
#[0, 0, 0, 1, 1] -> it keep increasing the i pointer until index 4, then it puts the value 1 into index 2, and moves on with the algo.
