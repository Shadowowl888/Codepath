from typing import List
import heapq as heapq
from collections import deque

'''
https://replit.com/@skyepersona1/Pod-30
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
# Problem 1: Valid Parenthesis
Leetcode Link: https://leetcode.com/problems/valid-parentheses
Solution: https://guides.codepath.org/compsci/valid-parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets. Open brackets must be closed in the correct order. Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[ ]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
'''

'''
Understand:
- What if input string is empty?
- What is the data type of the output?
- Input string = "[}" -> false
- What if there are random characters in the string? -> no random characters?

Match:
- Stack

Plan:
- Pop when there's close a bracket and make sure that the top of the stack's element is the same bracket type as the current cahracter of the string
    - If it's the same type -> pop
    - If it's different type -> return false
- Push open bracket to stack

Implement:
'''
def isValid(s: str) -> bool:
    stack = []
    closeToOpen = {
        ")" : "(",
        "]" : "[",
        "}" : "{"
    }
    for c in s:
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False

    # stack = []
    # for char in s:      
    #     if char == "(" or char == "[" or char == "{":
    #         stack.append(char)
    #     elif len(stack)  != 0 and char == ")" and stack[-1] == "(":
    #         stack.pop()
    #     elif len(stack)  != 0 and char == "}" and stack[-1] == "{":
    #         stack.pop()
    #     elif len(stack) != 0 and char == "]" and stack[-1] == "[":
    #         stack.pop()
    #     else:
    #         return False
    # if len(stack) == 0:
    #     return True 
    # else:
    #     return False
print("Problem 1: Valid Parenthesis")
print('s = "()":', isValid("()"))
print('s = "()[ ]{}":', isValid("()[]{}"))
print('s = "(]":', isValid("(]"))
print()


'''
# Problem 2: Kth Largest Element in a Stream
Leetcode Link: https://leetcode.com/problems/kth-largest-element-in-a-stream
Solution: https://guides.codepath.org/compsci/kth-largest-element-in-a-stream

Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.
Implement KthLargest class:
- KthLargest(int k, int[] nums): Initializes the object with the integer k and the stream of integers nums.
- int add(int val): Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

Example 1:
Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
'''

'''
Understand:
- What would happen if k is larger than the length of the array? -> return None
- What if the array is empty? -> return 0
- What if k is negative or 0? -> return None
- What if the array has only one element? -> check if k == 1 else None
'''
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
    def __str__(self):
        return str(self.minHeap)
print("Problem 2: Kth Largest Element in a Stream")
kthLargest = KthLargest(3, [4,5,8,2])
print("MinHeap:", kthLargest)
print("kthLargest.add(3):", kthLargest.add(3));   # return 4
print("MinHeap:", kthLargest)
print("kthLargest.add(5):", kthLargest.add(5));   # return 5
print("MinHeap:", kthLargest)
print("kthLargest.add(10):", kthLargest.add(10)); # return 5
print("MinHeap:", kthLargest)
print("kthLargest.add(9):", kthLargest.add(9));   # return 8
print("MinHeap:", kthLargest)
print("kthLargest.add(4):", kthLargest.add(4));   # return 8
print("MinHeap:", kthLargest)
print()


'''
# Problem 3: Number of Recent Calls
Leetcode Link: https://leetcode.com/problems/number-of-recent-calls
Solution: https://guides.codepath.org/compsci/number-of-recent-calls/

You have a RecentCounter class which counts the number of recent requests within a certain time frame.
Implement the RecentCounter class:
- RecentCounter() Initializes the counter with zero recent requests.
- int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

Example 1:
Input
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output
[null, 1, 2, 3, 3]

Explanation
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3
'''
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
class RecentCounter:
    def __init__(self):
        self.queue = deque()
    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] + 3000 < t:
            self.queue.popleft()
        return len(self.queue)
    def __str__(self):
        return str(self.queue)
print("Problem 3: Number of Recent Calls")
recentCounter = RecentCounter()
print("Queue:", recentCounter)
print("recentCounter.ping(1):", recentCounter.ping(1))       # requests = [1], range is [-2999,1], return 1
print("Queue:", recentCounter)
print("recentCounter.ping(100):", recentCounter.ping(100))   # requests = [1, 100], range is [-2900,100], return 2
print("Queue:", recentCounter)
print("recentCounter.ping(3001):", recentCounter.ping(3001)) # requests = [1, 100, 3001], range is [1,3001], return 3
print("Queue:", recentCounter)
print("recentCounter.ping(3002):", recentCounter.ping(3002)) # requests = [1, 100, 3001, 3002], range is [2,3002], return 3
print("Queue:", recentCounter)
print()


'''
# (Bonus) Problem 4: Min Stack
Leetcode Link: https://leetcode.com/problems/min-stack
Solution: https://guides.codepath.org/compsci/Min-Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Implement the MinStack class:
- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack. You must implement a solution with O(1) time complexity for each function.

Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
'''
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.minStack[-1]
    def __str__(self):
        return f"Stack:{self.stack}, MinStack={self.minStack})"
print("(Bonus) Problem 4: Min Stack")
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print("MinStack:", minStack)
print("minStack.getMin():", minStack.getMin()) # return -3
minStack.pop()
print("MinStack:", minStack)
print("minStack.top():", minStack.top())       # return 0
print("minStack.getMin():", minStack.getMin()) # return -2
print()


'''
# (Bonus) Problem 5: Implement Queue Using Stacks
Leetcode Link: https://leetcode.com/problems/implement-queue-using-stacks
Solution: https://guides.codepath.org/compsci/implement-queue-using-stacks/

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
Implement the MyQueue class:
- void push(int x) Pushes element x to the back of the queue.
- int pop() Removes the element from the front of the queue and returns it.
- int peek() Returns the element at the front of the queue.
- boolean empty() Returns true if the queue is empty, false otherwise.
Notes:
- You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
- Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

Example 1:
Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
'''
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
class MyQueue:
    def __init__(self):
        self.addStack, self.popStack = [], []
    def push(self, x: int) -> None:
        self.addStack.append(x)
    def pop(self) -> int:
        if not self.popStack:
            while self.addStack:
                self.popStack.append(self.addStack.pop())
        return self.popStack.pop()
    def peek(self) -> int:
        if not self.popStack:
            while self.addStack:
                self.popStack.append(self.addStack.pop())
        return self.popStack[-1]
    def empty(self) -> bool:
        return not self.addStack and not self.popStack
    def __str__(self):
        return f"Add Stack: {self.addStack}, Pop Stack: {self.popStack}"
print("(Bonus) Problem 5: Implement Queue Using Stacks")
myQueue = MyQueue()
myQueue.push(1) # queue is: [1]
myQueue.push(2) # queue is: [1, 2] (leftmost is front of the queue)
print("Queue:", myQueue)
print("myQueue.peek():", myQueue.peek())   # return 1
print("myQueue.pop():", myQueue.pop())     # return 1, queue is [2]
print("Queue:", myQueue)
print("myQueue.empty():", myQueue.empty()) # return false
print("Queue:", myQueue)
print()