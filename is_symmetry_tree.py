# 2018-04-29
# xinru
# file: 判断是否是对称的二叉树


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        return self.isSymmetrical_tree(pRoot.left, pRoot.right)
    def isSymmetrical_tree(self, p1, p2):
        if not p1 and not p2:
            return True
        if (p1 and not p2) or (p2 and not p1):
            return False
        if p1.val!=p2.val:
            return False
        return self.isSymmetrical_tree(p1.left, p2.right) and self.isSymmetrical_tree(p1.right, p2.left)