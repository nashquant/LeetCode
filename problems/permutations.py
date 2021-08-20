"""
Problem 46 - Permutations

Sucess - Very fast execution, faster than 88% submissions

"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ## Degenerate case
        if not nums:
            return []
        
        ## Base case
        elif len(nums) == 1:
            return [nums]
        
        ## Recursive case
        else:
            ans = []
            
            for i, num in enumerate(nums):
                subnums = nums[:i] + nums[i+1:]
                for perms in self.permute(subnums):
                    ans.append([num, *perms])
                
                    
            return ans
