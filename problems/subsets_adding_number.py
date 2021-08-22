"""

"""

from typing import List

"""
Subsets adding to number

Not a LeetCode problem exactly. Done using Dynamic Programming Principles. 

"""

def SAN(nums: List[int], target: int):

    """
    [], 2 --> [[2]]
    [2], 3 --> [[2,3], [2], [3]]
    [2,3],9 --> [[2,3,9], []]
    [2,3,9], 6 --> [[2,3], [2,9], [3,9]]
    [2,3,9,6], 7 --> [v[2,3,6], x[2,6,9], x[3,6,9], ...]
    
    """
    
    if not nums:
        return []
    if len(nums) == 1:
        return [nums[0]] if target == nums[0] else []

    ans = []
    perms = [set()]

    for i in range(len(nums)):
        new = nums[i]
        if new == target:
            ans.append({new})
            continue
        elif new <= target:
            tmp = []
            for perm in perms:
                new_sum = sum(perm) + new
                new_set = perm.union({new})
                if new_sum == target:
                    ans.append(new_set)
                elif new_sum < target:
                    tmp.append(new_set)
            perms.extend(tmp)
    
    return ans

if __name__ == '__main__':
  print(SAN([2,3,9,6,7,10,15],15))
