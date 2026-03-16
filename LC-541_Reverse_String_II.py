# Problem: 541 Reverse String II
# Solution link: https://leetcode.com/problems/reverse-string-ii/solutions/7639444/simple-2k-block-reversal-easy-two-pointe-fkpa/ 

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s=list(s)
        for i in range(0,len(s),2*k):
            left=i
            right=min(i+k-1,len(s)-1)
            while(left<right):
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
        return "".join(s)
