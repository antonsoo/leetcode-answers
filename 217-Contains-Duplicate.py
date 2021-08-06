class Solution: 
    def containsDuplicate(self, nums: List[int]) -> bool:
    # O(n) time, O(n) space
        if len(set(nums)) != len(nums):
            return True
        return False
