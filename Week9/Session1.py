'''
https://replit.com/join/gmhgqbsiwt-kuiduanzeng
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
# Problem 1: Fibonacci Number
Leetcode Link: https://leetcode.com/problems/fibonacci-number
Solution: https://guides.codepath.org/compsci/Fibonacci-Number

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
- F(0) = 0, F(1) = 1
- F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

Example 1:
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
'''

'''
Understand:
- Do we use top-down or bottom-up? both
- Space constraint? O(n), but try to not save in it an array

Match:
- Top down, recursion, memoization
- Bottom up, iterative, DP Table
- Use a dp array to keep track of previous value

Plan:
- 

Implement:
'''
# Your function fib is called as such:
# fib(6)
def fib(n: int) -> int:
    # Recursive Approach
    # if n <= 1:
    #     return n
    # return fib(n-1) + fib(n-2)

    # Top-Down Approach
    # dp = [0] * (n+1)
    # def helper(n):
    #     if n <= 1:
    #         return n
    #     if dp[n] == 0:
    #         dp[n] = helper(n-1) + helper(n-2)
    #     return dp[n]
    # return helper(n)

    # Bottom-Up Approach
    # if n <= 1:
    #     return n
    # dp = [0] * (n+1)
    # dp[0], dp[1] = 0, 1
    # for i in range(2, n+1):
    #     dp[i] = dp[i-1] + dp[i-2]
    # return dp[n]

    # Two Variables Approach
    if n <= 1:
        return n
    fib1, fib2 = 0, 1
    for i in range(2, n+1):
        fib1, fib2 = fib2, fib1 + fib2
    return fib2
print("Problem 1: Fibonacci Number")
print("n = 2:", fib(2))
print("n = 3:", fib(3))
print("n = 4:", fib(4))
print()
'''
Evaluate:
- Time Complexity: O(n)
- Space Complexity: O(1)
'''


'''
# Problem 2: Min Cost Climbing Stairs
Leetcode Link: https://leetcode.com/problems/min-cost-climbing-stairs
Solution: https://guides.codepath.org/compsci/Min-Cost-Climbing-Stairs

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.

Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
'''

'''
Understand:
- Climb until n index, 
- Can we modify the input array?
- Can the cost be negative? no 
- 2 <= cost.length <= 1000
- 0 <= cost[i] <= 999

Match:
- Top down and bottom up

Plan:
- dp[0] = cost[0], dp[1] = cost[1]

Implement:
'''
# Your function minCostClimbingStairs is called as such:
# cost = [10, 15, 20]
# minCostClimbingStairs(cost)
def minCostClimbingStairs(cost: list[int]) -> int:
    # Top-Down Approach
    # n = len(cost)
    # dp = [0] * n
    # def helper(n):
    #     if n <= 1:
    #         return cost[n]
    #     if dp[n] == 0:
    #         dp[n] = cost[n] + min(helper(n-1), helper(n-2))
    #     return dp[n]
    # return min(helper(n-1), helper(n-2))

    # Bottom-Up Approach
    # n = len(cost)
    # dp = [0] * n
    # dp[0], dp[1] = cost[0], cost[1]
    # for i in range(2, n):
    #     dp[i] = cost[i] + min(dp[i-1], dp[i-2])
    # return min(dp[n-1], dp[n-2])

    n = len(cost)
    cost1, cost2 = cost[0], cost[1]
    for i in range(2, n):
        cost1, cost2 = cost2, cost[i] + min(cost1, cost2)
    return min(cost1, cost2)
print("Problem 2: Min Cost Climbing Stairs")
print("cost = [10,15,20]:", minCostClimbingStairs([10,15,20]))
print("cost = [1,100,1,1,1,100,1,1,100,1]:", minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
print()
'''
Evaluate:
- Time Complexity: O(n)
- Space Complexity: O(1)
'''


'''
# Problem 3: Best Time to Buy and Sell Stock
Leetcode Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock
Solution: https://guides.codepath.org/compsci/Best-Time-to-Buy-and-Sell-Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
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
# Your function maxProfit is called as such:
# prices = [7,1,5,3,6,4]
# maxProfit(prices)
def maxProfit(prices: list[int]) -> int:
    # Bottom-Up Approach
    # n = len(prices)
    # dp = [0] * n
    # minPrice = prices[0]
    # for i in range(1, n):
    #     dp[i] = max(dp[i-1], prices[i] - minPrice)
    #     minPrice = min(minPrice, prices[i])
    # return dp[n-1]

    minPrice = prices[0]
    maxProfit = 0
    for price in prices:
        maxProfit = max(maxProfit, price - minPrice)
        minPrice = min(minPrice, price)
    return maxProfit
print("Problem 3: Best Time to Buy and Sell Stock")
print("prices = [7,1,5,3,6,4]:", maxProfit([7,1,5,3,6,4]))
print("prices = [7,6,4,3,1]:", maxProfit([7,6,4,3,1]))
print()
'''
Evaluate:
- Time Complexity: O(n)
- Space Complexity: O(1)
'''


'''
# (Bonus) Problem 4: Pascal's Triangle
Leetcode Link: https://leetcode.com/problems/pascals-triangle
Solution: https://guides.codepath.org/compsci/Pascal%27s-Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
'''
# Your function generate is called as such:
# generate(5)
def generate(numRows: int) -> list[list[int]]:
    # Top-Down Approach
    # dp = [[0] * (i+1) for i in range(numRows)]
    # def helper(i,j):
    #     if j == 0 or i == j:
    #         return 1
    #     if dp[i][j] == 0:
    #         dp[i][j] = helper(i-1,j-1) + helper(i-1,j)
    #     return dp[i][j]
    # for i in range(numRows):
    #     for j in range(i+1):
    #         dp[i][j] = helper(i,j)
    # return dp

    # Bottom-Up Approach
    dp = [[0] * (i+1) for i in range(numRows)]
    dp[0][0] = 1
    for i in range(1, numRows):
        dp[i][0], dp[i][i] = 1, 1
        for j in range(1, i):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    return dp

    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
print("(Bonus) Problem 4: Pascal's Triangle")
print("numRows = 5:", generate(5))
print("numRows = 1:", generate(1))
print()


'''
# (Bonus) Problem 5: Pascal's Triangle II
Leetcode Link: https://leetcode.com/problems/pascals-triangle-ii
Solution: https://guides.codepath.org/compsci/Pascal%27s-Triangle-II

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]
'''
# Your function getRow is called as such:
# getRow(5)
def getRow(rowIndex: int) -> list[int]:
    # Top-Down Approach
    # dp = [[0] * (i+1) for i in range(rowIndex+1)]
    # def helper(i,j):
    #     if j == 0 or i == j:
    #         return 1
    #     if dp[i][j] == 0:
    #         dp[i][j] = helper(i-1,j-1) + helper(i-1,j)
    #     return dp[i][j]
    # for i in range(rowIndex+1):
    #     for j in range(i+1):
    #         dp[i][j] = helper(i,j)
    # return dp[rowIndex]
        
    # Bottom-Up Approach
    dp = [0] * (rowIndex + 1)
    dp[0] = 1
    for i in range(1, rowIndex+1):
        for j in range(i, 0, -1):
            dp[j] = dp[j] + dp[j-1]
    return dp

    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
print("(Bonus) Problem 5: Pascal's Triangle II")
print("rowIndex = 3:", getRow(3))
print("rowIndex = 0:", getRow(0))
print("rowIndex = 1:", getRow(1))
print()