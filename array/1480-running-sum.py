# 1480 - Running Sum of 1d Array - Easy - Amzn/Adobe/Appl
# Problem: return the array like: runningSum[i] = sum(nums[0]…nums[i]).
# Complexity: O(n) time, O(1) space (if we dont count the output array)
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = [nums[0]]
        for i in range(1, len(nums)):
            output.append(nums[i] + output[i - 1])
        return output
    
# Note: can also do nums[i] += nums[i-1] if we want to overwrite the original array
