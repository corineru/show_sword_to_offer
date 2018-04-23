# 2018-04-23
# xinru
# file: 二叉树中和为某一值的路径


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            # 注意返回的是空数组
            return []
        if root and not root.left and not root.right and root.val == expectNumber:
            return [[root.val]]
        # left和right返回的均是二维数组
        left = self.FindPath(root.left, expectNumber-root.val)
        right = self.FindPath(root.right, expectNumber-root.val)
        res = []
        for i in left+right:
            # i是一维数组
            res.append([root.val]+i)
        return res