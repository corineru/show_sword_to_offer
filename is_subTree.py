# 2018-04-23
# xinru
# file:  判断是否是数的子结构


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        if self.is_subtree(pRoot1, pRoot2):
            return True
        return self.is_subtree(pRoot1.left, pRoot2) or self.is_subtree(pRoot1.right, pRoot2)

    def is_subtree(self, pRoot1, pRoot2):
        if not pRoot2:
            return True
        if not pRoot1 or pRoot1.val != pRoot2.val:
            return False
        return self.is_subtree(pRoot1.left, pRoot2.left) and self.is_subtree(pRoot1.right, pRoot2.right)