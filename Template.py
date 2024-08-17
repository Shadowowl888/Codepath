'''
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
# Problem 1: 
Leetcode Link: 
Solution: 
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
print("Problem 1: ")
print()
'''
Evaluate:
- Time Complexity: O()
- Space Complexity: O()
'''


'''
# Problem 2: 
Leetcode Link: 
Solution: 
'''
print("Problem 2: ")
print()


'''
# Problem 3: 
Leetcode Link: 
Solution: 
'''
print("Problem 3: ")
print()


'''
# (Bonus) Problem 4: 
Leetcode Link: 
Solution: 
'''
print("(Bonus) Problem 4: ")
print()


'''
# (Bonus) Problem 5: 
Leetcode Link: 
Solution: 
'''
print("(Bonus) Problem 5: ")
print()


# Question 1

# Question 2
def quiz(i):
    if i > 1:
        quiz(i / 2)
        quiz(i / 2)
    print("*")
print("Question 2")
quiz(5)

# Question 3
def test_a(n):
    print(f"({n} )")
    if n > 0:
        test_a(n - 2)
print("Question 3")
test_a(4)

# Question 4
def test_b(n):
    if n > 0:
        test_b(n - 2)
        print(f"({n} )")
print("Question 4")
test_b(4)

# Question 5
def isPowerOfThree(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 3 != 0:
        return False
    return isPowerOfThree(n //3)
print("n = 27:", isPowerOfThree(27))
print("n = 0:", isPowerOfThree(0))
print("n = -1:", isPowerOfThree(-1))
print("n = 9:", isPowerOfThree(9))
print("n = 1:", isPowerOfThree(1))
print("n = 45:", isPowerOfThree(45))

# Question 6
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
print("n = 2:", fib(2))
print("n = 3:", fib(3))
print("n = 4:", fib(4))