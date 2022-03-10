""" 20 - Valid Parentheses - 2022Q1:Amazon>LinkedIn>>Microsoft>FB>etc etc
"""
# O(n) time and space
class Solution:
    def isValid(self, s: str) -> bool: # dont have to consider input as not empty or wrong
        left = "[({" # right = "])}"
        stack = []
        for ch in s:
            if ch in left: # if this char is indeed one of the left parentheses' types
                stack.append(ch)
            else: # else got a right bracket
                if len(stack) == 0: # code below doesnt work if the stack is already empty cuz it's only right paranthasis on the stack, no opening/left para. we will actually assume we will never encounter this kind of input. but this part will make sure we don't go out of bounds
                    return False
                # then check if the current char matches what's on top of the stack (the last char we put on the stack)...pop if so
                elif ch == "}" and stack[-1] == "{":
                    stack.pop() # pop c
                elif ch == ")" and stack[-1] == "(":
                    stack.pop() # pop c
                elif ch == "]" and stack[-1] == "[":
                    stack.pop() # pop c
                else: # we got some junk input, not left or right bracket:
                    return False
        return len(stack) == 0 # returns True if len=0 ... meaning everything got popped
    
    
    # official answer:
    def isValid2(self, s):
        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'  # if stack, returns True if "stack" is not an empty list

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack # return True (paranthases match) if the stack is not empty->stack would return False -> not(False) = True
        
        
        
        #stolen answer:
        # go through the string and replace every pair of types of parantheses, if they exist, with the none char
        # after it's finished, just make sure everything indeed got matched completely
        # while "()" in s or "{}" in s or '[]' in s:
        #     s = s.replace("()", "").replace('{}', "").replace('[]', "")
        # return s == ''
        
        
