# 2018-04-23
# xinru
# file:  有min函数的栈

class Solution:
    def __init__(self):
        self.stack =[]
    def push(self, node):
        # write code here
        self.stack.append(node)
    def pop(self):
        # write code here
        self.stack.pop()
    def top(self):
        # write code here
        return self.stack[-1]
    def min(self):
        # write code here
        return min(self.stack)