# 2018-04-29
# xinru
# file: 二叉搜索树的第k个节点

class TreeNode:
    def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot or k == 0:
            return None
        val_list = self.preorder(pRoot)
        if k > len(val_list) or k <= 0:
            return None
        return val_list[k - 1]

    def preorder(self, pRoot):
        val_list = []
        if not pRoot:
            return []
        if pRoot.left:
            val_list.extend(self.preorder(pRoot.left))
        val_list.extend([pRoot])
        if pRoot.right:
            val_list.extend(self.preorder(pRoot.right))
        return val_list

