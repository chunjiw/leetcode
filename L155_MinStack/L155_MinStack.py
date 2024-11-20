# 155. Min Stack
# DescriptionHintsSubmissionsDiscussSolution
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.nums.append(x)
        if self.stack and self.stack[-1] < x:
            self.stack.append(self.stack[-1])
        else:
            self.stack.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        if not self.nums:
            return
        self.nums.pop()
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if not self.nums:
            return
        return self.nums[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if not self.nums:
            return
        return self.stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
