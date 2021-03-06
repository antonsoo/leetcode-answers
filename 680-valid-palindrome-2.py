class Solution:
    #680. Valid Palindrome II
    def validPalindrome(self, s: str) -> bool:
    # thanks to: https://leetcode.com/problems/valid-palindrome-ii/discuss/107718/Easy-to-Understand-Python-Solution
    # two pointers solution: O(n) time, O(n) space
        left_p = 0
        right_p = len(s) - 1
        while left_p < right_p:
            if s[left_p] != s[right_p]:
                left_str = s[left_p + 1: right_p + 1] # deleting the left char (remember: if we dont want to cut the right_p out, add +1)
                right_str = s[left_p: right_p] # deleting the right char (by simply leaving it out of the string slicing)
                return self.isPali(left_str) or self.isPali(right_str)
            left_p += 1
            right_p -= 1
        return True
    def isPali2(self, s):
        # O(n) time and O(1) space
        left_p = 0 
        right_p = len(s) - 1
        while left_p < right_p:
            if s[left_p] != s[right_p]:
                return False
            left_p += 1
            right_p -= 1
        return True
    def isPali(self, s): # this is actually faster because string reversal is implemented in C unlike my for loop above
        # O(n) time and space (O(n) time for slicing and O(n) time for comparing)
        return s == s[::-1]
    
    
    
    
#     def validPalindrome(self, s: str) -> bool:
#         # two pointers, O(n) time, O(1) space
#         deleted = 0
#         left_p = 0
#         right_p = len(s) - 1
#         if len(s) <= 1:
#             return True
        
#         didnt_fail1, didnt_fail2 = True, True
#         # my code will always delete the right char, but can make it random
#         while deleted < 2 and left_p < right_p:
#             if s[left_p] == s[right_p]:
#                 left_p += 1
#                 right_p -= 1
#             elif deleted < 2:
#                 print(s[left_p], s[right_p], 1)
#                 right_p -= 1
#                 deleted += 1
#                 if s[left_p] == s[right_p]:
#                     continue
#                 else:
#                     didnt_fail1 = False
#             else:
#                 didnt_fail1 = False
#         deleted = 0
#         left_p = 0
#         right_p = len(s) - 1
#         while deleted < 2 and left_p < right_p:
#             if s[left_p] == s[right_p]:
#                 left_p += 1
#                 right_p -= 1
#             elif deleted < 2:
#                 print(s[left_p], s[right_p], 2)
#                 left_p += 1
#                 deleted += 1
#                 if s[left_p] == s[right_p]:
#                     continue
#                 else:
#                     didnt_fail2 = False
#             else:
#                 didnt_fail2 = False
#         return didnt_fail1 or didnt_fail2
        
