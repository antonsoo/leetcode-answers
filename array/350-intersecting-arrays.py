"""
Use collections.Counter .
Use the fact that dict1.keys() & dict2.keys() returns the keys common to dict1 and dict2
Use the fact that [x] * n gives an array [x, x, ..., x] of length n
Use the extend method of lists

O(n + m) time, O(min(n, m)) space
"""
# 1) Count up the number of items in array1 and then array2, using counter (dictionaries) like arr1 = {'a': 2, ...}, arr2 = {'a': 3, ...}
# 2) Go through their intersect of keys, using &
# 3) Add the intersect to the output array by only taking the smallest/min number (value) between the two counters.

import collections
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:           
        collection1 = collections.Counter(nums1)
        collection2 = collections.Counter(nums2)
        output = []
        for key in collection1.keys() & collection2.keys():
            output.extend([key]*min(collection1[key], collection2[key]))
        return output
 
# one liner : return list((Counter(nums1)&Counter(nums2)).elements())   
    
# second way is to use two pointers


