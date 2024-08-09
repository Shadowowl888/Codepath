from typing import List

'''
https://replit.com/@EthanNgo13/Unit3?v=1
-------------------------------------------------------------------------------
Understand
- Ask clarifying questions and use examples to understand what the interviewer wants out of this problem
- Choose a “happy path” test input, different than the one provided, and a few edge case inputs. Verify that you and the interviewer are aligned on the expected inputs and outputs.

Match
- See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

Plan
- Sketch visualizations and write pseudocode
- Walk through a high level implementation with an existing diagram

Implement
- Implement the solution (make sure to know what level of detail the interviewer wants)

Review
- Re-check that your algorithm solves the problem by running through important examples
- Go through it as if you are debugging it, assuming there is a bug

Evaluate
- Finish by giving space and run-time complexity
- Discuss any pros and cons of the solution
-------------------------------------------------------------------------------
'''


'''
# Problem 1: Binary Search
Leetcode Link: https://leetcode.com/problems/binary-search
Solution: https://guides.codepath.org/compsci/Binary-Search-Problem

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''

'''
Understand:
- Input array is sorted
- If we cant find the number, return -1
- If we do find the number, return the index
- Must run in O(logn) time
- Can the input array be empty?
- If there's one number, should we just return the index

Match:
- Hashset: frequencies do not seem required
- Two pointer: Two pointers need to go at different paces to search
- Presorting: Input array is already sorted
- Sliding window: Our pointers don't move at fixed paces

Plan:
1. Create left pointer at 0, right pointer at len - 1
2. while left pointer <= right pointer
    - middle = r + l // 2
    - m = l + (r - l) // 2: 
            - https://stackoverflow.com/a/25113557/12461363ww
        - https://medium.com/swlh/overflow-bug-in-binary-search-c4d4a824807a
    - If the target is < then the middle
      - Set right pointer to middle - 1
    - The target is > to the middle
      - Set left pointer to middle + 1
    - else Target is = to the middle
      - return the index
3. return -1

Implement:
'''
# Your function search is called as such:
# arr = [1,2,3,4,5,6,7,8,9]
# search(arr, 5)
def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)-1
    while left <= right:
        middle = left + (right - left)//2
        if target < nums[middle]:
            right = middle - 1
        elif target > nums[middle]:
            left = middle + 1
        else:
            return middle
    return -1
print("Problem 1: Binary Search")
print("nums = [-1,0,3,5,9,12], target = 9:", search([-1,0,3,5,9,12], 9))
print("[-1,0,3,5,9,12], target = 2:", search([-1,0,3,5,9,12], 2))
print()


'''
# Problem 2: First Bad Version
Leetcode Link: https://leetcode.com/problems/first-bad-version
Solution: https://guides.codepath.org/compsci/First-Bad-Version

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example 1:
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:
Input: n = 1, bad = 1
Output: 1
'''

'''
Understand:
- 

Match:
- 

Plan:
- 

Implement:
'''
# Your function firstBadVersion is called as such:
# firstBadVersion(9)
def firstBadVersion(n: int) -> int:
    pass
print("Problem 2: First Bad Version")
print("n = 5, bad = 4:", firstBadVersion(5))
print("n = 1, bad = 1:", firstBadVersion(1))
print()


'''
# Problem 3: Sqrt(x)
Leetcode Link: https://leetcode.com/problems/sqrtx
Solution: https://guides.codepath.org/compsci/Sqrt(x)

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use Math.pow(x, 0.5) in Java or x ** 0.5 in python.

Example 1:
Input: 
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
'''
# Your function mySqrt is called as such:
# mySqrt(8)
def mySqrt(x: int) -> int:
    pass
print("Problem 3: Sqrt(x)")
print("x = 4:", mySqrt(4))
print("x = 8:", mySqrt(8))
print()


'''
# (Bonus) Problem 4: Find Minimum in Rotated Sorted Array
Leetcode Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
Solution: https://guides.codepath.org/compsci/Find-Minimum-in-Rotated-Sorted-Array

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
[4,5,6,7,0,1,2] if it was rotated 4 times. [0,1,2,4,5,6,7] if it was rotated 7 times. Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.
'''
# Your function findMin is called as such:
# nums = [4,5,6,7,0,1,2,3]
# findMin(nums)
def findMin(nums: List[int]) -> int:
    left, right = 0, len(nums)-1
    while left < right:
        mid = left + (right-left) // 2
        if nums[mid] < nums[right]:
            right = mid
        else:
            left = mid + 1
    return nums[right]
print("(Bonus) Problem 4: Find Minimum in Rotated Sorted Array")
print("nums = [3,4,5,1,2]:", findMin([3,4,5,1,2]))
print("nums = [4,5,6,7,0,1,2]:", findMin([4,5,6,7,0,1,2]))
print("nums = [11,13,15,17]:", findMin([11,13,15,17]))
print()


'''
# (Bonus) Problem 5: Search in Rotated Sorted Array
Leetcode Link: https://leetcode.com/problems/search-in-rotated-sorted-array
Solution: https://guides.codepath.org/compsci/Search-in-Rotated-Sorted-Array

There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1
'''
# Your function search is called as such:
# nums = [4,5,6,7,0,1,2,3]
# search(nums, 4)
def search(nums: List[int], target: int) -> int:
    pass
print("(Bonus) Problem 5: Search in Rotated Sorted Array")
print("nums = [4,5,6,7,0,1,2], target = 0:", search([4,5,6,7,0,1,2], 0))
print("nums = [4,5,6,7,0,1,2], target = 3:", search([4,5,6,7,0,1,2], 3))
print("nums = [1], target = 0:", search([1], 0))
print()