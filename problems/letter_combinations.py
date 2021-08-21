"""
Problem 17 -  Letter Combinations of a Phone Number

Sucess

"""

class Solution:
    
    def combine(self, arr1: Sequence[str], arr2: Sequence[str]) -> Sequence[str]:
        
        result = []
        
        for a1 in arr1:
            for a2 in arr2:
                a = a1 + a2
                result.append(a)
                
        return result
    
    def letterCombinations(self, digits: str) -> List[str]:
        
        MAPPER = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z'],
        }
        
        if not digits or digits.isspace():
            return []
        
        arrays = []
        
        for char in digits:
            arrays.append(MAPPER[char])
            
        ans = arrays[0]
        
        for i in range(1, len(arrays)):
            ans = self.combine(ans, arrays[i])
            
        return ans
            
