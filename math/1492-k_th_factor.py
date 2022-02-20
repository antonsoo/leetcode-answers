""" 1492: k-th factor of n. Diff'y: Medium. Companies: Amazon/etc
- Problem: Find the k-th factor of an integer n
A factor of an integer n is defined as an integer i where n % i == 0. (Divisors that have no (zero) remainder)
"""
class Solution:
    # elegant brute force solution with no space used:
    #If we use a list to store the factors, and just return the kth one, it would be even easier
    # O(n/2)->~O(n) time, O(1) space
    def kthFactor1(self, n: int, k: int) -> int:
        for x in range(1, n // 2 + 1):
            if n % x == 0:
                k -= 1
                if k == 0:
                    return x
        return n if k == 1 else -1
    
    
    # heap solution: O(sqrt(N) * log(k)) time, O(min(k, sqrt(N))) space
    # a max heap will keep the biggest element on the heap head
    def kthFactor2(self, n: int, k: int) -> int:
        # push into the heap by limiting size of heap to k
        # The Python heap is a min heap so to keep the max element always on top, push negative values
        def heappush_k(num):
            heappush(heap, -num)
            if len(heap) > k: # ran out of space, pop the head and you have the answer
                heappop(heap) # heappop is already implemented
        heap = []
        for x in range(1, int(n**0.5) + 1): #Iterate x from 1 to sqrt(N)
            if n % x == 0: # if x is a divisor of n with no remainder (so it's a factor)
                heappush_k(x) # push x
                if x != n // x: # also push n//x, which is the factor we just got, if it's not the same as x
                    heappush_k(n // x)
        # now pop the head if the heap is of size k, or -1 otherwise       
        return -heappop(heap) if k == len(heap) else -1

    
    # math solution: O(sqrt(n)) time, O(min(k, sqrt(N))) space
    def kthFactor(self, n: int, k: int) -> int:
        divisors, sqrt_n = [], int(n**0.5)
        for x in range(1, sqrt_n + 1):
            if n % x == 0:
                k -= 1
                divisors.append(x)
                if k == 0:
                    return x
        # If n is a perfect square
        # we have to skip the duplicate 
        # in the divisor list
        if (sqrt_n * sqrt_n == n):
            k += 1       
        n_div = len(divisors)
        return n // divisors[n_div - k] if k <= n_div else -1
    
