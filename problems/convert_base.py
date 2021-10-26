"""
- Given a non-negative integer n, convert n to base m (m<=9). 
- Answer in string format to emphasize the diff to base 10 integer.
- Do not use any built in base m conversion functions like bin.

- Here's an example and some starter code:

def base_m(n, m):
  # Fill this in.
print(base_m(123, 2))
# 1111011

In the above example, 2^6 + 2^5 + 2^4 + 2^3 + 2^1 + 2^0 = 123.
"""

def base_m(x: int, base: int) -> str:
    remainder = x%base
    dividend = x//base

    reversed = [str(remainder)]

    while dividend > base-1:
        reversed.append(str(dividend%base))
        dividend = dividend//base

    reversed.append(str(dividend))
    answer = reversed[::-1]
    
    return "".join(answer)

if __name__ == '__main__':
    assert int(base_m(16, 2), 2) == 16
    assert int(base_m(123, 2), 2) == 123
    assert int(base_m(1020, 4), 4) == 1020
    assert int(base_m(3238219, 7), 7) == 3238219
