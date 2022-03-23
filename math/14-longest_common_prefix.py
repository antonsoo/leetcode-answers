#14 - Longest Common Prefix - Easy (I think it's Medium+) - Facebook>Apple>Amazon>Google
class Solution:
    # O(len(strs))->O(n) time, O(max word len in strs)->O(m) space for the result
    def longestCommonPrefix3(self, strs): # solution thx to user "pye"
        prefix = ""
        if len(strs) == 0: 
            return prefix
        for i in range(len(min(strs))): # min will return the smallest lexigraphically value, so the first item if u order the list of strs
            curr_ch = strs[0][i] # initialize as the char in the first word each time
            # all() returns True if all bool values in that collection are True
            if all(word[i] == curr_ch for word in strs): # O(len(strs))
                prefix += curr_ch # if that char is indeed present in all strings then add it to the prefix
            else:
                break
        return prefix
		
    """
     - another solution: nlog(n) time, O(m) space for the result, and technically O(nlogn) space for sorting
     compares the lexiconically smallest string (smallest possible window/prefix) with the lexiconically  
     largest string, and stores as much of the matching characters as possible as the prefix
     sort between strings will sort in lexiconical order, like so: 
    ['flight', 'flo', 'flower', 'flowerknight']
     so you see the 0'th string is the one not matching the most, so we compare it to the last string
    - and the reason why we compare it to the [-1]'th string is because if there is only one string in the 
    array, then we just set that only string to be itself, so we dont have to write out that edge case.
	"""
    def longestCommonPrefix(self, strs): # solution thx to user "zhengzhicong"
        if len(strs) == 0:
            return "" 
        prefix = ""
        strs = sorted(strs)
        for ch in strs[0]:
            if strs[-1].startswith(prefix + ch):
                prefix += ch
            else:
                break
        return prefix
    
    
    
    
    
    # my failed solution, runs out of time, but works for many cases
    def longestCommonPrefix2(self, strs: List[str]) -> str:
        LCP = "" # longest common prefix
        
        if len(strs) ==  0: # edge case
            return LCP
        if len(strs) == 1: # edge case, one str
            return strs[0]
        
        char_i = -1 # keep track of chars in a word
        while 1:
            char_i += 1
            # go through each word 
            for word_j in range(len(strs)): 
                #print(strs[word_j])
                if char_i >= len(strs[word_j]): # ran out of length
                    break
                # initialize LPM prefix to the first word's next prefix
                if word_j == 0: 
                    LCP += strs[0][char_i] # add the prefix
                    continue
                # compare if each word matches the current prefix
                if strs[word_j][char_i] == LCP[char_i]:
                    continue    
                else:
                    return LPM[:-1]
        return LCP

    
