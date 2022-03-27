"""384. Shuffle an Array - Easy->"Medium" (I think it's hard) - 2022Q1:Google>>Uber>Amzn
- both solutions use the Fisher-Yates algorithm. The optimal solution is just a more
computer optimized version of it.
- the input nums is like this: [1, 2, 3]
- the output of each function is also just an array like [3, 1, 2] if it's shuffled
""" 

# the un-optimized Fisher-Yates algo solution: O(n^2) time, O(n) space
class Solution:
    def __init__(self, nums):
        self.array = nums
        self.original = nums[:] # just a copy of all the elements from the original

    def reset(self):
        self.array = self.original # self.array now points to the self.original array
        self.original = self.original[:] # a copy of all the elements from the original
        return self.array # the original copy

    # randomly chooses a number it hasn't already used in the original array
    # appends it to the array copy we made. Returns that copy at the end
    def shuffle(self):
        aux = self.array[:] # a second copy of all the elements in self.array
        # for each index in the first copy, you randomly choose elements from the second copy
        # and assign them to the values at that index (going from 0 to the end) using the loop
        for idx in range(len(self.array)):
            remove_idx = random.randrange(len(aux))
            self.array[idx] = aux.pop(remove_idx)
        #print(self.array)
        return self.array
    
    
# the optimized solution: O(n) time and space
class Solution2:
    def __init__(self, nums):
        self.array = nums
        self.original = nums[:]

    def reset2(self):
        self.array = self.original
        self.original = self.original[:]
        return self.array

    # randomly chooses two indices in the array and swaps them, 
    # returns n number of arrays with those random swaps
    def shuffle2(self):
        for i in range(len(self.array)):
            swap_idx = random.randrange(i, len(self.array))
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array
