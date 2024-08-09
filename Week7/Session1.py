from collections import deque, defaultdict

'''
https://replit.com/join/xyycrawftx-kuiduanzeng
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
# Problem 1: Binary Tree Level Order Traversal
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
Input: root = [ ]
Output: [ ]
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
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#         
# Your function levelOrder is called as such:
# root = TreeNode()
# levelOrder(root)
def levelOrder(root: TreeNode) -> list[list[int]]:
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
print("Problem 1: Binary Tree Level Order Traversal")
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print("root = [3,9,20,null,null,15,7]:", levelOrder(root))
root = TreeNode(1)
print("root = [1]:", levelOrder(root))
root = None
print("root = [ ]:", levelOrder(root))
print()
'''
Evaluate:
- Time Complexity: O(n)
- Space Complexity: O(n)
'''


'''
# Problem 2: All Nodes Distance K in Binary Tree
Leetcode Link: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree
Solution: https://guides.codepath.org/compsci/All-Nodes-Distance-K-in-Binary-Tree

Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.
You can return the answer in any order.

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.

Example 2:
Input: root = [1], target = 1, k = 3
Output: [ ]
'''

'''
Understand:
- Is it a BST tree? No, it just a binary tree
- Can you put answer in any order? Yes
- Could k or target be an invalid value? 
- What should return when tree is empty? Not empty
- What's type of target? TreeNode
- No duplicate nodes value in the tree
      3
    5   1
 6  2  0  8 
   7 4

Match:
- preorder
- inorder
- postorder
- binary tree level order
- Hashmap to record something
- BST - this is not a BST

Plan:
- Create a list that keep track of nodes and their neighbors
- Construct graph, traverse the tree using dfs
- Connect the nodes two by two, parent -> child, child -> parent
- Solution: https://imgur.com/a/EilWmDf

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
# distanceK(root, rightNode, 1)
def buildGraph(node, parent, graph):
    if node:
        # Create bi-directional graph
        if parent:
            graph[node.val].append(parent.val)
            graph[parent.val].append(node.val)
        buildGraph(node.left, node, graph)
        buildGraph(node.right, node, graph)
def distanceK(root: TreeNode, target: TreeNode, k: int) -> list[int]:
    graph = defaultdict(list)
    buildGraph(root, None, graph)
    
    visited = set()
    queue = deque([(target.val, 0)])
    result = []

    while queue:
        current, distance = queue.popleft()
        if distance == k:
            result.append(current)
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append((neighbor, distance + 1))
    return result
print("Problem 2: All Nodes Distance K in Binary Tree")
root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
print("root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2:", distanceK(root, root.left, 2))
root = TreeNode(1)
print("root = [1], target = 1, k = 3:", distanceK(root, root, 3))
print()
'''
Evaluate:
- Time Complexity: O(n)
- Space Complexity: O(n)
'''


'''
# Problem 3: Distribute Coins in Binary Tree
Leetcode Link: https://leetcode.com/problems/distribute-coins-in-binary-tree
Solution: https://guides.codepath.org/compsci/Distribute-Coins-in-Binary-Tree

You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. There are n coins in total throughout the whole tree.
In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.
Return the minimum number of moves required to make every node have exactly one coin.

Example 1:
Input: root = [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.

Example 2:
Input: root = [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root [taking two moves]. Then, we move one coin from the root of the tree to the right child.
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
# Your function distributeCoins is called as such:
# root = TreeNode()
# distributeCoins(root)
def distributeCoins(root: TreeNode) -> int:
    pass
print("Problem 3: Distribute Coins in Binary Tree")
root = TreeNode(3, TreeNode(0), TreeNode(0))
print("root = [3,0,0]:", distributeCoins(root))
root = TreeNode(0, TreeNode(3), TreeNode(0))
print("root = [0,3,0]:", distributeCoins(root))
print()
'''
Evaluate:
- Time Complexity: O()
- Space Complexity: O()
'''


'''
# (Bonus) Problem 4: Lowest Common Ancestor of a Binary Tree
Leetcode Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree
Solution: https://guides.codepath.org/compsci/Lowest-Common-Ancestor-of-a-Binary-Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [1,2], p = 1, q = 2
Output: 1
'''
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         
# Your function lowestCommonAncestor is called as such:
# root = TreeNode()
# rightNode = TreeNode()
# root.right = rightNode
# leftNode = TreeNode()
# root.left = leftNode
# lowestCommonAncestor(root, leftNode, rightNode)
def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    pass
print("(Bonus) Problem 4: Lowest Common Ancestor of a Binary Tree")
root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
print("root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1:", lowestCommonAncestor(root, root.left, root.right))
root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
print("root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4:", lowestCommonAncestor(root, root.left, root.left.right.right))
root = TreeNode(1, TreeNode(2))
print("root = [1,2], p = 1, q = 2:", lowestCommonAncestor(root, root, root.left))
print()


'''
# (Bonus) Problem 5: Path Sum III
Leetcode Link: https://leetcode.com/problems/path-sum-iii
Solution: https://guides.codepath.org/compsci/Path-Sum-III

Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

Example 1:
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example 2:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
'''
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         
# Your function pathSum is called as such:
# root = TreeNode()
# pathSum(root)
def pathSum(root: TreeNode, targetSum: int) -> int:
    def helper(root, sum):
        if not root:
            return 0
        return (sum - root.val == 0 if 1 else 0) + helper(root.left, sum - root.val) + helper(root.right, sum - root.val)
    if not root:
        return 0
    return helper(root, targetSum) + pathSum(root.left, targetSum) + pathSum(root.right, targetSum)
print("(Bonus) Problem 5: Path Sum III")
root = TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))), TreeNode(-3, None, TreeNode(11)))
print("root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8:", pathSum(root, 8))
root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), None), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
print("root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22:", pathSum(root, 22))
print()