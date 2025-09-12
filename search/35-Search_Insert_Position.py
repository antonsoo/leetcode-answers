# Credit: https://leetcode.com/problems/search-insert-position/solutions/5361984/video-return-middle-or-left-pointer
class Solution:
    # Regular solution
    # A classic binary search problem: 
    # Time complexity: O(log(n)). Space complexity: O(1).
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1
        i = 0

        while left <= right:
            i += 1
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else: 
                left = mid + 1
        return left





    # Printed solution (lets you visualize how the algorithms is actually working):
    # A classic binary search problem: 
    # Time complexity: O(log(n)). Space complexity: O(1).
    def printed_searchInsert(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1
        i = 0

        while left <= right:
            print("iteration number:", i)
            i += 1
            mid = (left + right) // 2
            print("mid calculated to be: ", mid)
            if nums[mid] == target:
                print("mid (returning): ", mid)
                return mid
            elif nums[mid] > target:
                right = mid - 1
                print("left (NO condition hit", left)
                print("right (condition hit): ", right)
            else: 
                left = mid + 1
                print("left (condition hit): ", left)
                print("right (NO condition hit)", right)
        print("final left: ", left)
        return left
