""" 53 - Maximum Subarray - Easy (I'd say the O(1) space solution is Med) - 2022Q1: Amzn>LI>>App>etc 
- A subarray is a contiguous part of an array.
- We don't need to remember where the subarray was located, we just want the largest sum. This makes the problem easier.
- best solution: Kadane's algorithm
For O(1) space, overwrite the array elements to store the best current running sum.
So start at one element, run for as much as you can, record the final value (the whole running sum) as the max_sum if it indeed higher than the current value itself.
Any array that has a positive sum is worth keeping, any that doesn't have that isn't worth keeping, instead restart it from that new point, if it keeps having a positive running sum, then keep it going.
So we're skipping over all the negative numbers, by just writing them as the max_number (if it is indeed the highest negative value out of only negative values). 
Note: it's not like we're disregarding any array that has a negative in it. We do consider it if the overall current sum is positive.
We stop the loop once the index hits the end.

"""
class Solution:
    #Kadane's algorithm: O(n) space, O(1) space if modified in place which we do. Very similar to the greedy approach (and same complexity)
    #difference between the greedy approach is that it uses an extra variable called curr_sum to keep track of the curr/local sum
    def maxSubArray(self, nums: List[int]) -> int:
        #but this algorithm just uses an if statement for that purpose.
        max_sum = nums[0] #initialize to the first num
        for i in range(1, len(nums)):  #start at 1 since we'll go to 0th element 
            if nums[i - 1] > 0: #if the previous num is positive
                nums[i] += nums[i - 1] #then add it to the current num, that is the current/local max sum
            #each time, calculate the total/true max sum to be the highest num between current num (i.e., current/local max sum) and the global max sum
            max_sum = max(nums[i], max_sum) 
        return max_sum #return the global max sum
    
    
    
    # divide-and-conquer: O(N*log(N)) time, O(log(N)) space 
    # first divide by left and right. Do the left side first, then do the right side.
    # repeat recursively.
    def maxSubArray2(self, nums: List[int]) -> int:
        def findBestSubarray(nums, left, right):
            # Base case - empty array.
            if left > right:
                return -math.inf

            mid = (left + right) // 2
            curr = best_left_sum = best_right_sum = 0

            # Iterate from the middle to the beginning.
            for i in range(mid - 1, left - 1, -1):
                curr += nums[i]
                best_left_sum = max(best_left_sum, curr)

            # Reset curr and iterate from the middle to the end.
            curr = 0
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                best_right_sum = max(best_right_sum, curr)

            # The best_combined_sum uses the middle element and
            # the best possible sum from each half.
            best_combined_sum = nums[mid] + best_left_sum + best_right_sum

            # Find the best subarray possible from both halves.
            left_half = findBestSubarray(nums, left, mid - 1)
            right_half = findBestSubarray(nums, mid + 1, right)

            # The largest of the 3 is the answer for any given input array.
            return max(best_combined_sum, left_half, right_half)
        
        
        # Our helper function is designed to solve this problem for
        # any array - so just call it using the entire input!
        return findBestSubarray(nums, 0, len(nums) - 1)
