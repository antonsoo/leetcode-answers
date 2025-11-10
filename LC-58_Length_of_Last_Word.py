# Problem # 58: Length of Last Word
# Problem link: https://leetcode.com/problems/length-of-last-word/
# Solution by: Me (Anton Soloviev)
# Date: Nov. 9, 2025
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0
        l = len(s) - 1

        empty_counter = 0
        if s[l] == " ":
            for i in range(l, -1, -1):
                if s[i] != " ":
                    break
                empty_counter += 1

        for i in range(l - empty_counter, -1, -1):
            if s[i] == " ":
                break
            else: 
                counter += 1

        return counter
