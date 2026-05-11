# 386. Lexicographical Numbers
# Solution: https://leetcode.com/problems/lexicographical-numbers/solutions/5814160/python-dfs-by-khosiyat-3xyb/

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        curr = 1
        for _ in range(n):
            result.append(curr)
            if curr * 10 <= n:
                curr *= 10  # Move to the next depth (append 0 at the end)
            else:
                while curr % 10 == 9 or curr + 1 > n:
                    curr //= 10  # Backtrack by removing the last digit
                curr += 1  # Increment to the next number in lexicographical order
        return result
