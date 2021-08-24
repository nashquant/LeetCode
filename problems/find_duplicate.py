from typing import List


def find_duplicate(arr: List[int]) -> int:
    """
    Given an array of nums containing n+1 ints where each int
    is between [1,n] (inclusive). Prove that at least one
    duplicate number must exist. Assume that there's just
    one duplicate number, but it could be repeated more
    than once. Then write a program in O(n) that finds and 
    returns this number.
    
    len(array) = n+1 items allowed {1,2,3,..., n}

    "Proof" Argument

    n = 2
    [1, 2, (1 or 2)]

    n = 3
    [1, 2, 3, (1 or 2 or 3)]

    n = n
    [1,2,3, ..., n] is a n-length array, so since
    we are bound to choose an array between [1,n]
    the n+1-th number must be repeated. CQD
    
    ATTENTION: Refer to Floyd's "Tortoise and Hare"
    If you want a faster solution.
    
    """

    if not arr or len(arr) == 1: 
        return None

    n = len(arr) - 1
    visited = set()

    for elem in arr:
        if elem in visited:
            return elem
        else:
            visited.update([elem])

if __name__ == '__main__':

    assert find_duplicate([6, 4, 3, 3 , 2, 3, 3]) == 3
