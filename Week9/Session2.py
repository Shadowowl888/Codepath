from collections import deque

'''
https://replit.com/@KuiduanZeng/Week9
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
# Problem 1: Find the Town Judge
Leetcode Link: https://leetcode.com/problems/find-the-town-judge
Solution: https://guides.codepath.org/compsci/Find-the-Town-Judge

In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
If the town judge exists, then:
1. The town judge trusts nobody.
2. Everybody (except for the town judge) trusts the town judge.
3. There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.
Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

Example 1:
Input: n = 2, trust = [[1,2]]
Output: 2

Example 2:
Input: n = 3, trust = [[1,3],[2,3]]
Output: 3

Example 3:
Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
'''

'''
Understand:
- Is the graph connected? not nesseary
- input: a list of [[ai, bi]]
- output: return -1
- Can the list be empty? it can. -1
    - Input: n = 1, trust = [], Output: 1

Match:
- Graph,  [1, 3],  person3 + 1, person1 - 1
- Town judge will have n - 1 trusts

Plan:
- numTrusts (differentiate from "trust")
- create a trusts array, initalizing with 0 value, the length will be (n+1).
- for loop to iterate through the input array trust
    - trusts[ai] -= 1
    - trusts[bi] += 1
- for loop to iterate through the trusts array:
    if trusts[i] == n - 1:
        return i
- return -1

- Input Cases:
- Input: n = 3, trust = [[1,3],[2,3]]
    - Output: 3, print(findJudge(n, trust))
- Input: n = 1, trust = []
    - Output: 1, print(findJudge(n, trust))
- Input: n = 4, trust = []
    - Output: -1, print(findJudge(n, trust))

Implement:
'''
# Your function findJudge is called as such:
# n = 3
# trust = [[1,3],[2,3]]
# findJudge(n, trust)
def findJudge(n: int, trust: list[list[int]]) -> int:
    trusted = [0] * (n + 1)
    for person1, person2 in trust:
        trusted[person1] -= 1
        trusted[person2] += 1
    for i in range(1, len(trusted)):
        if trusted[i] == n-1:
            return i
    return -1
print("Problem 1: Find the Town Judge")
print("n = 2, trust = [[1,2]]:", findJudge(2, [[1,2]]))
print("n = 3, trust = [[1,3],[2,3]]:", findJudge(3, [[1,3],[2,3]]))
print("n = 3, trust = [[1,3],[2,3],[3,1]]:", findJudge(3, [[1,3],[2,3],[3,1]]))
print()
'''
Evaluate:
- Time Complexity: O(V+E)
- Space Complexity: O(V)
'''


'''
# Problem 2: Find Center of Star Graph
Leetcode Link: https://leetcode.com/problems/find-center-of-star-graph
Solution: https://guides.codepath.org/compsci/Find-Center-of-Star-Graph

There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.
You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.

Example 1:
Input: edges = [[1,2],[2,3],[4,2]]
Output: 2
Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.

Example 2:
Input: edges = [[1,2],[5,1],[1,3],[1,4]]
Output: 1
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
# Your function findCenter is called as such:
# edges = [[1,3],[2,3],[4,2]]
# findCenter(edges)
def findCenter(edges: list[list[int]]) -> int:
    pass
print("Problem 2: Find Center of Star Graph")
print("edges = [[1,2],[2,3],[4,2]]:", findCenter([[1,2],[2,3],[4,2]]))
print("edges = [[1,2],[5,1],[1,3],[1,4]]:", findCenter([[1,2],[5,1],[1,3],[1,4]]))
print()
'''
Evaluate:
- Time Complexity: O()
- Space Complexity: O()
'''


'''
# Problem 3: Find if Path Exists in Graph
Leetcode Link: https://leetcode.com/problems/find-if-path-exists-in-graph
Solution: https://guides.codepath.org/compsci/Find-if-Path-Exists-in-Graph

There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.
You want to determine if there is a valid path that exists from vertex source to vertex destination.
Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

Example 1:
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2

Example 2:
Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.
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
# Your function validPath is called as such:
# edges = [[0,1],[1,2],[2,0]]
# validPath(3, edges, 0 ,2)
def validPath(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    pass
print("Problem 3: Find if Path Exists in Graph")
print("n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2:", validPath(3, [[0,1],[1,2],[2,0]], 0, 2))
print("n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5:", validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))
print()
'''
Evaluate:
- Time Complexity: O()
- Space Complexity: O()
'''


'''
# (Bonus) Problem 4: Decode String
Leetcode Link: https://leetcode.com/problems/decode-string
Solution: https://guides.codepath.org/compsci/Decode-String

Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].
The test cases are generated so that the length of the output will never exceed 10^5.

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
'''
# Your function decodeString is called as such:
# s = "3[a]2[bc]"
# decodeString(s)
def decodeString(s: str) -> str:
    pass
print("(Bonus) Problem 4: Decode String")
print('s = "3[a]2[bc]":', decodeString("3[a]2[bc]"))
print('s = "3[a2[c]]":', decodeString("3[a2[c]]"))
print('s = "2[abc]3[cd]ef":', decodeString("2[abc]3[cd]ef"))
print()


'''
# (Bonus) Problem 5: Add One Row to Tree
Leetcode Link: https://leetcode.com/problems/add-one-row-to-tree
Solution: https://guides.codepath.org/compsci/Add-One-Row-to-Tree

Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth depth.
Note that the root node is at depth 1.
The adding rule is:
- Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value val as cur's left subtree root and right subtree root.
- cur's original left subtree should be the left subtree of the new left subtree root.
- cur's original right subtree should be the right subtree of the new right subtree root.
- If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree.

Example 1:
Input: root = [4,2,6,3,1,5], val = 1, depth = 2
Output: [4,1,1,2,null,null,6,3,1,5]

Example 2:
Input: root = [4,2,null,3,1], val = 1, depth = 3
Output: [4,2,null,1,1,3,null,null,1]
'''
# Definition for a binary tree node.
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
# Your function addOneRow is called as such:
# root = TreeNode()
# val = 1
# depth = 1
# addOneRow(root, val, depth)
def addOneRow(root: TreeNode, val: int, depth: int) -> TreeNode:
    if depth == 1:
        return TreeNode(val, root, None)
    queue = deque()
    queue.append(root)
    currDepth = 2
    while currDepth < depth:
        width = len(queue)
        while width > 0:
            curr = queue.popleft()
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            width -= 1
        currDepth += 1
    for node in queue:
        node.left = TreeNode(val, node.left, None)
        node.right = TreeNode(val, None, node.right)
    return root
print("(Bonus) Problem 5: Add One Row to Tree")
root = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1)), TreeNode(6, TreeNode(5)))
print("root = [4,2,6,3,1,5], val = 1, depth = 2:", root.treetoArray(addOneRow(root, 1, 2)))
root = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1)))
print("root = [4,2,null,3,1], val = 1, depth = 3:", root.treetoArray(addOneRow(root, 1, 3)))
print()