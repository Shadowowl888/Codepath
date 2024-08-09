from typing import List

'''
# Warmup Problem: Reverse String
Leetcode Link: https://leetcode.com/problems/reverse-string
Solution: https://github.com/codepath/compsci_guides/wiki/Reverse-a-String/

Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
'''
def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    left, right = 0, len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left, right = left+1, right-1
    return s
print("Warmup Problem: Reverse String")
print('s = ["h","e","l","l","o"]:', reverseString(["h","e","l","l","o"]))
print('s = ["H","a","n","n","a","h"]:', reverseString(["H","a","n","n","a","h"]))
print()