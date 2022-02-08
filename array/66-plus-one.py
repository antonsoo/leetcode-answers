"""
- Problem: Add 1 to an array representing a digit. Ex: [1, 2, 9] + 1 = [1, 3, 0] or [9, 9] + 1 = [1, 0 ,0]
- Solution: Can do it in place. go through the array and see if the digits from the end are 9, change them to zeros.
If the digit is not 9, then add 1 to that digit, and return the array because we're done.
If you go through all the numbers and they're all 9, then the algorithm will automatically change all of them to zeros. All you have to do is add [1] in front.
- Complexity: O(N) time, O(N) space (in the worst case)
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        # move along the input array starting from the end
        for i in range(n):
            idx = n - 1 - i
            # set all the nines at the end of array to zeros
            if digits[idx] == 9:
                digits[idx] = 0
            # here we have the rightmost not-nine
            else:
                # increase this rightmost not-nine by 1
                digits[idx] += 1
                # and the job is done
                return digits

        # we're here because all the digits are nines
        return [1] + digits
