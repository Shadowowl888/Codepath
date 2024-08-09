from typing import Optional

'''
# Warmup Problem: Same Tree
Leetcode Link: https://leetcode.com/problems/same-tree/
Solution: https://leetcode.com/problems/same-tree/

Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if (not p or not q) or (p.val != q.val):
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
print("Warmup Problem: Same Tree")
p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))
print("p = [1,2,3], q = [1,2,3]:", isSameTree(p, q))
p = TreeNode(1, TreeNode(2))
q = TreeNode(1, None, TreeNode(3))
print("p = [1,2], q = [1,null,2]:", isSameTree(p, q))
p = TreeNode(1, TreeNode(2), TreeNode(1))
q = TreeNode(1, TreeNode(1), TreeNode(2))
print("p = [1,2,1], q = [1,1,2]:", isSameTree(p, q))
print()