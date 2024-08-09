'''
https://replit.com/join/wxfbuqgmpf-evanhaut
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
# Problem 1: Number of Islands
Leetcode Link: https://leetcode.com/problems/number-of-islands
Solution: https://guides.codepath.org/compsci/Number-of-Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''

'''
Understand:
- can single tile
- cant connect dia
- cant be empty 
- 1 < 300

Match:
- travesls: DFS, BFS, Row by row, col by col
- adjcant list: not needed 

Plan:
- getting lengths of row and col
- recuvice function: visit(grid, row, col))
-	return if out of bounds or not 1
-	mark current tile as visited change value to -1
  visit(up)
  visit(right)
  visit(left)
  visit(down)

count = 0
forloop rows:
	for cols:
		if value is 1:
			visit(row, col)
			count ++

Implement:
'''
# Your function numIslands is called as such:
# grid = [
# ["1","1","1","1","0"],
# ["1","1","0","1","0"],
# ["1","1","0","0","0"]
# ]
# numIslands(grid)
def numIslands(grid: list[list[str]]) -> int:
  # rowlen, collen = len(grid), len(grid[0])
  # def visit(grid, row, col):
  #   # row = 3, col = 0, grid[row][col] = 1
  #   print(row)
  #   print(col)
	# 	if row < 0 and row >= rowlen or col < 0 or col >= collen or grid[row][col] != "1":
  #     return
  #   grid[row][col] = "-1"
	# 	visit(grid, row + 1, col)
	# 	visit(grid, row - 1, col)
	# 	visit(grid, row, col + 1)
	# 	visit(grid, row, col - 1)
	# count = 0
	# for r in range(rowlen):
	#   for c in range(collen):
	# 		if grid[r][c] == "1":
	# 			visit(grid, r, c)
	# 			count += 1
  # return count

  def helper(i, j):
    grid[i][j] = "-1"
    neighbors = [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
    for (row,col) in neighbors:
      if 0 <= row < m and 0 <= col < n and grid[row][col] == "1":
        helper(row,col)
  m, n = len(grid), len(grid[0])
  result = 0
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == "1":
        helper(i,j)
        result += 1
  return result
print("Problem 1: Number of Islands")
print('grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]:', numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
print('grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]:', numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))
print()
'''
Evaluate:
- Time Complexity: O(V log V)
- Space Complexity: O(V)
'''


'''
# Problem 2: Max Area of Island
Leetcode Link: https://leetcode.com/problems/max-area-of-island
Solution: https://guides.codepath.org/compsci/Max-Area-Of-Island

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
The area of an island is the number of cells with a value 1 in the island.
Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
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
# Your function maxAreaOfIsland is called as such:
# grid = [
# [0,0,0,0,0,0,0,0]
# ]
# maxAreaOfIsland(grid)
def maxAreaOfIsland(grid: list[list[int]]):
    pass
print("Problem 2: Max Area of Island")
print("grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]:", maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
print("grid = [[0,0,0,0,0,0,0,0]]:", maxAreaOfIsland([[0,0,0,0,0,0,0,0]]))
print()
'''
Evaluate:
- Time Complexity: O()
- Space Complexity: O()
'''


'''
# Problem 3: Battleships in a Board
Leetcode Link: https://leetcode.com/problems/battleships-in-a-board
Solution: https://guides.codepath.org/compsci/Battleships-in-a-Board

Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.
Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

Example 1:
Input: board = [
  ["X",".",".","X"],
  [".",".",".","X"],
  [".",".",".","X"]
]
Output: 2

Example 2:
Input: board = [["."]]
Output: 0
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
# Your function countBattleships is called as such:
# board = [
# ["."]
# ]
# countBattleships(board)
def countBattleships(board: list[list[str]]) -> int:
    pass
print("Problem 3: Battleships in a Board")
print('board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]:', countBattleships([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]))
print('board = [["."]]:', countBattleships([["."]]))
print()
'''
Evaluate:
- Time Complexity: O()
- Space Complexity: O()
'''


'''
# (Bonus) Problem 4: Rotting Oranges
Leetcode Link: https://leetcode.com/problems/rotting-oranges
Solution: https://guides.codepath.org/compsci/Rotting-Oranges

You are given an m x n grid where each cell can have one of three values:
- 0 representing an empty cell,
- 1 representing a fresh orange, or
- 2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
'''
# Your function orangesRotting is called as such:
# grid = [
# [2,1,1],
# [1,1,0],
# [0,1,1]
# ]
# orangesRotting(grid)
def orangesRotting(grid: list[list[int]]) -> int:
  pass
print("(Bonus) Problem 4: Rotting Oranges")
print("grid = [[2,1,1],[1,1,0],[0,1,1]]:", orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print("grid = [[2,1,1],[0,1,1],[1,0,1]]:", orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
print("grid = [[0,2]]:", orangesRotting([[0,2]]))
print()


'''
# (Bonus) Problem 5: Flood Fill
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
print("(Bonus) Problem 5: Flood Fill")
print("image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2:", floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
print("image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0:", floodFill([[0,0,0],[0,0,0]], 0, 0, 0))
print()