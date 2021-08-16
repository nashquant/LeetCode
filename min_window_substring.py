"""
Problem #76 - Minimum Window Substring

264/266 cases passed

Still trying to enhance performance
to pass the last 2 cases.

"""

from collections import Counter

class Solution:
    
    def check_sub(self, ref: Counter, counter: Counter) -> bool:
        ans = True
        
        for elem in ref:
            if counter[elem] < ref[elem]:
                return False
        return True
            
    
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        null = ""
        
        if n>m: return null
        
        ref = Counter(t)
        
        for j in range(n, m+1):
            for i in range(m-j+1):
                sub = s[i:i+j]
                counter = Counter(sub)
                if self.check_sub(ref, counter):
                    return sub
                
        return null

        
        
