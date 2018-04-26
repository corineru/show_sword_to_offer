# 2018-04-26
# xinru
# file: 二叉搜索树与双向链表


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree

        def leftlast(p):
            left = p.left
            if left:
                while (left.right):
                    left = left.right
            return left

        def rightfirst(p):
            right = p.right
            if right:
                while (right.left):
                    right = right.left
            return right

        self.Convert(pRootOfTree.left)
        self.Convert(pRootOfTree.right)
        left = leftlast(pRootOfTree)
        pRootOfTree.left = left
        if left:
            left.right = pRootOfTree
        right = rightfirst(pRootOfTree)
        pRootOfTree.right = right
        if right:
            right.left = pRootOfTree
        pHead = pRootOfTree
        while (pHead.left):
            pHead = pHead.left
        return pHead