class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # O(n) time, O(1) space
        # extension of Kadane's algorithm!! we need to do this since we also have negative products which might become positive later
        # here we use an extra local sum (so min and max sums) to find the largest neg and pos values
        # this is because two large neg values can multiple to produce a larger positive value
        
        if len(nums) < 2:
            return nums[0]
        
        l_max_sum = nums[0]
        l_min_sum = nums[0]
        g_sum = nums[0] # result
        
        for num in nums[1:]:
            temp_l_max_sum = max(num, l_max_sum * num, l_min_sum * num) # to find the lagest pos val
            l_min_sum = min(num, l_min_sum * num, l_max_sum * num) # to find the largest neg val
            l_max_sum = temp_l_max_sum
            
            g_sum = max(l_max_sum, g_sum)
        return g_sum
