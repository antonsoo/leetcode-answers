# Problem: 60. Permutation Sequence
# Problem link: https://leetcode.com/problems/permutation-sequence/
# # Solution by Aysuuuu
# Solution link: https://leetcode.com/problems/permutation-sequence/solutions/696782/python3-solution-explained-with-a-tip-fo-r7uu
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factor = factorial(n-1)
        k -= 1 # index starts from 1 in the question but our list indexs starts from 0
        ans = []
        numbers_left = list(range(1,n+1))
        
        for m in range(n-1,0,-1):
            index = int(k // factor)
            ans += str(numbers_left[index])
            numbers_left.pop(index)
            k %= factor
            factor /= m
            
        ans += str(numbers_left[0])
        return ''.join(ans)
