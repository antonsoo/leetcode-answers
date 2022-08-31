# 392. Is Subsequence - Easy - 2022Q3:Google/Amzn/Adobe
class Solution:
    def isSubsequence(self, subs: str, target: str) -> bool:
        # s = subsequence, t = target (whole sequence)
        # Two pointer solution: O(|T|) (length of target string) time, O(1) space
        #LEFT_BOUND, RIGHT_BOUND = len(subs), len(target)

        # summary: just have two pointers that look over the two strings, increase the pointer on the subsequence if it matches, or don't if it doesn't match. Always increase the target string pointer. 
        left_pointer = right_pointer = 0
        while left_pointer < len(subs) and right_pointer < len(target):
            # move both pointers or just the right pointer
            if subs[left_pointer] == target[right_pointer]:
                left_pointer += 1
            right_pointer += 1

        return left_pointer == len(subs) # returns True if the whole subsequence got matched, i.e., it finished traversing through the substring
