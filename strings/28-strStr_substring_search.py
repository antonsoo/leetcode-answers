#28. Implement strStr() - "Easy" (Medium?) - Microsoft/Amazon/Google/etc
class Solution:
    
    # Python's inbuilt method. It might actually be sublinear because of tricks, etc.
    def strStr8(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
    
    # sliding window approach, window length will be Nlen
    # O(Hlen*Nlen) time (?), O(Nlen) space (?)
    def strStr2(self, haystack: str, needle: str) -> int:
        Hlen, Nlen = len(haystack), len(needle)
        if Nlen == 0: # either both are empty, or just the needle string
            return 0
        elif Hlen == 0 or Hlen < Nlen: # only Hlen is empty, so they don't match. Or the needle is bigger
            return -1 
        
        for i in range(Hlen): # sliding window. iterate from each 
            if i + Nlen > Hlen: # window is too big now
                return -1
            # check if the part of the string that's the same size as the window equals the window
            elif haystack[i : i + Nlen] == needle: 
                return i
        return -1 # no match was ever found
    
    #O(Hlen*Nlen) time, O(Nlen) space
    # shorter version of the above: # same runtime as above... which is pretty good. Second best after KMP but better memory than KMP.
    def strStr5(self, haystack: str, needle: str) -> int:
        Hlen, Nlen = len(haystack), len(needle)
        for i in range(0, Hlen - Nlen + 1):
            if haystack[i : i + Nlen] == needle:
                return i
        return -1
          

    #Rabin Karp, built-in hash, constant time (tested). Much slower than the code above.
    #computing the hash of a string is a more complex operation than just comparing it to another string
    def strStr8(self, haystack, needle):
        Hlen, Nlen = len(haystack), len(needle)
        hash_n = hash(needle)
        for i in range(Hlen - Nlen + 1):
            if hash(haystack[i : i + Nlen]) == hash_n:
                return i
        return -1

    #Rabin Karp, numeral base for both uppercase and lowercase letters, constant time
    # awful run time for some reason, like 20x more than the other approache sabove
    def strStr6(self, haystack, needle):
        def f(c):
            return ord(c)-ord('A')
        n, h, d, m = len(needle), len(haystack), ord('z')-ord('A')+1, sys.maxsize
        if n > h: return -1
        nd, hash_n, hash_h = d**(n-1), 0, 0   
        for i in range(n):
            hash_n = (d*hash_n+f(needle[i]))%m
            hash_h = (d*hash_h+f(haystack[i]))%m            
        if hash_n == hash_h: return 0        
        for i in range(1, h-n+1):
            hash_h = (d*(hash_h-f(haystack[i-1])*nd)+f(haystack[i+n-1]))%m   # e.g. 10*(1234-1*10**3)+5=2345
            if hash_n == hash_h: return i
        return -1

    #KMP. The fastest performance but worst memory out of the ones I've tested. up to 2x (or more?) compared to just using list comparison (no hashes). O(n+m) time?
    def strStr(self, haystack, needle):
        n, h = len(needle), len(haystack)
        i, j, nxt = 1, 0, [-1]+[0]*n
        while i < n:                                # calculate next array
            if j == -1 or needle[i] == needle[j]:   
                i += 1
                j += 1
                nxt[i] = j
            else:
                j = nxt[j]
        i = j = 0
        while i < h and j < n:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = nxt[j]
        return i-j if j == n else -1        
      
        
    # here I try to reinvent the KMP I think
    # fails when the new attempted string is part of the old failed attempt. Ex: "mississippi"  "issip"
    # pointer approach, go through the haystack, if the current string starts matching the needle
    # also another error
    def strStr2(self, haystack: str, needle: str) -> int:      
        Hlen, Nlen = len(haystack), len(needle)
        if Nlen == 0: # either both are empty, or just the needle string
            return 0
        elif Hlen == 0 or Hlen < Nlen: # only Hlen is empty, so they don't match. Or the needle is bigger
            return -1  
            
        # pointer approach, go through the haystack, if the current string starts matching the needle
        #then start counting the needle, unless they start to mismatch before the needle ends
        np = 0 # needle pointer, to go through the needle string
        needle_index = -1 
        for ind, ch in enumerate(haystack):
            if ch == needle[np]:
                if np == 0: # if we're seeing a new potential needle match, set the start of that index
                    needle_index = ind
                    print(needle_index)
                np += 1
                if np < len(needle) + 1:  # still have to iterate
                    continue
                else: # done, iterated through the entire needle
                    break
            else: # reset the value and index
                np = 0
                needle_index = -1 
        return needle_index
