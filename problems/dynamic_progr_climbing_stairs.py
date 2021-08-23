"""
Problem 70 (Modified) - Climbing Stairs (Dynamic Programming)
Success - Modified the problem to climb maximum "m" stairs at once.

Dynamic Programming involves the creation of a data structure to 
cache (memoization) previous calculations, thus avoiding repetitive 
calculations.  

"""

def climb_stairs(n: int, m: int) -> int:

    """
    m>1, n>1, m<=n
    
    m<=n is not necessary, but solving for m<=n is equivalent to solve
    to any m>1 and n>1, because it doesn't matter if you can advance
    more stairs than the total.
    
    n = 3 and m = 3
    
    ways(3) = ways(2) + ways(1) + ways(0)
    
    to get to 3, we can advance from 2, or from 1, or from 0...
    
          _  3
        _|   2
      _|     1
    _|       0
    ways(n) = ways(n-1) + ways(n-2) + ways(n-3) + .. + ways(n-m)
    
    """
    
    if m < 1: return 0
    if n < 1: return 0

    m = min(m, n)

    if m == 1: return 1

    L = [0] * n
    L[0] = 1
    L[1] = 2

    for i in range(2, n):
        for j in range(m):
            L[i]+=L[i-1-j]
            
    return L[n-1]

if __name__ == '__main__':

    print(climb_stairs(8, 3))
