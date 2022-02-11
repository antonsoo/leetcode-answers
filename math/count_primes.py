"""
- Problem: count all the primes up to 2 to n.
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
- Descr: A prime number is a natural number greater than 1 which is only divisible by itself or 1. You can't make it using products of other natural numbers other than 1 and itself.
- Solution:
And so this algorithm will go through the list and count each *new* number as a prime, and all the then skip visiting all of the multiples of that number.
For example at first the only prime is 2, and we get rid of multiples of 2 in the array. Then we repeat with the next num we haven't seen (3), and then and then 5, 7, etc.
- Complexity: O(sqrt(n) * log(log(n))) time, O(n) space. 
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        # edge case. prime numbers start from 2. 
        if n <= 2:
            return 0
        
        # initialize the numbers array that will hold the boolean info of whether a number is a prime or not. From 0 to n total numbers.  
        numbers = [False, False] + [True] * (n - 2)
        
        # the hard part here is noticing or knowing the correct bounds.
        for p in range(2, int(sqrt(n)) + 1): # iterate through all the numbers
            if numbers[p]: # if bool value at number p is True, only goes to numbers we haven't set to False yet
                for multiple in range(p * p, n, p): # then, get rid of all prime numbers (set them all to False) in the list which is a multiple of that list
                    numbers[multiple] = False # so we dont visit it again, and so we know it's not a prime
        
        return sum(numbers) # returns the sum of True/1 values that tells us the number of primes 
