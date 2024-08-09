import heapq

'''
https://replit.com/@EvanHaut/Unit-4?v=1
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
# Problem 1: Kth Largest Element in an Array
Leetcode Link: https://leetcode.com/problems/kth-largest-element-in-an-array
Solution: https://guides.codepath.org/compsci/Kth-Largest-Element-in-an-Array

Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
You must solve it in O(n) time complexity.

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
'''

'''
Understand:
- is nums sorted, no
- test1 = [4, 6, 1, 7, 89, 21], k = 3
- test2 = [0, 3, 5, 1], k = 4
- What if k is larger than the length of the array?
- k cannot be negative
- can the array be empty?

Match:
- Heap - winner
- Sort array - wouldnt be O(n)
- Two pointer - would need to be sorted
- Multiple passes - for linked lists
- Sliding Window - needs to be sorted
k = 3
[1,2,3,4,5]

Plan:
1. create heap data structure
2. iterate through array and negate every element
3. add elements to heap
4. pop k times
5. return top element negated 

1. create heap data structure
2. fill heap with k elements
3. push and pop until end of array
4. pop and return that element

Implement:
'''
# Your function findKthLargest is called as such:
# nums = [5,4,3]
# findKthLargest(nums, 3)
def findKthLargest(nums: list[int], k: int) -> int:
    heap = []
    for num in nums:
        heapq.heappush(heap, num*-1)
    for i in range(k-1):
        heapq.heappop(heap)
    return heapq.heappop(heap) * -1
print("Problem 1: Kth Largest Element in an Array")
print("nums = [3,2,1,5,6,4], k = 2:", findKthLargest([3,2,1,5,6,4], 2))
print("nums = [3,2,3,1,2,4,5,5,6], k = 4:", findKthLargest([3,2,3,1,2,4,5,5,6], 4))
print()


'''
# Problem 2: Number of Students Unable to Eat Lunch
Leetcode Link: https://leetcode.com/problems/number-of-students-unable-to-eat-lunch
Solution: https://guides.codepath.org/compsci/Number-of-Students-Unable-to-Eat-Lunch

The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.
The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:
If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue. Otherwise, they will leave it and go to the queue's end. This continues until none of the queue students want to take the top sandwich and are thus unable to eat.
You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.

Example 1:
Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
Output: 0 
Explanation:
- Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
- Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
- Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
- Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
- Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
Hence all students are able to eat.

Example 2:
Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
Output: 3
'''

'''
Understand:
- Input: 
- Queue for students(j=0), [1, 0, 0, 1] <- student sandwhich pref
- sandwiches for stack(i=0) [0, 1, 1, 0] <- sandwich type
- Output:

Match:
- 

Plan:
- 

Implement:
'''
# Your function countStudents is called as such:
# students = [1,1,1,0,0,1]
# sandwiches = [1,0,0,0,1,1]
# countStudents(students, sandwiches)
def countStudents(students: list[int], sandwiches: list[int]) -> int:
    ones, zeros = 0, 0
    for student in students:
        if student == 0:
            zeros += 1
        else:
            ones += 1
    for sandwich in sandwiches:
        if sandwich == 0:
            if zeros == 0:
                return ones
            zeros -= 1
        else:
            if ones == 0:
                return zeros
            ones -= 1
    return zeros + ones
print("Problem 2: Number of Students Unable to Eat Lunch")
print("students = [1,1,0,0], sandwiches = [0,1,0,1]:", countStudents([1,1,0,0], [0,1,0,1]))
print("students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]:", countStudents([1,1,1,0,0,1], [1,0,0,0,1,1]))
print()


'''
# Problem 3: Add Two Numbers II
Leetcode Link: https://leetcode.com/problems/add-two-numbers-ii
Solution: https://guides.codepath.org/compsci/Add-Two-Numbers-II

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]

Example 2:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]

Example 3:
Input: l1 = [0], l2 = [0]
Output: [0]
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#
# Your function addTwoNumbers is called as such:
# l1 = ListNode(1)
# l2 = ListNode(2)
# addTwoNumbers(l1, l2)
def addTwoNumbers(l1: [ListNode], l2: [ListNode]) -> [ListNode]:
    pass
print("Problem 3: Add Two Numbers II")
l1 = ListNode(7)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l1.next.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
print("l1 = [7,2,4,3], l2 = [5,6,4]:", addTwoNumbers(l1, l2))
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
print("l1 = [2,4,3], l2 = [5,6,4]:", addTwoNumbers(l1, l2))
l1 = ListNode(0)
l2 = ListNode(0)
print("l1 = [0], l2 = [0]:", addTwoNumbers(l1, l2))
print()


'''
# (Bonus) Problem 4: Validate Stack Sequences
Leetcode Link: https://leetcode.com/problems/validate-stack-sequences
Solution: https://guides.codepath.org/compsci/Validate-Stack-Sequences

Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.

Example 1:
Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

Example 2:
Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.
'''
# Your function validateStackSequences is called as such:
# pushed = [5,4,3]
# popped = [3,4,5]
# validateStackSequences(nums, 3)
def validateStackSequences(pushed: list[int], popped: list[int]) -> bool:
    pass
print("(Bonus) Problem 4: Validate Stack Sequences")
print("pushed = [1,2,3,4,5], popped = [4,5,3,2,1]:", validateStackSequences([1,2,3,4,5], [4,5,3,2,1]))
print()


'''
# (Bonus) Problem 5: Evaluate Reverse Polish Notation
Leetcode Link: https://leetcode.com/problems/evaluate-reverse-polish-notation
Solution: https://guides.codepath.org/compsci/Evaluate-Reverse-Polish-Notation

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
Evaluate the expression. Return an integer that represents the value of the expression.

Note that:
- The valid operators are '+', '-', '*', and '/'.
- Each operand may be an integer or another expression.
- The division between two integers always truncates toward zero.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in a reverse polish notation.
- The answer and all the intermediate calculations can be represented in a 32-bit integer.

Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
'''
# Your function evalRPN is called as such:
# tokens = ["4","13","5","/","+"]
# evalRPN(tokens)
def evalRPN(tokens: list[str]) -> int:
    pass
print("(Bonus) Problem 5: Evaluate Reverse Polish Notation")
print('tokens = ["2","1","+","3","*"]:', evalRPN(["2","1","+","3","*"]))
print('tokens = ["4","13","5","/","+"]:', evalRPN(["4","13","5","/","+"]))
print('tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]:', evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
print()