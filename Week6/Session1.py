from collections import deque

'''
https://replit.com/join/vokkzfnzmz-hannahsim1
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
# Problem 1: Invert Binary Tree
Leetcode Link: https://leetcode.com/problems/invert-binary-tree
Solution: https://guides.codepath.org/compsci/Invert-Binary-Tree

Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []
'''

'''
Understand:
- Input is binary tree
- Output inverted binary tree
- Is the tree balanced?
- Empty tree? Return empty tree

Match:
- Preorder - Try
- Inorder - No
- Postorder - 
- Bst - Not searching for anything
- Hashmap - No need to store nodes
    1
  3   2
     5  4

Plan:
- Handle empty tree
- Swap the left right nodes
- Traverse left right nodes
- Return tree

Implement:
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def treetoArray(self, root):
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        while result and result[-1] is None:
            result.pop()
        return result
#         
# Your function invertTree is called as such:
# root = TreeNode()
# invertTree(root)
def invertTree(root: TreeNode) ->TreeNode:
    if not root:
        return None
    root.left, root.right = root.right, root.left
    invertTree(root.left)      
    invertTree(root.right)
    return root
print("Problem 1: Invert Binary Tree")
root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
print("root = [4,2,7,1,3,6,9]:", root.treetoArray(invertTree(root)))
root = TreeNode(2, TreeNode(1), TreeNode(3))
print("root = [2,1,3]:", root.treetoArray(invertTree(root)))
root = TreeNode(None)
print("root = []:", root.treetoArray(invertTree(root)))
print()
'''
Evaluate:
- Time Complexity: O(n)
- Space Complexity: O(n)
'''


'''
# Problem 2: Maximum Depth of a Binary Tree
Leetcode Link: https://leetcode.com/problems/maximum-depth-of-binary-tree
Solution: https://guides.codepath.org/compsci/Maximum-Depth-of-Binary-Tree

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
'''

'''
Understand:
- Find height of tree
- Input = tree
- Output = longest height + root
- Empty, return empty

Match:
- Preorder - Try
- Inorder - No 
- Postorder - Try
- Bst - Not searching for anything
- Hashmap - No need to store nodes

Plan:
- Preorder:
    - check if root is None
*
  *
    *
      *

Implement:
'''
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         
# Your function maxDepth is called as such:
# root = TreeNode()
# maxDepth(root)
def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
print("Problem 2: Maximum Depth of a Binary Tree")
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print("root = [3,9,20,null,null,15,7]:", maxDepth(root))
root = TreeNode(1, None, TreeNode(2))
print("root = [1,null,2]:", maxDepth(root))
print()
'''
Evaluate:
- Time Complexity: O(n)
- Space Complexity: O(n)
'''


'''
# Problem 3: Minimum Depth of a Binary Tree
Leetcode Link: https://leetcode.com/problems/minimum-depth-of-binary-tree
Solution: https://guides.codepath.org/compsci/Minimum-Depth-of-Binary-Tree

Given the root of a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
'''
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         
# Your function minDepth is called as such:
# root = TreeNode()
# minDepth(root)
def minDepth(root: TreeNode) -> int:
    pass
print("Problem 3: Minimum Depth of a Binary Tree")
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print("root = [3,9,20,null,null,15,7]:", minDepth(root))
root = TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6)))))
print("root = [2,null,3,null,4,null,5,null,6]:", minDepth(root))
print()


'''
# (Bonus) Problem 4: Binary Tree Inorder Traversal
Leetcode Link: https://leetcode.com/problems/binary-tree-inorder-traversal
Solution: https://guides.codepath.org/compsci/Binary-Tree-Inorder-Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = [ ]
Output: [ ]

Example 3:
Input: root = [1]
Output: [1]
'''
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         
# Your function inorderTraversal is called as such:
# root = TreeNode()
# inorderTraversal(root)
def inorderTraversal(root: TreeNode) -> list[int]:
    results = []
    def helper(node):
        if not node:
            return
        helper(node.left)
        results.append(node.val)
        helper(node.right)
        return results
    return helper(root)
print("(Bonus) Problem 4: Binary Tree Inorder Traversal")
root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print("root = [1,null,2,3]:", inorderTraversal(root))
root = TreeNode(None)
print("root = [ ]:", inorderTraversal(root))
root = TreeNode(1)
print("root = [1]:", inorderTraversal(root))
print()


'''
# (Bonus) Problem 5: Sorted Array to Binary Search Tree
Leetcode Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree
Solution: https://guides.codepath.org/compsci/Convert-Sorted-Array-to-Binary-Search-Tree

Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Output: [0,-10,5,null,-3,null,9] is also accepted

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
'''
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         
# Your function sortedArrayToBST is called as such:
# nums = [1,2,3,4,5]
# sortedArrayToBST(root)
def sortedArrayToBST(nums: list[int]) -> TreeNode:
    def helper(left, right):
        if left > right:
            return None
        mid = left + (right - left) // 2
        root = TreeNode(nums[mid])
        root.left = helper(left, mid-1)
        root.right = helper(mid+1, right)
        return root
    return helper(0, len(nums)-1)
print("(Bonus) Problem 5: Sorted Array to Binary Search Tree")
print("nums = [-10,-3,0,5,9]:", root.treetoArray(sortedArrayToBST([-10,-3,0,5,9])))
print("nums = [1,3]:", root.treetoArray(sortedArrayToBST([1,3])))
print()