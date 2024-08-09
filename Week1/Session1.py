from typing import List

'''
https://padlet.com/allisonjchan/tip102-2-2024-contract-goals-ti3h5pf0okrngfsy
https://collabedit.com/n4te9
https://replit.com/@skyepersona1/Pod-30
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
# Problem 1: Contains Duplicates
Leetcode Link: https://leetcode.com/problems/contains-duplicate/
Solution: https://guides.codepath.org/compsci/Contains-Duplicates

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

'''
Understand:
- Can the array be empty? -> false
- What's the input type and output type? -> input: array, output: boolean

Match:        
- Hash set -> key: element of the array, value: frequency of the element
    - Time Complexity: O(n), Space Complexity: O(n)
- Use two for loops to check for each element and use the second for loop to check any duplicates
    - Time Complexity: O(n**2), Space Complexity: O(1)

Plan:
- Brute Force
    - First for loop to go through every integer in the input array
    - Second for loop to check if there a duplicate in the other element, if the duplicate is found, return. true
    - exit for loop, return false
- Hash Map
    - Initialize set()
    - For each element we check to see if it's in the set.
    - If it's not in the set, then add the current element to the set
    - If it's in the set -> return true
    - If there are no duplicates-> return false

Implement:
'''
def containsDuplicate(nums: List[int]) -> bool:
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False
print("Problem 1: Contains Duplicates")
print("nums = [1,2,3,1]:", containsDuplicate([1,2,3,1]))
print("nums = [1,2,3,4]:", containsDuplicate([1,2,3,4]))
print("nums = [1,1,1,3,3,4,3,2,4,2]:", containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
print()


'''
# Problem 2: Two Sum
Leetcode Link: https://leetcode.com/problems/two-sum
Solution: https://guides.codepath.org/compsci/Two-Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
'''

'''
Understand:
1. Does the array include negative numbers?  -> yes
2. Would there be empty arrays? ->
3. Does the order of the indicies matter? -> no
4. Can we use the same number twice that is on the same position or different position? -> no, you must use different positions

Match:
- Hashmap -> we can keep track of each element's indices
  - Time Complexity: O(n), Space complexity: O(n)
- Array -> Nested for loops checking every element with every other element for the target sum
  - Time complexity: O(n^2), Space complexity: O(1)
- Sort + 2 pointer -> use two pointers on each end to check the sum. if the sum is larger than target, move the right pointer to the left. else, move the left pointer to the right.
  - Time complexity: O(nlogn), Space complexity: O(n)
  - https://stackoverflow.com/questions/48759175/what-is-the-space-complexity-of-the-python-sort

Plan:
- Initialize the hashmap
- Iterate through the array
  - complementary = target - nums[i]
  - if complementary is not in the hashmap -> key: current element, value: current element's index
  - if it's in the hashmap -> return [complementary's index, current number's index]

Implement:
'''
def twoSum(nums: List[int], target: int) -> List[int]:
    result = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in result:
            return [result[diff], i]
        result[n] = i
print("Problem 2: Two Sum")
print("nums = [2,7,11,15] & target = 9:", twoSum([2,7,11,15], 9))
print("nums = [3,2,4] & target = 6:", twoSum([3,2,4], 6))
print("nums = [3,3] & target = 6:", twoSum([3,3], 6))
print()


'''
# Problem 3: Longest Consecutive Sequence
Leetcode Link: https://leetcode.com/problems/longest-consecutive-sequence/
Solution: https://guides.codepath.org/compsci/Longest-Consecutive-Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
'''
def longestConsecutive(nums: List[int]) -> int:
    longestStreak = 0
    numSet = set(nums)
    for num in numSet:
        if num - 1 not in numSet:
            currentNum = num
            currentStreak = 1
            while currentNum + 1 in numSet:
                currentNum += 1
                currentStreak += 1
            longestStreak = max(longestStreak, currentStreak)
    return longestStreak
print("Problem 3: Longest Consecutive Sequence")
print("nums = [100,4,200,1,3,2]:", longestConsecutive([100,4,200,1,3,2]))
print("nums = [0,3,7,2,5,8,4,6,0,1]:", longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print()


'''
# (Bonus) Problem 4: Roman to Integer
Leetcode Link: https://leetcode.com/problems/roman-to-integer/
Solution: https://guides.codepath.org/compsci/Roman-to-Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
- I can be placed before V (5) and X (10) to make 4 and 9.
- X can be placed before L (50) and C (100) to make 40 and 90.
- C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''
def romanToInt(s: str) -> int:
    map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    res = 0
    for i in range(len(s)):
        if i < len(s)-1 and map[s[i]] < map[s[i+1]]:
            res -= map[s[i]]
        else:
            res += map[s[i]]
    return res
print("(Bonus) Problem 4: Roman to Integer")
print("s = III:", romanToInt("III"))
print("s = LVIII:", romanToInt("LVIII"))
print("s = MCMXCIV:", romanToInt("MCMXCIV"))
print()


'''
# (Bonus) Problem 5: Destination City
Leetcode Link: https://leetcode.com/problems/destination-city/
Solution: https://guides.codepath.org/compsci/Destination-City

You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.
It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

Example 1:
Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

Example 2:
Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A".

Example 3:
Input: paths = [["A","Z"]]
Output: "Z"
'''
def destCity(paths: List[List[str]]) -> str:
    # start, end = set(), set()
    # for startCity, endCity in paths:
    #     start.add(startCity)
    #     end.add(endCity)
    # for endCity in end:
    #     if endCity not in start:
    #         return endCity
    
    src = set(path[0] for path in paths)
    dest = set(path[1] for path in paths)
    res = dest - src
    return res.pop()
print("(Bonus) Problem 5: Destination City")
print('paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]:', destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
print('paths = [["B","C"],["D","B"],["C","A"]]:', destCity([["B","C"],["D","B"],["C","A"]]))
print('paths = [["A","Z"]]', destCity([["A","Z"]]))
print()