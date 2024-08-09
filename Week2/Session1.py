'''
https://replit.com/@kuiduanz/Unit-2?v=1
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
# Problem 1: Remove Duplicates from Sorted List
Leetcode Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list
Solution: https://guides.codepath.org/compsci/Remove-Duplicates-from-Sorted-List

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Constraints
- The number of nodes in the list is in the range `[0, 300]`.
- `-100 <= Node.val <= 100`
- The list is guaranteed to be **sorted** in ascending order.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
'''

'''
Understand:
- 1. What would be output if the input is only head? Empty? -> return None
- 2. What type of LinkedList is this? -> LinkedList
- 3. What is the data type for value in the node? -> Integers
- 4. Duplicates would mean there are multiple nodes with the same value like four nodes with value of 1

Match:
- Linked List
- 1 -> 1 -> 1 -> 2 -> 2 -> 2 -> 3 -> 4
               s
               f       

Plan:
- 1. Create 2 pointers: slow and fast. slow iterates through the LL one node at a time, fast pointer moves until the value of slow pointer is not equal
- 2. While slow or fast are not null:
    - 3. While slow == fast
        - fast = fast.next
    - slow.next = fast
    - slow = fast
- 4. return the head

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
# Your function deleteDuplicates is called as such:
# head = ListNode(1)
# head.next = ListNode(1)
# deleteDuplicates(head)
def deleteDuplicates(head: ListNode) -> ListNode:
    # slow, fast = head, head
    # while slow or fast:
    #     while fast and slow.val == fast.val:
    #         fast = fast.next # move to next node
    #     slow.next = fast
    #     slow = fast
    # return head

    res = head
    while head and head.next:
        if head.val == head.next.val:
            head.next = head.next.next
        else:
            head = head.next
    return res
print("Problem 1: Remove Duplicates from Sorted List")
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(2)
print("head = [1,1,2]:", deleteDuplicates(head))
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)
print("head = [1,1,2,3,3]:", deleteDuplicates(head))
print()


'''
# Problem 2: Linked List Cycle
Leetcode Link: https://leetcode.com/problems/linked-list-cycle
Solution: https://guides.codepath.org/compsci/Linked-List-Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

Constraints
- The number of the nodes in the list is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` or a **valid index** in the linked-list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# Your function hasCycle is called as such:
# head = ListNode(1)
# head.next = ListNode(1)
# hasCycle(head)
def hasCycle(head: ListNode) -> bool:
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
print("Problem 2: Linked List Cycle")
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next
print("head = [3,2,0,-4], pos = 1:", hasCycle(head))
head = ListNode(1)
head.next = ListNode(2)
head.next.next = head
print("head = [1,2], pos = 0:", hasCycle(head))
head = ListNode(1)
print("head = [1], pos = -1:", hasCycle(head))
print()


'''
# Problem 3: Reverse Linked List
Leetcode Link: https://leetcode.com/problems/reverse-linked-list
Solution: https://guides.codepath.org/compsci/Reverse-Linked-List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Constraints
- The number of nodes in the list is the range `[0, 5000]`.
- `-5000 <= Node.val <= 5000`

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# Your function reverseList is called as such:
# head = ListNode(1)
# head.next = ListNode(1)
# reverseList(head)
def reverseList(head: ListNode) -> ListNode:
    prev, curr = None, head
    while curr:
        curr.next, prev, curr = prev, curr, curr.next
    return prev
print("Problem 3: Reverse Linked List")
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print("head = [1,2,3,4,5]:", reverseList(head))
head = ListNode(1)
head.next = ListNode(2)
print("head = [1,2]:", reverseList(head))
head = None
print("head = []:", reverseList(head))
print()


'''
# (Bonus) Problem 4: Linked List Cycle II
Leetcode Link: https://leetcode.com/problems/linked-list-cycle-ii
Solution: https://guides.codepath.org/compsci/Linked-List-Cycle-II

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. **Note that pos is not passed as a parameter. **
Do not modify the linked list.

Constraints
- The number of the nodes in the list is in the range `[0, 10^4]`.
- `-105 <= Node.val <= 105`
- `pos` is `-1` or a **valid index** in the linked-list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# Your function detectCycle is called as such:
# head = ListNode(1)
# head.next = ListNode(1)
# detectCycle(head)
def detectCycle(head: ListNode) -> ListNode:
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            break
    if not fast or not fast.next:
        return None
    e, h = slow, head
    while e.next:
        if e == h:
            return e
        e = e.next
        h = h.next 
print("(Bonus) Problem 4: Linked List Cycle II")
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next
print("head = [3,2,0,-4], pos = 1:", detectCycle(head))
head = ListNode(1)
head.next = ListNode(2)
head.next.next = head
print("head = [1,2], pos = 0:", detectCycle(head))
head = ListNode(1)
print("head = [1], pos = -1:", detectCycle(head))
print()


'''
# (Bonus) Problem 5: Remove Linked List Elements
Leetcode Link: https://leetcode.com/problems/remove-linked-list-elements
Solution: https://guides.codepath.org/compsci/Remove-Linked-List-Elements

Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Constraints
- The number of nodes in the list is in the range `[0, 10^4]`.====
- `1 <= Node.val <= 50`
- `0 <= val <= 50`

Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2: 
Input: head = [], val = 1
Output: []

Example 3:
Input: head = [7,7,7,7], val = 7
Output: []
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# Your function removeElements is called as such:
# head = ListNode(1)
# head.next = ListNode(1)
# removeElements(head, 1)
def removeElements(head: ListNode, val: int) -> ListNode:
    temp = ListNode(0)
    temp.next = head
    curr = temp
    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return temp.next
print("(Bonus) Problem 5: Remove Linked List Elements")
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(6)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(6)
print("head = [1,2,6,3,4,5,6], val = 6:", removeElements(head, 6))
head = None
print("head = [], val = 1:", removeElements(head, 1))
head = ListNode(7)
head.next = ListNode(7)
head.next.next = ListNode(7)
head.next.next.next = ListNode(7)
print("head = [7,7,7,7], val = 7:", removeElements(head, 7))
print()