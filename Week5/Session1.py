'''
https://replit.com/@KuiduanZeng/Python?v=1
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
# Problem 1: Valid Palindrome II
Leetcode Link: https://leetcode.com/problems/valid-palindrome-ii
Solution: https://guides.codepath.org/compsci/Valid-Palindrome-II

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1: 
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true

Example 3:
Input: s = "abc"
Output: false
'''

'''
Understand:
- 

Match:
- 

Plan:
- isPalindrome(s: str, left: int, right: int, skips: int) -> bool:
    - Base case: when pointer one pass the pointer two -> return True
    - skips > 1 -> return False
    - if str[left] == str[right]:
        - return isPalindrome(s, left + 1, right - 1, skips)
    - else:
        - if str[left] != str[right] && skips < 1 -> return false
        - else:
            - return isPalindrome(s, left + 1, right, skips + 1) and isPalindrome(s, left, right-1, skips + 1)

isPalindrome function:
def isPalindrome(s: str) -> bool:
    start, end = 0, len(s)-1
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1 
    return True

Implement:
'''
# Your function isPalindrome is called as such:
# s = "people"
# isPalindrome(s)
def isPalindrome(s: str) -> bool:
    # left, right = 0, len(s)-1
    # def isPalindrome(s: str, left: int, right: int, skips: int) -> bool:
    #     if left > right:
    #         return True
    #     if skips < 0:
    #         return False
    #     if s[left] == s[right]:
    #         return isPalindrome(s, left + 1, right - 1, skips)
    #     else:
    #         if s[left] != s[right] and skips < 1:
    #             return False
    #         else:
    #             return isPalindrome(s, left + 1, right, skips - 1) or isPalindrome(s, left, right-1, skips - 1)

    def isPalindrome(left, right, skips):
        if skips > 1:
            return False
        while left <= right:
            if s[left] != s[right]:
                return isPalindrome(left+1, right, skips+1) or isPalindrome(left, right-1, skips+1)
            left += 1
            right -= 1
        return True
    return isPalindrome(0, len(s)-1, 0)
print("Problem 1: Valid Palindrome II")
print('s = "aba":', isPalindrome("aba"))
print('s = "abca":', isPalindrome("abca"))
print('s = "abc":', isPalindrome("abc"))
print()
'''
Evaluate:
- Time Complexity: O(n)
- Space Complexity: O(n)
'''


'''
# Problem 2: Shortest Distance to a Character
Leetcode Link: https://leetcode.com/problems/shortest-distance-to-a-character
Solution: https://guides.codepath.org/compsci/Shortest-Distance-To-a-Character

Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.
The distance between two indices i and j is abs(i - j), where abs is the absolute value function.

Example 1:
Input: s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]
Explanation: The character 'e' appears at indices 3, 5, 6, and 11 (0-indexed).
The closest occurrence of 'e' for index 0 is at index 3, so the distance is abs(0 - 3) = 3.
The closest occurrence of 'e' for index 1 is at index 3, so the distance is abs(1 - 3) = 2.
For index 4, there is a tie between the 'e' at index 3 and the 'e' at index 5, but the distance is still the same: abs(4 - 3) == abs(4 - 5) = 1.
The closest occurrence of 'e' for index 8 is at index 6, so the distance is abs(8 - 6) = 2.

Example 2:
Input: s = "aaab", c = "b"
Output: [3,2,1,0]
'''

'''
Understand:
- How long the c can be?
    - c is one char in s
- Can input s be empty? Can input c be empty?
- What if the input is 1 char?
    - Edge Case: s="b", c="b" -> return [0]
    - Happy Case: s="happy", c="p" -> return [2, 1, 0, 0, 1]

Match:
- Two Pointer: Go through each character, starting from current character index, and expand the two pointers outward until it find a matching character.
- Sliding Window: recursive call 
- Hashmap: characters map to the index and compute the distance between each character in the string

Plan:
- Create pointers, set to 0
- Create answer array
- Outer for loop, runs till length(s):
- set pointers to current indices
    - while True:
        - if left pointer >= length(s) and left pointer == c:
            append (abs(current char - left pointer)) to answer[]
        - elif right pointer < length(s) and right pointer == c:
            append (abs(current char - right pointer)) to answer[]
        - update pointers
- return answer

Implement:
'''
# Your function shortestToChar is called as such:
# s = "people"
# c = "e"
# shortestToChar(s,c)
def shortestToChar(s: str, c: str) -> [int]:
    left = right = 0
    answer = []
    for char in range(len(s)):
        right = left = char
        while True:
            if left >= 0 and s[left] == c:
                answer.append(abs(char-left))
                break
            elif right < len(s) and s[right] == c:
                answer.append(abs(char-right))
                break
            left -= 1
            right += 1
    return answer
