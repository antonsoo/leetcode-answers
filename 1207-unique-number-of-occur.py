# objective: make sure the counts(number of occurences) of each digit is unique
# complexity: O(N) time to through the array once, 
#O(N) space in the worst case have to store the entire original array
from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # collect all the counts automatically into a dictionary
        counts = collections.Counter(arr)
        # initialize an list/array for the counts
        countsList = []
        # go through the values/counts 
        for val in counts.values():
            countsList.append(val)
        # now make sure the array doesn't have any duplicates, easy trick,
        # just use the set property since a set cant have duplicates
        # the elements might not match because set() reorders them
        # but all we need to do is compare the length of the two
        return len(countsList) == len(set(countsList))
