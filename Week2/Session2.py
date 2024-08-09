'''
https://replit.com/join/invgdslexi-lightningowl
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
# Problem 1: Remove Nth Node from End of List
Leetcode Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list
Solution: https://guides.codepath.org/compsci/Remove-Nth-Node-from-End-of-List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Constraints
- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
'''

'''
Understand:
- Is it 0-indexed or not?
- Can n be greater than the length of the list?
- Is it singly or doubly linked list?
- What happens if we have only one node? -> output is Null
- Empty linked list? -> output is Null, n would have to be 0

Match:
- Linked List
- Modify the list (add/remove nodes) using temp head
- Two pointers (want pointers at specific positions/speeds)

Plan:
- temp node is pointed to the head to see the starting edge case, temp.next = head
- Use two pointers
- Start the faster pointer by n nodes distance from head 
- Move the slow pointer and fast pointer by 1 node at the same time until the fast.next reached to the null (end of list)
- Remove slow.next's node
- Return temp.next

Implement:
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)
#
# Your function removeNthFromEnd is called as such:
# head = ListNode(1)
# head.next = ListNode(1)
# removeNthFromEnd(head, 1)
def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    temp = ListNode(0, head)
    slow, fast = temp, temp
    for i in range(n+1):
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return temp.next
print("Problem 1: Remove Nth Node from End of List")
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print("head = [1,2,3,4,5], n = 2:", removeNthFromEnd(head, 2))
head = ListNode(1)
print("head = [1], n = 1:", removeNthFromEnd(head, 1))
head = ListNode(1)
head.next = ListNode(2)
print("head = [1,2], n = 1:", removeNthFromEnd(head, 1))
print()
'''
Evaluate:
- Time Complexity: O(n)
- Space Complexity: O(1)
'''


'''
# Problem 2: Add Two Numbers
Leetcode Link: https://leetcode.com/problems/add-two-numbers
Solution: https://guides.codepath.org/compsci/Add-Two-Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Constraints
- The number of nodes in each linked list is in the range [1, 100].
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading zeros.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''

'''
Understand:
- Each linked list can have different lengths
- What type of LL? Singly, Doubly, or Circular?
- How to deal with carries?

Match:
- Two pointers - one pointer for each linked list to iterate through
- temp head - linked list to return, we will add nodes to the temp head
- multiple pass: N/A

Plan:
- temp head pointing to nothing
- two pointers, one for each linked list p1 and p2
- while p1 or p2 is not null, add the values of p1 and p2 and store the remainder in a variable
- Add p1 and p2 values and store it to total
- If total is less than 10

Implement:
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# Your function addTwoNumbers is called as such:
# l1 = ListNode(1)
# l1.next = ListNode(1)
# l2 = ListNode(2)
# l2.next = ListNode(2)
# addTwoNumbers(l1, l2)
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    pass
print("Problem 2: Add Two Numbers")
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
l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(9)
l1.next.next.next.next = ListNode(9)
l1.next.next.next.next.next = ListNode(9)
l1.next.next.next.next.next.next = ListNode(9)
l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)
l2.next.next.next = ListNode(9)
print("l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]:", addTwoNumbers(l1, l2))
print()


'''
# Problem 3: Palindrome Linked List
Leetcode Link: https://leetcode.com/problems/palindrome-linked-lists
Solution: https://guides.codepath.org/compsci/Palindrome-Linked-Lists

Given the head of a singly linked list, return true if it is a palindrome (a sequence that reads the same forward and backward) or false otherwise.

Constraints
- The number of nodes in the list is in the range [1, 10^5].
- 0 <= Node.val <= 9

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# Your function isPalindrome is called as such:
# head = ListNode(1)
# head.next = ListNode(1)
# isPalindrome(head)
def isPalindrome(head: ListNode) -> bool:
    pass
print("Problem 3: Palindrome Linked List")
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
print("head = [1,2,2,1]:", isPalindrome(head))
head = ListNode(1)
head.next = ListNode(2)
print("head = [1,2]:", isPalindrome(head))
print()


'''
# (Bonus) Problem 4: Remove Duplicates from Sorted List II
Leetcode Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii
Solution: https://guides.codepath.org/compsci/Remove-Duplicates-from-Sorted-List-II

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Constraints
- The number of nodes in the list is in the range [0, 300].
- -100 <= Node.val <= 100
- The list is guaranteed to be sorted in ascending order.

Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# Your function deleteDuplicates is called as such:
# head = ListNode(1)
# head.next = ListNode(1)
# deleteDuplicates(head)
def deleteDuplicates(head: ListNode) -> ListNode:
    pass
print("(Bonus) Problem 4: Remove Duplicates from Sorted List II")
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(4)
head.next.next.next.next.next.next = ListNode(5)
print("head = [1,2,3,3,4,4,5]:", deleteDuplicates(head))
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(1)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(3)
print("head = [1,1,1,2,3]:", deleteDuplicates(head))
print()


'''
# (Bonus) Problem 5: Swap Nodes in Pairs
Leetcode Link: https://leetcode.com/problems/swap-nodes-in-pairs
Solution: https://guides.codepath.org/compsci/Swap-Nodes-in-Pairs

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Constraints
- The number of nodes in the list is in the range [0, 100].
- 0 <= Node.val <= 100

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# Your function swapPairs is called as such:
# head = ListNode(1)
# head.next = ListNode(1)
# swapPairs(head)
def swapPairs(head: ListNode) -> ListNode:
    temp = ListNode(0, head)
    prev = temp
    while head and head.next:
        a, b = head, head.next
        a.next = b.next
        b.next = a
        prev.next = b
        prev = a
        head = a.next
    return temp.next
print("(Bonus) Problem 5: Swap Nodes in Pairs")
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
print("head = [1,2,3,4]:", swapPairs(head))
head = None
print("head = []:", swapPairs(head))
head = ListNode(1)
print("head = [1]:", swapPairs(head))
print()