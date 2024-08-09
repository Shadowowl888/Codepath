'''
# Warmup Problem: Power of Two
Leetcode Link: https://leetcode.com/problems/power-of-two
Solution: https://guides.codepath.org/compsci/Power-Of-Two

Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2^x.

Example 1:
Input: n = 1
Output: true
Explanation: 2^0 = 1

Example 2:
Input: n = 16
Output: true
Explanation: 2^4 = 16

Example 3:
Input: n = 3
Output: false
'''
def isPowerOfTwo(n: int) -> bool:
    if n == 1:
        return True
    if (n % 2 != 0) or n == 0:
        return False
    return isPowerOfTwo(n // 2)
print("Warmup Problem: Power of Two")
print("n = 1:", isPowerOfTwo(1))
print("n = 16:", isPowerOfTwo(16))
print("n = 3:", isPowerOfTwo(3))
print()