'''
https://replit.com/join/gkrtlcjznn-lightningowl
https://courses.codepath.org/courses/tip103/pages/mock_interview_guide
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
# Problem 1: Sort Colors
Leetcode Link: https://leetcode.com/problems/sort-colors
Solution: https://guides.codepath.org/compsci/Sort-Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]
'''

'''
Understand:
- Time Complexity: O(n)
- Space Complexity: O(1)
- [1] -> [1]
- [1, 1, 1, 1] -> [1, 1, 1, 1]

Match:
- Two Pointer
- Sorting

Plan:
- left will keep track of where to put next 0, mid keep track of 1, and right keep track of where to put next 2
- left = 0
- right = n-1
- mid = 0
- while mid <= right:
    - if nums[mid] is 0:
        - swap numbers at mid and left
        - temp = nums[mid]
        - nums[mid] = nums[left]
        - nums[left] = temp
        - left += 1
        mid++
    - if nums[mid] is 1:
        - mid += 1
    - if nums[mid] is 2:
        - swap numbers at mid and right
        - temp = nums[mid]
        - nums[mid] = nums[right]
        - right -= 1
- return nums
1 0 2
^ ^
l r
m

[0, 0, 1, 1, 2, 2]
        ^^     
        r
    l          
        m 

Implement:
'''
# Your function sortColors is called as such:
# nums = [2,0,2,1,1,0]
# sortColors(nums)
def sortColors(nums: list[int]) -> None:
    left, mid, right = 0, 0, len(nums)-1
    while mid <= right:
        if nums[mid] == 0:
            nums[mid], nums[left] = nums[left], nums[mid]
            left += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[right] = nums[right], nums[mid]
            right -= 1
    return nums
print("Problem 1: Sort Colors")
print("nums = [2,0,2,1,1,0]:", sortColors([2,0,2,1,1,0]))
print("nums = [2,0,1]:", sortColors([2,0,1]))
print()
'''
Evaluate:
- Time Complexity: O(n)
- Space Complexity: O(1)
'''


'''
# Problem 2: Product of Array Except Self
Leetcode Link: https://leetcode.com/problems/product-of-array-except-self
Solution: https://guides.codepath.org/compsci/Product-of-Array-Except-Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''

'''
Understand:
- What would you do with an empty array/single number array?
    - [], [1]
- What would the output be for two number array?
    - [-2, 1] -> [1, -2]
- Run time is O(N), what is the space though?
    - O(1) SPACE
    - output array doesn't count as extra space

Match:
- Two pointer: one pointer on the index and other pointer traversing the array multiplying the numbers O(n^2) too long
- Hashmap/set: Not relevent because we aren't using frequency of numbers and space is O(1)
- Sliding window: Not useful because the subarrays are too large
- Presorting: Time and space doesn't work out

Plan:
- 

Implement:
'''
# Your function productExceptSelf is called as such:
# nums = [1, 2, 3, 4]
# productExceptSelf(nums)
def productExceptSelf(nums: list[int]) -> list[int]:
    res = [0] * len(nums)
    leftProduct, rightProduct = 1, 1
    for i in range(len(nums)):
        res[i] = leftProduct
        leftProduct *= nums[i]
    for i in range(len(nums)-1, -1, -1):
        res[i] *= rightProduct
        rightProduct *= nums[i]
    return res
print("Problem 2: Product of Array Except Self")
print("nums = [1,2,3,4]:", productExceptSelf([1,2,3,4]))
print("nums = [-1,1,0,-3,3]:", productExceptSelf([-1,1,0,-3,3]))
print()
'''
Evaluate:
- Time Complexity: O(n)
- Space Complexity: O(n)
'''


'''
# Problem 3: Koko Eating Bananas
Leetcode Link: https://leetcode.com/problems/koko-eating-bananas
Solution: https://guides.codepath.org/compsci/Koko-Eating-Bananas

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23
'''
# Your function minEatingSpeed is called as such:
# piles = [3, 6, 7, 11]
# h = 8
# minEatingSpeed(piles, h)
def minEatingSpeed(piles: list[int], h: int) -> int:
    pass
print("Problem 3: Koko Eating Bananas")
print("piles = [3,6,7,11], h = 8:", minEatingSpeed([3,6,7,11], 8))
print("piles = [30,11,23,4,20], h = 5:", minEatingSpeed([30,11,23,4,20], 5))
print("piles = [30,11,23,4,20], h = 6:", minEatingSpeed([30,11,23,4,20], 6))
print()


'''
# (Bonus) Problem 4: Container With Most Water
Leetcode Link: https://leetcode.com/problems/container-with-most-water
Solution: https://guides.codepath.org/compsci/Container-With-Most-Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

Example 2:
Input: height = [1,1]
Output: 1
'''
# Your function maxArea is called as such:
# height = [1,8,6,2,5,4,8,3,7]
# maxArea(height)
def maxArea(height: list[int]) -> int:
    maxArea = 0
    left, right = 0, len(height)-1
    while left <= right:
        smallestHeight = min(height[left], height[right])
        maxArea = max(maxArea, (right - left) * smallestHeight)
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
    return maxArea
print("(Bonus) Problem 4: Container With Most Water")
print("height = [1,8,6,2,5,4,8,3,7]:", maxArea([1,8,6,2,5,4,8,3,7]))
print("height = [1,1]:", maxArea([1,1]))
print()


'''
# (Bonus) Problem 5: Merge Intervals
Leetcode Link: https://leetcode.com/problems/merge-intervals
Solution: https://guides.codepath.org/compsci/Merge-Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''
# Your function merge is called as such:
# intervals = [[1,4],[4,5]]
# merge(intervals)
def merge(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals or len(intervals) == 0:
        return intervals
    intervals.sort(key=lambda x: x[0])
    mergedIntervals = [intervals[0]]
    for curr in intervals:
        if not mergedIntervals or mergedIntervals[-1][1] < curr[0]:
            mergedIntervals.append(curr)
        else:
            mergedIntervals[-1][1] = max(mergedIntervals[-1][1], curr[1])
    return mergedIntervals
print("(Bonus) Problem 5: Merge Intervals")
print("intervals = [[1,3],[2,6],[8,10],[15,18]]:", merge([[1,3],[2,6],[8,10],[15,18]]))
print("intervals = [[1,4],[4,5]]:", merge([[1,4],[4,5]]))
print()