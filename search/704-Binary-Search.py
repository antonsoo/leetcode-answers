class Solution:
    #binary search: O(log n) time. O(1) space. Requires sorted list.
    def search(self, nums: List[int], target: int) -> int:
        leftp, rightp = 0, len(nums) - 1
        while leftp <= rightp:
            pivot = leftp + (rightp - leftp) // 2 # more robust than ..
            if nums[pivot] == target:
                return pivot
            elif target < nums[pivot]: # move the bounds of the window
                rightp = pivot - 1
            else:
                leftp = pivot + 1         
        return -1 # fail case
    
#     def find_mp(self, l): #finds midpoint
#         n = len(l)
#         return [n//2, l[n//2]] # [index, val]
    
#     def search(self, nums: List[int], target: int) -> int:
#         ind, mp = self.find_mp(nums) # midpoint
#         if mp == target:
#             return index
#         elif mp <= target: # in right half
#             index -= ind
#             nums = nums[0:mp]
#             search(nums)
#         elif mp >= target: # in the left half:
#             index += ind
#             nums = nums[mp:]
#             search(nums)
#         else: #doesn't exist
#             return -1


        
        
