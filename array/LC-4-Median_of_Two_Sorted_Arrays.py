# Sep 15, 2025
# LC Problem Number 4: "Median of Two Sorted Arrays"
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # two pointer solution?
        n = len(nums1)
        m = len(nums2)

        # easiest solution:
        nums3 = nums1 + nums2
        nums3.sort()
        l = len(nums3)
        halfcutoff = l // 2
        if l % 2 == 0:
            return (nums3[halfcutoff - 1] + nums3[halfcutoff])/2
        else:
            return (nums3[halfcutoff])
