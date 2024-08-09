from typing import List

'''
# Warmup Problem: Majority Element
Leetcode Link: https://leetcode.com/problems/majority-element
Solution: https://guides.codepath.org/compsci/Majority-Element

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''
def majorityElement(nums: List[int]) -> int:
    # Time Complexity: O(nlog(n))
    # nums.sort()
    # n = len(nums)
    # return nums[n//2]
    
    res, count = 0, 0
    for n in nums:
        if count == 0:
            res = n
        count += (1 if n == res else -1)
    return res
print("Warmup Problem: Majority Element")
print("nums = [3,2,3]:", majorityElement([3,2,3]))
print("nums = [2,2,1,1,1,2,2]:", majorityElement([2,2,1,1,1,2,2]))
print()