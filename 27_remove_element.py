class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Pointer for the next valid position
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Overwrite value at k with non-val element
                k += 1  # Move k forward
        return k  # k is the count of valid elements
