from typing import List

'''
# Warmup Problem: Fibonacci Number
Leetcode Link: https://leetcode.com/problems/fibonacci-number
Solution: https://guides.codepath.org/compsci/fibonacci-number

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
def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
print("Warmup Problem: Fibonacci Number")
print("n = 2:", fib(2))
print("n = 3:", fib(3))
print("n = 4:", fib(4))
print()


'''
# Warmup Problem: Find the Town Judge
Leetcode Link: https://leetcode.com/problems/find-the-town-judge
Solution: https://guides.codepath.org/compsci/find-the-town-judge

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
def findJudge(n: int, trust: List[List[int]]) -> int:
    trusted = [0] * (n + 1)
    for person1, person2 in trust:
        trusted[person1] -= 1
        trusted[person2] += 1
    for i in range(1, len(trusted)):
        if trusted[i] == n-1:
            return i
    return -1
print("Warmup Problem: Find the Town Judge")
print("n = 2, trust = [[1,2]]:", findJudge(2, [[1,2]]))
print("n = 3, trust = [[1,3],[2,3]]:", findJudge(3, [[1,3],[2,3]]))
print("n = 3, trust = [[1,3],[2,3],[3,1]]:", findJudge(3, [[1,3],[2,3],[3,1]]))
print()