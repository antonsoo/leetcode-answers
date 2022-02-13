""" 
- note: max roman numeral without special symbols is 3999 (MMM....)
- problem: convert an integer to a roman number (string)
- solution: iterate over the integer:symbol pairs from greatest to least
if the current integer <= givenNum then count the number of times it fits in that integer, and repeat it again until you hit 0
keep appending the value you get (times the number of times it's in the integer): Ex: 478 = CDLXXVIII
"""
class Solution:
    # complexity: O(1) time and space, since the input and output will always be small
    def intToRoman(self, num: int) -> str:
        if num <= 0 or num > 3999: # edge case
            return 0
        d = OrderedDict()
        d = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
        roman_num = ""
        for integer, symbol in list(reversed(d.items())): #have to reverse it since I've initialized it from lowest to highest value.
            if num == 0: # note: num will be changed again and again
                break
            # count will be how many times we need to use that symbol, notice we don't need the step of doing the size check because
            #the division will automatically set the symbolCount value to 0 if the denominator is bigger, so symbol*0 = ""
            symbolCount, num = divmod(num, integer) # divmod returns (quotient, remainder) of, in this case: num/value
            roman_num += symbol * symbolCount
        return roman_num
    
    """
    my solution can be improved by using a list of tuples and ordering them from greatest to least, to save a bit of clocktime
    when you just iterate in order, there is no reason to use an OrderedDict over a list of tuples (you actually waste memory             because the OrderedDict keeps a copy of a dict and a doubly-linked list)
     offician solution #1 (same as the one above, but a bit better)"""
    def intToRoman8(self, num: int) -> str:
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), 
                  (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), 
                  (5, "V"), (4, "IV"), (1, "I")]
        
        roman_digits = []
        # Loop through each symbol.
        for value, symbol in digits:
            # We don't want to continue looping if we're done.
            if num == 0: break
            count, num = divmod(num, value)
            # Append "count" copies of "symbol" to roman_digits.
            roman_digits.append(symbol * count)
        return "".join(roman_digits)
    
    # faster, hard-coded solution
    def intToRoman6(self, num: int) -> str:
        thousands = ["", "M", "MM", "MMM"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        # Ex: 3895//1000 = 3.  3985 % 1000 = 895
        return (thousands[num // 1000] + hundreds[num % 1000 // 100] 
               + tens[num % 100 // 10] + ones[num % 10])
    
    
    # my failed solution
    def intToRoman2(self, num: int) -> str:
        if num <= 0 or num > 3999: # edge case
            return 0
        d = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X"}
        if num <= 10:
            return d[num]
        roman_num = ""
        for c in str(num): 
            if num < 100:
                roman_num += d[int(c)]
                continue
            elif num < 1000:
                c
            else:
                d
        return roman_num
    
    
    
