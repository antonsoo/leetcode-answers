# Problem: 806. Number of Lines To Write String
# Solution source: https://leetcode.com/problems/number-of-lines-to-write-string/solutions/7210337/with-indian-tadka-cppjavapy-code-by-pras-7919/

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        total = 0
        for ch in s:
            w = widths[ord(ch) - ord('a')]
            if total + w > 100:
                lines += 1
                total = 0
            total += w
        return [lines, total]
