# Solution: https://leetcode.com/problems/rotate-function/solutions/7795196/two-simple-lines-of-code-by-mikposp-559j/
# 396. Rotate Function

class Solution:
    def maxRotateFunction(self, a: List[int]) -> int:
        return max(accumulate(reversed(a), 
            lambda F,v,q = sum(a):F+q - v*len(a),
            initial = sum(map(mul, a, count())) ) )
