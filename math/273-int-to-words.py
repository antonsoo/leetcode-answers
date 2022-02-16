""" difficulty: hard+
- problem: convert an int to English words.
- Solution: divide and conquer or/and recursive solution.
"""

from collections import deque
# O(N) time, O(1) space 
class Solution:
    def numberToWords(self, num): # broken right now, some of the names are wrong for the functions
        """
        :type num: int
        :rtype: str
        """
        def one_to_nine(num):
            numsdict = {
                1: 'One',
                2: 'Two',
                3: 'Three',
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'Eight',
                9: 'Nine'
            }
            return numsdict[num]

        def ten_to_nineteen(num):
            numsdict = {
                10: 'Ten',
                11: 'Eleven',
                12: 'Twelve',
                13: 'Thirteen',
                14: 'Fourteen',
                15: 'Fifteen',
                16: 'Sixteen',
                17: 'Seventeen',
                18: 'Eighteen',
                19: 'Nineteen'
            }
            return numsdict[num]
        
        def twenty_to_ninety(num):
            numsdict = {
                2: 'Twenty',
                3: 'Thirty',
                4: 'Forty',
                5: 'Fifty',
                6: 'Sixty',
                7: 'Seventy',
                8: 'Eighty',
                9: 'Ninety'
            }
            return numsdict[num]
        

        def two(num):
            if not num:
                return ''
            elif num < 10:
                return one_to_nine(num)
            elif num < 20:
                return ten_to_nineteen(num)
            else:
                tenner = num // 10
                rest = num - tenner * 10
                return twenty_to_ninety(tenner) + ' ' + one_to_nine(rest) if rest else twenty_to_ninety(tenner)
        
        def three(num):
            hundred = num // 100
            rest = num - hundred * 100
            if hundred and rest:
                return one_to_nine(hundred) + ' Hundred ' + two(rest) 
            elif not hundred and rest: 
                return ten_to_nineteen(rest)
            elif hundred and not rest:
                return one_to_nine(hundred) + ' Hundred'
        
        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000
        
        if not num:
            return 'Zero'
        
        result = ''
        if billion:        
            result = three(billion) + ' Billion'
        if million:
            result += ' ' if result else ''    
            result += three(million) + ' Million'
        if thousand:
            result += ' ' if result else ''
            result += three(thousand) + ' Thousand'
        if rest:
            result += ' ' if result else ''
            result += three(rest)
        return result
    
    
    
    def numberToWords2(self, num: int) -> str:
        dic = {
            1000000000: "Billion",
            1000000: "Million",
            1000: "Thousand",
            100: "Hundred",
            90: "Ninety",
            80: "Eighty",
            70: "Seventy",
            60: "Sixty",
            50: "Fifty",
            40: "Forty",
            30: "Thirty",
            20: "Twenty",
            19: "Nineteen",
            18: "Eighteen",
            17: "Seventeen",
            16: "Sixteen",
            15: "Fifteen",
            14: "Fourteen",
            13: "Thirteen",
            12: "Twelve",
            11: "Eleven",
            10: "Ten",
            9: "Nine",
            8: "Eight",
            7: "Seven",
            6: "Six",
            5: "Five",
            4: "Four",
            3: "Three",
            2: "Two",
            1: "One",
            0: "Zero",
        }
        if num == 0: return dic[0]
        
        segments = [float("inf"), 1000000000, 1000000, 1000, 100, 90, 80, 70, 60, 50, 40, 30, 20]
        
        def numberToWords(number):
            nonlocal dic, segments
            ret = deque()
            for i in range(1, len(segments)):
                if segments[i] <= number < segments[i-1]: # only true when number bigger or equal to the number prev segment
                    div, rest = number // segments[i], number % segments[i]
                    ret.append(dic[segments[i]])
                    if rest > 0: ret.append(numberToWords(rest))
                    # We say "One Hundred", "One thoushand" but we don't say "One Fifty", we simply say "Fifty":
                    if div > 0 and i < 5: 
                        ret.appendleft(numberToWords(div))
                    return " ".join(ret)
            return dic[number]
            
        return numberToWords(num)
