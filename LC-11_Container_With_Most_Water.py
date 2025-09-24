# Date: Sep 23, 2025
# LC # 11. "Container With Most Water"
# Solution Credit: LC user nick-named "niits"
# Solution link: https://leetcode.com/problems/container-with-most-water/solutions/5139915/video-simple-two-pointer-solution
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area



################################################
################################################
################################################
# old solution
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # O(n) time, O(1) space
        maxArea = 0
        left = 0
        right = len(height) - 1
        while left < right:
            maxArea = max(maxArea, min(height[left], height[right]) * (right - left))
            # move the pointer of the smaller height forward/backward
            # so basically you're just finding the biggest height since it will give you the biggest area potentially (distance is also important, that's why you start as far as away as possible and try everything)
            if height[left] < height[right]: 
                left += 1
            else:
                right -= 1 
        return maxArea
