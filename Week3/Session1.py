from typing import List

'''
https://replit.com/@HannahSim1/Unit-3-Arrays?v=1
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
# Problem 1: Valid Palindrome
Leetcode Link: https://leetcode.com/problems/valid-palindrome
Solution: https://guides.codepath.org/compsci/Valid-Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
'''

'''
Understand:
- Use isalnum() to 

Match:
- 
    
Plan:
- lower()
- first -> beginning, last -> end
- while first pointer < end pointer:
    * make first<second first in while cond
    while not first pointer isalnum() and first < second:
        move firsst pointer
    while not second pointer isalnum() and first < second:
        move second pointer

    if string[first] != string[second]:
        return False

    move first pointer to right by one 
    move second pointer to left by one
- return True

Implement:
'''
# Your function isPalindrome is called as such:
# s = "people"
# isPalindrome(s)
def isPalindrome(s: str) -> bool:
    # s = s.lower()
    # start, end = 0, len(s)-1
    # while start < end:
    #     while start < end and not s[start].isalnum():
    #         start += 1
    #     while start < end and not s[end].isalnum():
    #         end -= 1
    #     if s[start] != s[end]:
    #         return False
    #     start += 1
    #     end -=1 
    # return True

    left, right = 0, len(s)-1
    while left < right:
        if not alphaNum(s[left]):
            left += 1
        elif not alphaNum(s[right]):
            right -= 1
        elif s[left].lower() == s[right].lower():
            left, right = left + 1, right - 1
        else:
            return False
    return True
def alphaNum(char):
    return (ord('A') <= ord(char) <= ord('Z') or
            ord('a') <= ord(char) <= ord('z') or
            ord('0') <= ord(char) <= ord('9'))
print("Problem 1: Valid Palindrome")
print('isPalindrome("A man, a plan, a canal: Panama"):', isPalindrome("A man, a plan, a canal: Panama"))
print('isPalindrome("race a car"):', isPalindrome("race a car"))
print('isPalindrome(" "):', isPalindrome(" "))
print()


'''
# Problem 2: Unique Number of Occurrences
Leetcode Link: https://leetcode.com/problems/unique-number-of-occurences
Solution: https://guides.codepath.org/compsci/Unique-Number-of-Occurrences

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. 
No two values have the same number of occurrences.

Example 2:
Input: arr = [1,2]
Output: false

Example 3:
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
'''

'''
Understand:
- empty array input? ->
- What if there are negative numbers? -> yes
- Are there invalid value in the array?

Match:
- HashMap -> key: actual number, value: frequency
- array.count to count the occurence of numebr
- Presort the array

Plan:
- 1, 2,3,4,5
- 3, 2, 1  -> 3, 2, 1 set.length  ==  values.length

Implement:
'''
# Your function uniqueOccurrences is called as such:
# arr = [1,2,3,4]
# uniqueOccurrences(arr)
def uniqueOccurrences(arr: List[int]) -> bool:
    pass
print("Problem 2: Unique Number of Occurrences")
print("arr = [1,2,2,1,1,3]:", uniqueOccurrences([1,2,2,1,1,3]))
print("arr = [1,2]:", uniqueOccurrences([1,2]))
print("arr = [-3,0,1,-3,1,1,1,-3,10,0]:", uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))
print()


'''
# Problem 3: Merge Sorted Array
Leetcode Link: https://leetcode.com/problems/merge-sorted-array
Solution: https://guides.codepath.org/compsci/Merge-Sorted-Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:
Input: nums1 = [1], m = 1, nums2 = [ ], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [ ].
The result of the merge is [1].

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
'''
# Your function merge is called as such:
# nums1 = [1,2,3,0,0,0]
# nums2 = [1,2,3]
# merge(nums1, 3, nums2, 3)
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    pass
print("Problem 3: Merge Sorted Array")
print("nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3:", merge([1,2,3,0,0,0], 3, [2,5,6], 3))
print("nums1 = [1], m = 1, nums2 = [ ], n = 0:", merge([1], 1, [], 0))
print("nums1 = [0], m = 0, nums2 = [1], n = 1:", merge([0], 0, [1], 1))
print()


'''
# (Bonus) Problem 4: Is Subsequence
Leetcode Link: https://leetcode.com/problems/is-subsequence
Solution: https://guides.codepath.org/compsci/Is-Subsequence

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
'''
# Your function isSubsequence is called as such:
# s = "People"
# t = "Peeps"
# isSubsequence(s, t)
def isSubsequence(s: str, t: str) -> bool:
    pass
print("(Bonus) Problem 4: Is Subsequence")
print('s = "abc", t = "ahbgdc":', isSubsequence("abc", "ahbgdc"))
print('s = "axc", t = "ahbgdc":', isSubsequence("axc", "ahbgdc"))
print()


'''
# (Bonus) Problem 5: Reverse Words in a String
Leetcode Link: https://leetcode.com/problems/reverse-words-in-a-string
Solution: https://guides.codepath.org/compsci/Reverse-Words-in-a-String

Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
'''
# Your function reverseWords is called as such:
# s = "a big world"
# reverseWords(s)
def reverseWords(s: str) -> str:
    s = s.strip().split()
    reversedWords = s[::-1]
    return " ".join(reversedWords)
print("(Bonus) Problem 5: Reverse Words in a String")
print('s = "the sky is blue":', reverseWords("the sky is blue"))
print('s = "  hello world  ":', reverseWords("  hello world  "))
print('s = "a good   example":', reverseWords("a good   example"))
print()