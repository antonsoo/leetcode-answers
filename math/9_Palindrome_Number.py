# Sept 8, 2025:
class Solution:
    # the "Oh, I know the precise formula for this" / "my brain is bigger than my house" solution (credit to the user named `niits`)
    # Complexity: Time:O(log(x)); Space:O(1)
    def isPalindrome(self, x: int) -> bool:
        # fail case (negative number)
        if x < 0:
            return False
        
        # initialize the reverse and xcopy
        reverse = 0
        xcopy = x
        
        while x > 0:
            reverse = (reverse * 10) + (x % 10)
            x //= 10
        
        return reverse == xcopy
    


    # my solution:
    def my_isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        xstr = str(x)
        if xstr == xstr[::-1]:
            return True
        else:
            return False
