def num_divisors(n: int) -> int:

    """

    O(sqrtN)
    
    Check: 
    
    Factorization: (a^m) * (b^n) * ... * (z ^ k)
    Therefore: Num_of_divisors = (m+1) * (n+1) * ... * (k+1)
    
    """
    divisors, i = set(), 1
    
    while (i+1)*(i+1) <=n:
        if not n%i: 
            divisors.update([i, n//i])
        i+=1

    return len(divisors)

if __name__ == '__main__':
    assert num_divisors(100) == 8
    assert num_divisors(450) == 18  ### (2) * (3^2) * (5^2) -> divisors = 2 * 3 * 3 = 18
