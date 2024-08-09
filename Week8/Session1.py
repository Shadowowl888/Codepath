'''
https://replit.com/join/gekouwgkeq-ethanngo13
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
# Problem 1: Transpose Matrix
Leetcode Link: https://leetcode.com/problems/transpose-matrix
Solution: https://guides.codepath.org/compsci/Transpose-Matrix

Given a 2D integer array matrix, return the transpose of matrix.
The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:
Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
'''

'''
Understand:
- Does the length of the row and columns match? NO
- Can the matrix be one cell? YES
- Input: 2d array of integers
- Output: transposed matrix

Match:
- BFS
- DFS
- Putting numbers into a hashmap
- Own pattern - switching the rows with the columns
- matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

Plan:
1. Create an empty result matrix T
2. Iterate through the rows i:
    3. Iterate through the columns j:
        - Add a new row j
        - Add the elements in i
- https://imgur.com/a/oxvcSQX
    - transposed = [[i] for i in range(10)]
    - print(transposed)

Implement:
'''
# Your function transpose is called as such:
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# transpose(matrix)
def transpose(matrix: list[list[int]]) -> list[list[int]]:
    result = []
    for j in range(len(matrix[0])): #columns
        row = []
        for i in range(len(matrix)): #rows
            row.append(matrix[i][j])
        result.append(row)
    return result
    # return zip(*matrix)
    # return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
print("Problem 1: Transpose Matrix")
print("matrix = [[1,2,3],[4,5,6],[7,8,9]]:", transpose([[1,2,3],[4,5,6],[7,8,9]]))
print("matrix = [[1,2,3],[4,5,6]]:", transpose([[1,2,3],[4,5,6]]))
print()
'''
Evaluate:
- Time Complexity: O(n*m)
- Space Complexity: O(n*m)
'''


'''
# Problem 2: Flipping an Image
Leetcode Link: https://leetcode.com/problems/flipping-an-image
Solution: https://guides.codepath.org/compsci/Flipping-an-Image

Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.
To flip an image horizontally means that each row of the image is reversed.
- For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
- For example, inverting [0,1,1] results in [1,0,0].

Example 1:
Input: image = [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

Example 2:
Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
'''

'''
Understand:
- input: nxn binary matrix (square), type of data: integer
- output: Flip the matrix then invert it
- 1x1 matrix: return just the inverse
- empty matrix:
- 1 <= n <= 20

Match:
- Pattern: Flip and reverse
- Two pointer: one point at beginning and one at end (SWAP)
    - meet at middle or cross then stop

Plan:
1. Iterate through the outer loop i
    - Set left pointer to [i][0]
    - Set right pointer to [i][len(matrix[i-1])]
    - While left <= right pointer
        - Swap left and right
        - new element = 1 - curr
        0 : 1 - 0 = 1
        1 : 1 - 1 = 0
        - increment left and decrement right
- https://imgur.com/a/kAZZkQC

Implement:
'''
# Your function flipAndInvertImage is called as such:
# image = [[1,1,0],[1,0,1],[0,0,0]]
# flipAndInvertImage(image)
def flipAndInvertImage(image: list[list[int]]) -> list[list[int]]:
    for i in range(len(image)):
        left, right = 0, len(image[i])-1
        while left <= right:
            image[i][left], image[i][right] = image[i][right], image[i][left]
            if left < right:
                image[i][left] = 1 - image[i][left]
                image[i][right] = 1 - image[i][right]
            else:
                image[i][left] = 1 - image[i][left]
            left += 1
            right -= 1
    return image
    # for row in image:
    #     row.reverse()
    #     # For each row flip each item from 0 to 1 and 0 to 1.
    #     for i, element in enumerate(row):
    #         if element == 1:
    #             row[i] = 0
    #         else:
    #             row[i] = 1
    # return image
print("Problem 2: Flipping an Image")
print("image = [[1,1,0],[1,0,1],[0,0,0]]:", flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
print("image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]:", flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))
print()
'''
Evaluate:
- Time Complexity: O(n*m)
- Space Complexity: O(1)
'''


'''
# Problem 3: Rotate Image
Leetcode Link: https://leetcode.com/problems/rotate-image
Solution: https://guides.codepath.org/compsci/Rotate-Image

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
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
# Your function rotate is called as such:
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# rotate(matrix)
def rotate(matrix: list[list[int]]) -> None:
    def solve(n, start):
        if start >= n/2:
            return
        for i in range(start, n-1-start):
            a = matrix[start][i]
            b = matrix[i][n-1-start]
            c = matrix[n-1-start][n-1-i]
            d = matrix[n-1-i][start]
            
            matrix[start][i] = d
            matrix[i][n-1-start] = a
            matrix[n-1-start][n-1-i] = b
            matrix[n-1-i][start] = c
        solve(n, start+1)
    solve(len(matrix), 0)
    return matrix
print("Problem 3: Rotate Image")
print("matrix = [[1,2,3],[4,5,6],[7,8,9]]:", rotate([[1,2,3],[4,5,6],[7,8,9]]))
print("matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]:", rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
print()
'''
Evaluate:
- Time Complexity: O(n*m)
- Space Complexity: O(1)
'''


'''
# (Bonus) Problem 4: Spiral Matrix
Leetcode Link: https://leetcode.com/problems/spiral-matrix
Solution: https://guides.codepath.org/compsci/Spiral-Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''
# Your function spiralOrder is called as such:
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# spiralOrder(matrix)
def spiralOrder(matrix: list[list[int]]) -> list[int]:
    pass
print("(Bonus) Problem 4: Spiral Matrix")
print("matrix = [[1,2,3],[4,5,6],[7,8,9]]:", spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print("matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]:", spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print()


'''
# (Bonus) Problem 5: Search 2D Matrix
Leetcode Link: https://leetcode.com/problems/search-a-2d-matrix
Solution: https://guides.codepath.org/compsci/Search-a-2D-Matrix

You are given an m x n integer matrix matrix with the following two properties:
- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
'''
# Your function searchMatrix is called as such:
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# searchMatrix(matrix)
def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m*n - 1
    mid, pivotElement = 0, 0
    while left <= right:
        mid = (left + right) // 2
        pivotElement = matrix[mid // n][mid % n]
        if pivotElement == target:
            return True
        elif target < pivotElement:
            right = mid - 1
        else:
            left = mid + 1
    return False
print("(Bonus) Problem 5: Search 2D Matrix")
print("matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3:", searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print("matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13:", searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
print()