"""
Problem 567 - Permutation in String

Sucess - Faster than 92% attempts!
"""

from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)
        
        target = Counter(s1)
        cache = Counter(s2[:m])
        
        if cache == target:
            return True
        
        if n == m:
            return False
        
        for i in range(1, n-m+1):
            old = s2[i-1]
            new = s2[i+m-1]
            
            if cache.get(old) == 1:
                del cache[old]
            else:
                cache[old]-=1
            
            if cache.get(new) is None:
                cache[new] = 1
            else:
                cache[new]+=1
              
            if cache == target:
                return True
            
            
