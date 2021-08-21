"""
Problem 49 -  Group Anagrams

Sucess - Found a better solution, see below
"""

from collections import Counter
class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if not strs:
            return []
        elif len(strs) == 1:
            return [strs]
        
        counters = {
            s: Counter(s) for s in strs 
        }
        
        ans = []
        
        while strs:
            string = strs.pop()
            anagrams = [string]
            for other in strs:
                if counters[string] == counters[other]:
                    anagrams.append(other)
            
            for anag in anagrams[1:]:
                strs.remove(anag)
            
            ans.append(anagrams)
        
        return ans
      
"""
The solution below is not mine, but it is brilliant
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        res = []
        c = 0
        for i, s in enumerate(strs):
            ind = tuple(sorted(s))
            if ind not in hashmap:
                hashmap[ind] = c
                c += 1
                res.append([s])
            else:
                res[hashmap[ind]].append(s)
        return res 
