# 344. Reverse String - Easy - Microsoft/Amazon/etc
class Solution:
    # O(N/2) -> ~O(N) time, O(1) space
    # Can also use s.reverse()
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # two pointers at two ends, increase one, decrease the other. 
        p1 = 0
        p2 = len(s) - 1
        while p1 < p2:
            s[p1], s[p2] = s[p2], s[p1]
            p1 += 1
            p2 -= 1