print("Problem 2: Shortest Distance to a Character")
print('s = "loveleetcode", c = "e":', shortestToChar("loveleetcode", "e"))
print('s = "aaab", c = "b":', shortestToChar("aaab", "b"))
print()


'''
# Problem 3: Crawler Log Folder
Leetcode Link: https://leetcode.com/problems/crawler-log-folder
Solution: https://guides.codepath.org/compsci/Crawler-Log-Folder

The Leetcode file system keeps a log each time some user performs a change folder operation.
The operations are described below:
"../" : Move to the parent folder of the current folder. (If you are already in the main folder, remain in the same folder).
"./" : Remain in the same folder.
"x/" : Move to the child folder named x (This folder is guaranteed to always exist).
You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.
The file system starts in the main folder, then the operations in logs are performed.
Return the minimum number of operations needed to go back to the main folder after the change folder operations.

Example 1:
Input: logs = ["d1/","d2/","../","d21/","./"]
Output: 2

Example 2:
Input: logs = ["d1/","d2/","./","d3/","../","d31/"]
Output: 3

Example 3:
Input: logs = ["d1/","../","../","../"]
Output: 0
'''
# Your function minOperations is called as such:
# logs = ["d1/","d2/","../","d21/","./"]
# minOperations(logs)
def minOperations(logs: [str]) -> int:
    pass
print("Problem 3: Crawler Log Folder")
print('logs = ["d1/","d2/","../","d21/","./"]:', minOperations(["d1/","d2/","../","d21/","./"]))
print('logs = ["d1/","d2/","./","d3/","../","d31/"]:', minOperations(["d1/","d2/","./","d3/","../","d31/"]))
print('logs = ["d1/","../","../","../"]:', minOperations(["d1/","../","../","../"]))
print()


'''
# (Bonus) Problem 4: Pow(x, n)
Leetcode Link: https://leetcode.com/problems/powx-n
Solution: https://guides.codepath.org/compsci/Pow(x,n)

Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
'''
# Your function myPow is called as such:
# x = 12.3
# n = 3
# myPow(x,n)
def myPow(x: float, n: int) -> float:
    if n == 0:
        return 1
    if n < 0:
        x **= -1
        n *= -1
    if n % 2 == 1:
        return x * myPow(x, n-1)
    else:
        num = myPow(x, n // 2)
        return num * num
print("(Bonus) Problem 4: Pow(x, n)")
print("x = 2.00000, n = 10:", myPow(2.00000, 10))
print("x = 2.10000, n = 3:", myPow(2.10000, 3))
print("x = 2.00000, n = -2:", myPow(2.00000, -2))
print()


'''
# (Bonus) Problem 5: Power of Four
Leetcode Link: https://leetcode.com/problems/power-of-four
Solution: https://guides.codepath.org/compsci/Power-of-Four

Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4^x.

Example 1:
Input: n = 16
Output: true

Example 2:
Input: n = 5
Output: false

Example 3:
Input: n = 1
Output: true
'''
# Your function isPowerOfFour is called as such:
# n = 4
# isPowerOfFour(n)
def isPowerOfFour(n: int) -> bool:
    if n == 1:
        return True
    if (n % 4 != 0) or (n == 0):
        return False
    return isPowerOfFour(n // 4)
print("(Bonus) Problem 5: Power of Four")
print("n = 16:", isPowerOfFour(16))
print("n = 5:", isPowerOfFour(5))
print("n = 1:", isPowerOfFour(1))
print()