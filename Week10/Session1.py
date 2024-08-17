'''
https://replit.com/join/copejgyfdu-ethanngo13
https://docs.google.com/document/d/1Upq9qnOttEDDe6w0Cud21SkHZE-lptK98wAx5mTKmMk/edit
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
# Problem 1: Pacific Atlantic Water Flow
Leetcode Link: https://leetcode.com/problems/pacific-atlantic-water-flow
Solution: https://guides.codepath.org/compsci/Pacific-Atlantic-Water-Flow

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Example 1:
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

Example 2:
Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.

Example 3:
Input: heights = [[0,2,2,0]]
Output: [[0,0],[0,1],[0,2][0,3]]
'''

'''
Understand:
- rain water can flow lower or equal to the current elevation
- Each yellow point is where rain water can flow both to atlantic or pacific
- Can move in only up,down,left,right
- Can we be given an empty grid? NO 1 < n < ...
- What would we return for single elevation? [0,0]
- Input: grid of elevations
- Output: grid of points where water goes to edges

Match:
- DFS: Visit the different paths based on if the elevation is less than
- Storing points in hashset: store the visited nodes
- Storing points in hashmap: NA, not searching for anything

Plan:
1. Iterate through all the points in the grid:
    2. call the helper on top and bottom row
        - Get the difference of the sets
    3. call the helper on left and right col
        - Get the difference of the sets       
- Helper
    - Base Case:
    Atlantic : > length of rows or length col
    Pacific : < 0 for row and col
        Return
    - If the next point is >= the current elevation, then we should call the helper on that point
    - Store it in a set

Implement:
'''
# Your function pacificAtlantic is called as such:
# heights = [[1,3],[2,3]]
# pacificAtlantic(heights)
def pacificAtlantic(heights: list[list[int]]) -> list[list[int]]:
    def dfs(x, y, grid, maxHeight):
        if x < 0 or y < 0 or y > len(grid) or y > len(grid[0]):
            return
        if grid[x][y] >= maxHeight:
            dfs(x + 1, y, grid, grid[x][y])
            dfs(x - 1, y, grid, grid[x][y])
            dfs(x, y + 1, grid, grid[x][y])
            dfs(x, y-1, grid, grid[x][y])
print("Problem 1: Pacific Atlantic Water Flow")
print("heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]:", pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
print("heights = [[1]]:", pacificAtlantic([[1]]))
print("heights = [[0,2,2,0]]:", pacificAtlantic([[0,2,2,0]]))
print()
'''
Evaluate:
- Time Complexity: O()
- Space Complexity: O()
'''


'''
# Problem 2: Lowest Common Ancestor of a Binary Tree
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

'''
Understand:
- 

Match:
- 

Plan:
- 

Implement:
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#         
# Your function lowestCommonAncestor is called as such:
# root = TreeNode()
# left = TreeNode()
# right = TreeNode()
# root.left = left
# root.right = right
# lowestCommonAncestor(root, left, right)
def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    pass
print("Problem 2: Lowest Common Ancestor of a Binary Tree")
root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
print("root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1:", lowestCommonAncestor(root, root.left, root.right))
root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
print("root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4:", lowestCommonAncestor(root, root.left, root.left.right.right))
root = TreeNode(1, TreeNode(2))
print("root = [1,2], p = 1, q = 2:", lowestCommonAncestor(root, root, root.left))
print()
'''
Evaluate:
- Time Complexity: O()
- Space Complexity: O()
'''


'''
# Problem 3: Flood Fill
Leetcode Link: https://leetcode.com/problems/flood-fill
Solution: https://guides.codepath.org/compsci/Flood-Fill

An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].
To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.
Return the modified image after performing the flood fill.

Example 1:
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

Example 2:
Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation: The starting pixel is already colored 0, so no changes are made to the image.

Example 3:
Input: image = [[1,0,0],[0,1,0],[0,0,1]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,1,0],[0,0,1]]
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
# Your function floodFill is called as such:
# image = [
# [2,1,1],
# [1,1,0],
# [0,1,1]
# ]
# floodFill(image, 1, 1, 2)
def floodFill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    pass
print("Problem 3: Flood Fill")
print("image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2:", floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
print("image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0:", floodFill([[0,0,0],[0,0,0]], 0, 0, 0))
print("image = [[1,0,0],[0,1,0],[0,0,1]], sr = 0, sc = 0, color = 0:", floodFill([[1,0,0],[0,1,0],[0,0,1]], 0, 0, 0))
print()
'''
Evaluate:
- Time Complexity: O()
- Space Complexity: O()
'''


'''
# (Bonus) Problem 4: Accounts Merge
Leetcode Link: https://leetcode.com/problems/accounts-merge
Solution: https://guides.codepath.org/compsci/Accounts-Merge

Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.
Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.
After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:
Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

Example 2:
Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]

Example 3:
Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co"]]
Output: [["Gabe","Gabe0@m.co","Gabe3@m.co"]]
'''
# Your function accountsMerge is called as such:
# accounts = [
# ["John","johnsmith@mail.com","john_newyork@mail.com"],
# ["John","johnsmith@mail.com","john00@mail.com"],
# ["Mary","mary@mail.com"],
# ["John","johnnybravo@mail.com"]
# ]
# accountsMerge(accounts)
def accountsMerge(accounts: list[list[str]]) -> list[list[str]]:
    pass
print("(Bonus) Problem 4: Accounts Merge")
print('accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]:', accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))
print('accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]:', accountsMerge([["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]))
print('accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co"]]:', accountsMerge([["Gabe","Gabe0@m.co","Gabe3@m.co"]]))
print()


'''
# (Bonus) Problem 5: House Robber
Leetcode Link: https://leetcode.com/problems/house-robber
Solution: https://guides.codepath.org/compsci/House-Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
'''
# Your function rob is called as such:
# nums = [2,7,9,3,1]
# rob(nums)
def rob(nums: list[int]) -> int:
    pass
print("(Bonus) Problem 5: House Robber")
print("nums = [1,2,3,1]:", rob([1,2,3,1]))
print("nums = [2,7,9,3,1]:", rob([2,7,9,3,1]))
print()