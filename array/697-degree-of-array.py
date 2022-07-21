# problem: return  the length of the subarray that has the degree of the array
#i.e., find the element that occures the most in the array, that's the degree
#then find the subarray that contains all the elements of that most-occuring int and all the 
#numbers inbetween those. Ex: [1,2,2,3,1,4,2]. 222 is the most repeating. 
#then just return the subarray that has all the 2's in there: [2,2,3,1,4,2]
# Question I have: if it's like [1, 1, 1, 3, 2, 2, 2] my algorithm will take 1, but should we instead count 1 as being the number of the degree? or the evaluation of this problem will work with both?
#Actually when u have the degrees of two nums being equal, you need to try all the possible subarrays of each of those nums, and find the one with the smallest length (and the degree responsible for it)
# Problem: 697. Degree of an Array (Easy): Bunch of companies
class Solution:
    # O(n) time and space
    def findShortestSubArray(self, nums):
        left, right, count = {}, {}, {}
        for ind, num in enumerate(nums):
            if num not in left: # first occurence of that number only
                left[num] = ind
            right[num] = ind # changes after each occurence for that number
            # also populate the count dictionary:
            count[num] = count.get(num, 0) + 1 # gets a value for the key (num) if it exists, otherwise it puts a zero in that place for that key, and it adds 1 (so the count goes up)

        ans = len(nums) # answer is the subarray with the highest degree and smallest length
        degree = max(count.values()) # the degree
        for num in count: # go through the array and find the value that c
            if count[num] == degree:
                ans = min(ans, right[num] - left[num] + 1)
        return ans
    
    # this approach:
    #count all the occurences of the numbers, take the one with the highest occurence
    #then find the number in the original array (where it begins), and where it ends
    #do this from the end, until u find that number. Then return the subarray.
    # Complexity: O(n) time, O(n) worst space
    # my approach can be fixed by storing the first and last indices of all the numbers that correspond to the highest index so that we could pick out the number that corresponds to the smallest array (out of those highest index nums)
    from collections import Counter
    def findShortestSubArray2(self, nums: List[int]) -> int: # not working
        counts = Counter(nums)
        maxval = 0 
        maxkey = 0 # assume no negative keys
        for key, val in counts.items(): # find the num that repeats the most
            if val == maxval: # can write this whole thing more Pythonically, but a bit hard
                maxkey = key  
                maxval = val
        first_ind = 0 # first index where the most repeating num (degree) occurs
        last_ind = len(nums) - 1 # last index where it occurs
        #print(counts)
        #print(maxkey)
        for ind, num in enumerate(nums): # now find the correct indices
            if num == maxkey: 
                first_ind = ind
                break
        print(first_ind)
        for ind, num in reversed(list(enumerate(nums))): # now do it backwards, last ind
            #print(num)
            if num == maxkey:
                last_ind = ind # - 1  
                break
        print(first_ind, last_ind)
        return last_ind - first_ind + 1  #nums[first_ind : last_ind]

        
