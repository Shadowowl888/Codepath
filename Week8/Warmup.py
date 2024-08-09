from typing import List

'''
# Warmup Problem: Island Perimeter
Leetcode Link: https://leetcode.com/problems/island-perimeter
Solution: https://guides.codepath.org/compsci/Island-Perimeter

You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example 1:
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.

Example 2:
Input: grid = [[1]]
Output: 4

Example 3:
Input: grid = [[1,0]]
Output: 4
'''
def islandPerimeter(grid: List[List[int]]) -> int:
    def dfs(i, j):
        if i < 0 or i > len(grid)-1 or j < 0 or j > len(grid[i])-1:
            return 1
        elif grid[i][j] == 0:
            return 1
        elif grid[i][j] == -1:
            return 0
        else:
            grid[i][j] = -1
            return dfs(i, j-1) + dfs(i, j+1) + dfs(i-1, j) + dfs(i+1, j)
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                return dfs(i, j)
print("Warmup Problem: Island Perimeter")
print("grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]:", islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
print("grid = [[1]]:", islandPerimeter([[1]]))
print("grid = [[1,0]]:", islandPerimeter([[1,0]]))
print()