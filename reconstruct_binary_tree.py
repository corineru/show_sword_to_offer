# 2018-04-22
# xinru
# file: 根据前序和中序遍历的结果重建二叉树


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class solution:

    def reConstructBinaryTree(self, pre, tin):
        if len(pre)==0:
            return None
        if len(pre)==1:
            return TreeNode(pre[0])
        head = TreeNode(pre[0])
        head.left = self.reConstructBinaryTree(pre[1:tin.index(pre[0])+1] ,tin[:tin.index(pre[0])])
        head.right = self.reConstructBinaryTree(pre[tin.index(pre[0])+1:], tin[tin.index(pre[0]) +1:])
        return head