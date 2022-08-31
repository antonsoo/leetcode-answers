#205. Isomorphic Strings - 'Easy'/Med - 2022Q2: Amzn/LinkedIn/Google
# Two strings s and t are isomorphic if the characters in s can be replaced to get t. 
# Basically, it needs to have that same number of characters for that specific character in the same places if replaced.
# Ex: s="egg" has two chars 'g' in the 2nd & 3rd place. t='add'. Replacement: e->a, g->d. 
#so it's the same character 'd' that's used in 2nd&3rd place. 
class Solution:
  
    # O(N) time go through each string once. O(1) because only so many ASCII.
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_s_t = {}
        mapping_t_s = {}
        
        for c1, c2 in zip(s, t):
            # Case 1: No mapping exists in either of the dictionaries
            if (c1 not in mapping_s_t) and (c2 not in mapping_t_s):
                mapping_s_t[c1] = c2
                mapping_t_s[c2] = c1
            # Case 2: Either mapping doesn't exist in one of the dictionaries or Mapping exists and
            # it doesn't match in either of the dictionaries or both 
            # .get is only useful if u want to provide a default key, so not here..
            elif mapping_s_t.get(c1) != c2 or mapping_t_s.get(c2) != c1:
                return False
            
        return True    
    
    
    
    
    # second method: O(N) time and space complexity
    def transformString2(self, s: str) -> str:
        index_mapping = {}
        new_str = []
        
        for i, c in enumerate(s):
            if c not in index_mapping:
                index_mapping[c] = i
            new_str.append(str(index_mapping[c]))
        
        return " ".join(new_str)
    
    def isIsomorphic2(self, s: str, t: str) -> bool:
        return self.transformString(s) == self.transformString(t)
    
    
    
    
    # my failed attempt
    def isIsomorphic3(self, s: str, t: str) -> bool:
        used = {} # dict
        used_t = set() # set #note: ={} initializiation doesn't work
        for i, ch in enumerate(s):
            if ch not in used: # case that char from s not seen yet:
                used[ch] = t[i] 
                if t[i] not in used_t: # char from s&t not seen yet:
                    used_t.add(ch)
            else: # case that char from s seen already
                decoding_ch = used[ch]
                # check if the char decoding matches
                if decoding_ch == t[i]:
                    continue
                else:
                    return False
        return True
                 
