# Date: Sep 28-29, 2025
# LC # 17. "Letter Combinations of a Phone Number"
# Problem Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Solution Credit: LC user nick-named "vanAmsen"
# Solution link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/solutions/3855474/100-backtracking-iterative-video-letter-combinations-of-a-phone-number
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        combinations = [""]

        for digit in digits:
            new_combinations = []
            for combination in combinations:
                for letter in phone_map[digit]:
                    new_combinations.append(combination + letter)
            combinations = new_combinations

        return combinations
