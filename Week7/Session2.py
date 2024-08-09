from collections import deque

'''
https://replit.com/join/ffneydrltb-hannahsim1
https://courses.codepath.org/courses/tip103/pages/mock_interview_guide
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
# Problem 1: Insert into a Binary Search Tree
Leetcode Link: https://leetcode.com/problems/insert-into-a-binary-search-tree
Solution: https://guides.codepath.org/compsci/Insert-Into-a-Binary-Search-Tree

You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.
Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

Example 1:
Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: One accepted tree tree is:

Example 2:
Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]

Example 3:
Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]
'''

'''
Understand:
- Input: root node of a BST and a value
- Output is a BST with teh new value
- Tree doesnt need to be complete
- Try to complete within O(log n) time and space

Match:
- Pre post in order level
- Pre order
- Hashmap: extra steps    

Plan:
- Checking if the current node is empty
- Iterative:
    - Follow the current node and check if given value is greater. If so, then insert the value to the right tree.
    - If one side is empty, then insert the value to that side. Repeat the same for when the value is smaller.
    - break out of loop when one side is empty
- Recursive:
    - Checking if current node is empty
    - IF value at root is greater than the given value, then insert value to right. Just call itself.
    - If value at root is less than given value, insert to left
    - return root

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
# Your function insertIntoBST is called as such:
# root = TreeNode()
# insertIntoBST(root, 1)
def insertIntoBST(root: TreeNode,  val: int) -> TreeNode:
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insertIntoBST(root.left, val)
    else:
        root.right = insertIntoBST(root.right, val)
    return root
print("Problem 1: Insert into a Binary Search Tree")
root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
print("root = [4,2,7,1,3], val = 5:", root.treetoArray(insertIntoBST(root, 5)))
root = TreeNode(40, TreeNode(20, TreeNode(10), TreeNode(30)), TreeNode(60, TreeNode(50), TreeNode(70)))
print("root = [40,20,60,10,30,50,70], val = 25:", root.treetoArray(insertIntoBST(root, 25)))
root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
print("root = [4,2,7,1,3,null,null,null,null,null,null], val = 5:", root.treetoArray(insertIntoBST(root, 5)))
print()
'''
Evaluate:
- Time Complexity: O(H)
- Space Complexity: O(H)
'''


'''
# Problem 2: Kth Smallest Element in a BST
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

'''
Understand:
- 

Match:
- 

Plan:
- 

Implement:
'''
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         
# Your function distanceK is called as such:
# root = TreeNode()
# rightNode = TreeNode()
# root.right = rightNode
# distanceK(root, 1)
def distanceK(root: TreeNode, k: int) -> int:
    pass
print("Problem 2: Kth Smallest Element in a BST")
root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
print("root = [3,1,4,null,2], k = 1:", distanceK(root, 1))
root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
print("root = [5,3,6,2,4,null,null,1], k = 3:", distanceK(root, 3))
print()
'''
Evaluate:
- Time Complexity: O()
- Space Complexity: O()
'''


'''
# Problem 3: Validate Binary Search Tree
Leetcode Link: https://leetcode.com/problems/validate-binary-search-tree
Solution: https://guides.codepath.org/compsci/Validate-Binary-Search-Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         
# Your function isValidBST is called as such:
# root = TreeNode()
# isValidBST(root)
def isValidBST(root: TreeNode) -> bool:
    pass
print("Problem 3: Validate Binary Search Tree")
root = TreeNode(2, TreeNode(1), TreeNode(3))
print("root = [2,1,3]:", isValidBST(root))
root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
print("root = [5,1,4,null,null,3,6]:", isValidBST(root))
print()


'''
# (Bonus) Problem 4: Construct Binary Tree from Preorder and Inorder Traversal
Leetcode Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
Solution: https://guides.codepath.org/compsci/Construct-Binary-Tree-from-Preorder-and-Inorder-Traversal

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]
'''
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         
# Your function buildTree is called as such:
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# buildTree(preorder, inorder)
def buildTree(preorder: list[int], inorder: list[int]) -> TreeNode:
    pass
print("(Bonus) Problem 4: Construct Binary Tree from Preorder and Inorder Traversal")
print("preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]:", buildTree([3,9,20,15,7], [9,3,15,20,7]))
print("preorder = [-1], inorder = [-1]:", buildTree([-1], [-1]))
print()


'''
# (Bonus) Problem 5: Binary Tree Pruning
Leetcode Link: https://leetcode.com/problems/binary-tree-pruning
Solution: https://guides.codepath.org/compsci/Binary-Tree-Pruning

Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.
A subtree of a node node is node plus every node that is a descendant of node.

Example 1:
Input: root = [1,null,0,0,1]
Output: [1,null,0,null,1]
Explanation: Only the red nodes satisfy the property "every subtree not containing a 1". The diagram on the right represents the answer.

Example 2:
Input: root = [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]

Example 3:
Input: root = [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]
'''
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         
# Your function pruneTree is called as such:
# root = TreeNode()
# rightNode = TreeNode()
# root.right = rightNode
# pruneTree(root, rightNode, 1)
def pruneTree(root: TreeNode) -> TreeNode:
    def containsOne(node):
        if not node:
            return False
        leftContainsOne = containsOne(node.left)
        rightContainsOne = containsOne(node.right)
        if (not leftContainsOne):
            node.left = None
        if (not rightContainsOne):
            node.right = None
        return node.val == 1 or leftContainsOne or rightContainsOne
    return root if containsOne(root) else None
print("(Bonus) Problem 5: Binary Tree Pruning")
root = TreeNode(1, None, TreeNode(0, TreeNode(0), TreeNode(1)))
print("root = [1,null,0,0,1]:", root.treetoArray(pruneTree(root)))
root = TreeNode(1, TreeNode(0, TreeNode(0), TreeNode(0)), TreeNode(1, TreeNode(0), TreeNode(1)))
print("root = [1,0,1,0,0,0,1]:", root.treetoArray(pruneTree(root)))
root = TreeNode(1, TreeNode(1, TreeNode(1, 0), TreeNode(1)), TreeNode(0, TreeNode(0), TreeNode(1)))
print("root = [1,1,0,1,1,0,1,0]:", root.treetoArray(pruneTree(root)))
print()