# 2018-04-25
# xinru
# file: 是否是平衡树

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        def Depth(p):
            if not p:
                return 0
            if not p.left and not p.right:
                return 1
            return max(Depth(p.left), Depth(p.right)) + 1
        if not pRoot:
            return True
        if not pRoot.left and not pRoot.right:
            return True
        if abs(Depth(pRoot.left)-Depth(pRoot.right))>1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)