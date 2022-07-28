# 724 - Find Pivot Index - Easy/Top-rated - Med? - 2022Q2: GoldmanS>FB>Amzn>...  # same as 1991. Find the Middle Index in Array
# find the index of the number where numbers strictly to the right equal numbers strictly to the left (dont include that num in the calculation)
class Solution:
    # O(N) time, O(1) space
    def pivotIndex(self, nums):
        totSum = sum(nums)
        leftSum = 0
        for i, num in enumerate(nums):
            rightsum = totSum - leftSum - num # totalSum - leftSum - num (possible pivot)
            if leftSum == rightsum:
                return i # that's the index of our current num (the pivot)
            leftSum += num
        return -1 # no pivot was found
    
    
    
    
    # This solution: use two pointers from left and right, at the two ends
    # Complexity: O(nlog(n)) time from the sort, 2*O(n) ~ O(n) space
    def pivotIndex2(self, nums: List[int]) -> int:
        length = len(nums)
        lsums, rsums = [0] * length, [0] * length # keep track of the sums
        #lp, rp = 0, len(nums) - 1   # left and right pointers
        #rsums[0] = nums[length - 1]
        # can combine the two loops into one but this is more readable
        for i in range(length): 
            lsums[i] = nums[i] + lsums[i - 1] # prev sum plus the curr num
        for i in reversed(range(length - 1)):
            rsums[i] = nums[i] + rsums[i + 1]
        print(lsums)
        print(rsums)
        for rp in reversed(range(length)): # find the sum that equals
            for lp in range(length):
            # find where the number matches
                if lsums[lp] == rsums[rp]:
                    return lp + 1
        # edge case after the prev failed: all left or right numbers sum to zero:
        if lsums[length - 1] - nums[0] == 0: # so all the sums to the left are 0
            return 0 # the pivot is zero
        elif lsums[1] == 0:
            return length - 1
            #or lsums[length - 1] == 0 or rsums[1] == 0 or //
            #rsums[length - 2] == 0:
            #    return 
            
        return -1
