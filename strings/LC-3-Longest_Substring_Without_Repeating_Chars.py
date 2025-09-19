# Sept 14-18, 2025
# LC Problem Number 3: "Longest Substring Without Repeating Characters"
# Sep 14-19, 2025
# Problem link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Soltion credit: https://leetcode.com/problems/longest-substring-without-repeating-characters/solutions/3649636/3-method-s-c-java-python-beginner-friendly
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charSet = set()
        left = 0

        for right in range(n):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLength = max(maxLength, right - left + 1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])

        return maxLength



    # Solution credit: Kani -- https://leetcode.com/problems/longest-substring-without-repeating-characters/solutions/3649636/3-method-s-c-java-python-beginner-friendly/comments/2110217/
    def deq_lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        q = deque()
        for c in s:
            if c in q:
                while q.popleft() != c:
                    pass
            q.append(c)
            res = max(res, len(q))
        
        return res
