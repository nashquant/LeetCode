
"""

Given a non-negative integer n, convert n to base m (m<=9) in string form. Do not use any built in base m conversion functions like bin.

Here's an example and some starter code:

def base_m(n, m):
  # Fill this in.

print(base_m(123, 2))
# 1111011

In the above example, 2^6 + 2^5 + 2^4 + 2^3 + 2^1 + 2^0 = 123.

"""

def base_m(x: int, base: int) -> str:
    remainder = x%base
    divisor = x//base

    number = [str(remainder)]

    while divisor > base-1:
        number.append(str(divisor%base))
        divisor = divisor//base

    number.append(str(divisor))
    strnumber = "".join(number[::-1])
    return strnumber


def check_base(x: int, base: int) -> bool:
    return x == int(base_m(x, base), base)

if __name__ == '__main__':
    assert check_base(16, 2)
    assert check_base(1023, 2)
    assert check_base(12381, 5)
