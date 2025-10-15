# Problem link: https://leetcode.com/problems/longest-valid-parentheses/description/
# LeetCode Problem number 32: "Longest Valid Parentheses"
# Solution link: https://leetcode.com/problems/longest-valid-parentheses/solutions/5373015/stack-solution-video-explanation/
# This solution is from the user nick-named "niits"
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        
        return max_len
