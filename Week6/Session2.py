'''
https://replit.com/join/actjyqvilo-ethanngo13
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
# Problem 1: Binary Tree Paths
Leetcode Link: https://leetcode.com/problems/binary-tree-paths
Solution: https://guides.codepath.org/compsci/Binary-Tree-Paths

Given the root of a binary tree, return all root-to-leaf paths in any order.

Example 1
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Example 2
Input: root = [1]
Output: ["1"]
'''

'''
Understand:
- Any form of binary tree
- Input: binary tree
- Output: the numbers of paths with n leaves

Match:
- Tree traversals: preorder and postorder
Add a path to an array when there is a leaf node
1 2 5, 1 3
- Hashmap: not helpful
- Binary tree search: not searching for elements
    1
  2    3
5
["1,2,5"]

Plan:
1. Base case: when encounter a leaf ( node is null )
    add the string to the array
    pop the most recent element from the string
    return
2. Add the element of the node into our string
    - Every other element add arrow before it plus element
3. Call the recursive function(node.left)
4. Call the recursive function(node.right)

Implement:
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#         
# Your function binaryTreePaths is called as such:
# root = TreeNode()
# binaryTreePaths(root)
def binaryTreePaths(root: TreeNode) ->list[str]:
    # def helper(node, path, answer):
    #     if node is None:
    #         path.pop()
    #         answer.append(path)
    #         path.pop()
    #         return
    #     path.append(str(node.val))
    #     path.append("->")
    #     helper(node.left, path, answer)
    #     helper(node.right,path, answer)
    # answer = []
    # path = []
    # helper(root, path, answer)
    # return answer

    # Create helper function to allow us to retain memory of allPaths
    def helper(root, currPath):
        if not root:
            return
        currPath.append(str(root.val))
        if not root.left and not root.right:
            allPaths.append("->".join(currPath))
        helper(root.left, currPath)
        helper(root.right, currPath)
        currPath.pop()
    allPaths = []
    helper(root, [])
    return allPaths
print("Problem 1: Binary Tree Paths")
root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
print("root = [1,2,3,null,5]:", binaryTreePaths(root))
root = TreeNode(1)
print("root = [1]:", binaryTreePaths(root))
print()
'''
Evaluate:
- Time Complexity: O(n)
- Space Complexity: O(n)
'''


'''
# Problem 2: Balanced Binary Tree
Leetcode Link: https://leetcode.com/problems/balanced-binary-tree
Solution: https://guides.codepath.org/compsci/Balanced-Binary-Tree

Given a binary tree, determine if it is height-balanced.
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Example 1
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3
Input: root = []
Output: true
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
# Your function isBalanced is called as such:
# root = TreeNode()
# isBalanced(root)
def isBalanced(root: TreeNode) ->bool:
    pass
print("Problem 2: Balanced Binary Tree")
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print("root = [3,9,20,null,null,15,7]:", isBalanced(root))
root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
print("root = [1,2,2,3,3,null,null,4,4]:", isBalanced(root))
root = TreeNode()
print("root = []:", isBalanced(root))
print()
'''
Evaluate:
- Time Complexity: O()
- Space Complexity: O()
'''


'''
# Problem 3: Symmetric Tree
Leetcode Link: https://leetcode.com/problems/symmetric-tree
Solution: https://guides.codepath.org/compsci/Symmetric-Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2
Input: root = [1,2,2,null,3,null,3]
Output: false
'''
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         
# Your function isSymmetric is called as such:
# root = TreeNode()
# isSymmetric(root)
def isSymmetric(root: TreeNode) ->bool:
    pass
print("Problem 3: Symmetric Tree")
root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
print("root = [1,2,2,3,4,4,3]:", isSymmetric(root))
root = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
print("root = [1,2,2,null,3,null,3]:", isSymmetric(root))
print()


'''
# (Bonus) Problem 4: Diameter of Binary Tree
Leetcode Link: https://leetcode.com/problems/diameter-of-binary-tree
Solution: https://guides.codepath.org/compsci/Diameter-of-Binary-Tree

Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.

Example 1
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2
Input: root = [1,2]
Output: 1
'''
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         
# Your function diameterOfBinaryTree is called as such:
# root = TreeNode()
# diameterOfBinaryTree(root)
def diameterOfBinaryTree(root: TreeNode) -> int:
    pass
print("(Bonus) Problem 4: Diameter of Binary Tree")
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print("root = [1,2,3,4,5]:", diameterOfBinaryTree(root))
root = TreeNode(1, TreeNode(2))
print("root = [1,2]:", diameterOfBinaryTree(root))
print()


'''
# (Bonus) Problem 5: Path Sum
Leetcode Link: https://leetcode.com/problems/path-sum
Solution: https://guides.codepath.org/compsci/Path-Sum

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

Example 1
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.
'''
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         
# Your function hasPathSum is called as such:
# root = TreeNode()
# hasPathSum(root)
def hasPathSum(root: TreeNode, targetSum: int) -> bool:
    # Set basecase to root is None, return False
    if not root:
        return False
    # Upon reaching a leaf node, check if value is equal to targetSum
    if not root.left and not root.right and root.val == targetSum:
        return True
    # Recursively proceed to next node and remove value from targetSum
    return hasPathSum(root.left, targetSum - root.val) or hasPathSum(root.right, targetSum - root.val)
print("(Bonus) Problem 5: Path Sum")
root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), None), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
print("root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22:", hasPathSum(root, 22))
root = TreeNode(1, TreeNode(2), TreeNode(3))
print("root = [1,2,3], targetSum = 5:", hasPathSum(root, 5))
root = None
print("root = [], targetSum = 0:", hasPathSum(root, 0))
print()