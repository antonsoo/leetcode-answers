# Date Submitted/Worked on: Sep 18-19, 2025
# Problem: LC # 6: "Zigzag Conversion" 
# Problem type (category): Strings
# Problem link: https://leetcode.com/problems/zigzag-conversion/
# Solution credit: Niits; link: https://leetcode.com/problems/zigzag-conversion/solutions/6146922/two-points-to-solve-the-question
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        idx, d = 0, 1
        rows = [''] * numRows

        for char in s:
            rows[idx] += char
            if idx == 0:
                d = 1
            elif idx == numRows - 1:
                d = -1
            idx += d

        return ''.join(rows)  
