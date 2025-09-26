New (Sept 2025):
class Solution:
    # credit: "Arpit Yadav" (https://leetcode.com/problems/roman-to-integer/solutions/6985405/decode-roman-numerals-in-one-pass-beat-100-with-this-elegant-trick-leetcode13)
    def romanToInt(self, s: str) -> int:
        roman_numeral_dict = {
            "I": 1,
            "V": 5, 
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        result_sum = 0 # the result we'll return
        for i in range(len(s)):
            current_num = roman_numeral_dict[s[i]]
            next_num = roman_numeral_dict[s[i + 1]] if (i + 1) < len(s) else 0

            if current_num < next_num:
                result_sum -= current_num
            else:
                result_sum += current_num
            
        return result_sum


    

    # unfinished
    def my_romanToInt(self, s: str) -> int:
        roman_numeral_dict = {
            "I": 1,
            "V": 5, 
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        string_window = []
        sum = 0

        for i in range (1, len(s)):
            print(s[i - 1], s[i]) 
