"""
Use collections.Counter .
Use the fact that dict1.keys() & dict2.keys() returns the keys common to dict1 and dict2
Use the fact that [x] * n gives an array [x, x, ..., x] of length n
Use the extend method of lists

O(n + m) time, O(min(n, m)) space
"""
    
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


