from typing import Optional

'''
# Warmup Problem: Merge Two Sorted Lists
Leetcode Link: https://leetcode.com/problems/merge-two-sorted-lists
Solution: https://guides.codepath.org/compsci/Merge-Two-Sorted-Lists

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
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
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    res = ListNode()
    currentNode = res
    while list1 and list2:
        if list1.val < list2.val:
            currentNode.next = list1
            list1 = list1.next
        else:
            currentNode.next = list2
            list2 = list2.next
        currentNode = currentNode.next
    if list1:
        currentNode.next = list1
    if list2:
        currentNode.next = list2
    return res.next
print("Warmup Problem: Merge Two Sorted Lists")
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
print("list1 = [1,2,4], list2 = [1,3,4]:", mergeTwoLists(l1,l2))
l1 = None
l2 = None
print("list1 = [], list2 = []:", mergeTwoLists(l1,l2))
l1 = None
l2 = ListNode(0)
print("list1 = [], list2 = [0]:", mergeTwoLists(l1,l2))
print()