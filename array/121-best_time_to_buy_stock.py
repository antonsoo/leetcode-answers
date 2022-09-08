""" 121 - Easy - LC75 - Best Time to Buy and Sell Stock - 2022Q1: Amzn>FB>Blmbg/Msft
"""

#import sys
class Solution:   
    def maxProfit(self, prices: List[int]) -> int:
        # one pass solution: O(n) time, O(1) space
        # really easy: just keep track of the smallest price and largest profit so far.
        minprice = float('inf') # prices[0] also works... #sys.maxsize  #initialize as largest int
        maxprof = 0  # maximum profit, i.e., max positive difference
        for day in range(len(prices)): # prices of stocks per day... just numbers in an array
            curr_diff = prices[day] - minprice
            if prices[day] < minprice: # find the min price in the whole list
                minprice = prices[day] 
            elif curr_diff > maxprof: # is the current difference between current day and minprice, the largest possible so far?
                maxprof = curr_diff # if it is, the reset the maxprof to be the current largest diff
        return maxprof

        
       
    #the brute force approach, runs out of time:  O(n**2) time, O(1) space
    def maxProfit3(self, prices: List[int]) -> int:
        maxprof = 0
        for i in range(len(prices) - 1):    #this num is always behind
            for j in range(i+1, len(prices)): #this num is always ahead by 1
                prof = prices[j] - prices[i] #compared the diff: num_ahead - num_behind
                if prof > maxprof:
                    maxprof = prof
        return maxprof
    
    
    # this doesn't work because the min or max price might not reset in the future, and it will count the past one    
    def maxProfit3(self, prices: List[int]) -> int:
        minprice = float('inf') #sys.maxsize  #initialize as largest int
        maxprice = float('-inf')  
        for i in range(len(prices)): #prices of stocks per day... just numbers in an array
            if prices[i] < minprice: #find the min price in the whole list
                minprice = prices[i] 
            if prices[i] > maxprice:
                maxprice = prices[i]
        print(maxprice, minprice)
        return maxprice - minprice
