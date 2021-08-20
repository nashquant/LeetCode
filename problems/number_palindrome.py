"""
Problem 9 - Palindrome Number.
Success
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
