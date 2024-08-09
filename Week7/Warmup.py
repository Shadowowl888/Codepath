from typing import Optional, List

'''
# Warmup Problem: Binary Tree Level Order Traversal
Leetcode Link: https://leetcode.com/problems/binary-tree-level-order-traversal
Solution: https://guides.codepath.org/compsci/Binary-Tree-Level-Order-Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    results = []
    queue = [root]
    while queue:
        level_size = len(queue)
        current_level = []
        for i in range(level_size):
            node = queue.pop(0)
            if node:
                current_level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        if current_level:
            results.append(current_level)
    return results
print("Warmup Problem: Binary Tree Level Order Traversal")
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print("root = [3,9,20,null,null,15,7]:", levelOrder(root))
root = TreeNode(1)
print("root = [1]:", levelOrder(root))
root = None
print("root = []:", levelOrder(root))
print()