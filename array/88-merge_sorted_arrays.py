""" 88 - merge sorted arrays - 2022Q1: FB>>>Msft/Amzn>etcetc
- Non-decreasing order means it the next num can either increase or stay the same. 
- **Do not return anything, modify nums1 in-place instead.
- The input is not like I expected. They actually have the array to be modified, nums1,
have extra zeros at the end that equals to the size of the second array. That way you don't have to append to it.
- also the lengths of each array are inputted. (I modified it from the original to make more sense, alphabetically)
n will be len(list1 without the zeros at the end)...and that's the array to modify, m will be the len of list2
"""
class Solution:
    
    # best solution: 3 pointers. Iterate from the end to the start
    # p1 starts at the end (RIGHT BEFORE THE ZEROS), p2 starts at the end of list2, p will be at the end of list1 that we're modifying
    # then choose the biggest value and set it to the value at p
    # O(n + m) time, O(1) space
    def merge(self, nums1: List[int], n: int, nums2: List[int], m: int) -> None:
        # Set p1 and p2 to point to the end of their respective arrays.
        p1 = n - 1
        p2 = m - 1
    
        # And move p backwards through the array, each time writing
        # the smallest value pointed at by p1 or p2.
        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
    
    
    
    # O(n+m) time, O(n) space
    # Make a copy of the original and go through the copy list1 and original list2. Change original list1
    def merge5(self, nums1: List[int], n: int, nums2: List[int], m: int) -> None:
        # Make a copy of the first m elements of nums1.
        nums1_copy = nums1[:n] 
        
        # Read pointers for nums1Copy and nums2 respectively.
        p1 = 0
        p2 = 0
        
        # Compare elements from nums1Copy and nums2 and write the smallest to nums1.
        for p in range(m + n):
            # We also need to ensure that p1 and p2 aren't over the boundaries
            # of their respective arrays. So we do this if we're out of bounds on nums2:
            #Or we do it if the pointer1 is in bounds in nums1 and the val1 is less than val2
            if p2 >= m or (p1 < n and nums1_copy[p1] <= nums2[p2]):
                nums1[p] = nums1_copy[p1] 
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1
    
    
    
    # worst solution: O((n+m)*log(n+m)) time, O(m) space
    def merge2(self, nums1: List[int], n: int, nums2: List[int], m: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Write the elements of num2 into the end of nums1. Those extra places are where the zeros are
        for i in range(m):
            nums1[i + n] = nums2[i]
        
        # Sort nums1 list in-place.
        nums1.sort()
    
    
    
    # my failed attempt:
    # the input is not like what I expceted, also I shouldn't do this from the start to the end, but rather the end to the start
    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2 = 0, 0 # pointers for nums1 and nums2
        limit1, limit2 = len(nums1), len(nums2) # original lengths of the two lists
        
        while True:
            # check bounds, return accordingly
            if p1 >= limit1 and p2 >= limit2 or p2 >= limit2: # both are out of range, or just the nums2 pointer
                return nums1
            elif p1 >= limit1: # only nums1 pointer is out of range of the original list
                nums1 += nums2[p2:] # adds/appends all the elents individually
                return nums1
            
            
            if nums1[p1] == nums2[p2]:
                nums1.insert(p1, nums2[p2])
                p1 += 1 
                p2 += 1
            elif nums1[p1] < nums2[p2]: # insert after p1 because the num at p1 is currently smaller
                p1 += 1
                nums1.insert(p1, nums2[p2])
                p2 += 1
            else: # nums[p1] > nums[p2]: # insert before the current p1 (so at p1 and push others) because the num there is larger
                nums1.insert(p1, nums2[p2])
                p1 += 1
                p2 += 1
                
        return nums1

        
