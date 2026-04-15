# Problem: 395. Longest Substring with At Least K Repeating Characters
# Solution: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/solutions/949688/python-short-simple-recursive-solution-b-ccti/

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) == 0 or k > len(s):
            return 0
        c = Counter(s)
        sub1, sub2 = "", ""
        for i, letter in enumerate(s):
            if c[letter] < k:
                sub1 = self.longestSubstring(s[:i], k)
                sub2 = self.longestSubstring(s[i+1:], k)
                break
        else:
            return len(s)
        return max(sub1, sub2)
