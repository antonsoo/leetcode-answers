"""
problem: create a superset (all combinations of all subsets) of a given set (technically an array is given). Assume no edge cases.
solution: (easy one) simply combine one subset with another, and keep going the index of the num you combine the set with.
complexity: N * 2**N time, N * 2**N space  ... can be improved further to O(N) space
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powersetOutput = [[]] # output. Already initialize the empty set (technically, array).
        for num in nums:
            powersetOutput += [(subset + [num]) for subset in powersetOutput]
        return powersetOutput

    
"""
Ex: start with [[]]  , input [1, 2, 3] 
combine [] with [1]: [], [1]
next: [], [1] combine with [2]: [],[1],[2],[1, 2]  (notice how we go one by one following the formula above)
next:  [],[1],[2],[1, 2] with [3], . .. 
"""
