# 2018-04-23
# xinru
# file:  栈的压入、弹出序列

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack=[]
    def IsPopOrder(self, pushV, popV):
        # write code here
        i = 0
        for elem in pushV:
            if elem != popV[i]:
                self.stack.append(elem)
            else:
                i += 1
        while(self.stack):
            if self.stack.pop()!=popV[i]:
                return False
            i += 1
        if not self.stack:
            return True
        return False