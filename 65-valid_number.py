"""
- Problem: find if an input number is valid. Ex: valid: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
- Complexity: Both solutions are O(N) time and O(1) space.
- Solutions below: (from LC answers)
"""
class Solution(object):
    def isNumber(self, s):
        # This is the DFA we have designed above
        dfa = [
            {"digit": 1, "sign": 2, "dot": 3},  # state 0
            {"digit": 1, "dot": 4, "exponent": 5}, # state 1 
            {"digit": 1, "dot": 3}, # state 2
            {"digit": 4}, # state 3
            {"digit": 4, "exponent": 5}, # state 4
            {"sign": 6, "digit": 7}, # state 5
            {"digit": 7}, # state 6
            {"digit": 7}  # state 7
        ]
        
        current_state = 0
        for c in s:
            if c.isdigit():
                group = "digit"
            elif c in ["+", "-"]: # can only be the first state, state 0
                group = "sign"
            elif c in ["e", "E"]:
                group = "exponent"
            elif c == ".":
                group = "dot"
            else:
                return False

            if group not in dfa[current_state]:
                return False
            
            current_state = dfa[current_state][group]  # Ex: sign: dfa[0]['sign'] = 2 -> state 2, which is digit or dot 
        
        return current_state in [1, 4, 7]
    
    
    
    def isNumber2(self, s: str) -> bool:
        seen_digit = seen_exponent = seen_dot =  False
        for i, c in enumerate(s):
            if c.isdigit():
                seen_digit = True
            elif c in ["+", "-"]:
                if i > 0 and s[i - 1] != "e" and s[i - 1] != "E":
                    return False
            elif c in ["e", "E"]:
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False
            elif c == ".":
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            else:
                return False
        
        return seen_digit
