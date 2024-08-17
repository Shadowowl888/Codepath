from typing import Optional

'''
# Warmup Problem: Kth Smallest Element in a BST
Leetcode Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst
Solution: https://guides.codepath.org/compsci/Kth-Smallest-Element-in-a-BST

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    result = []
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        result.append(node.val)
        inorder(node.right)
    inorder(root)
    return result[k-1]
print("Warmup Problem: Kth Smallest Element in a BST")
root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
print("root = [3,1,4,null,2], k = 1:", kthSmallest(root, 1))
root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
print("root = [5,3,6,2,4,null,null,1], k = 3:", kthSmallest(root, 3))
print()