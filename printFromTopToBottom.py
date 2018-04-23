# 2018-04-23
# xinru
# file:  按行打印二叉树

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        val_list = []
        node_list = []
        val_list.append(root.val)
        if root.left:
            node_list.append(root.left)
        if root.right:
            node_list.append(root.right)

        #对每行进行循环，知道全部都是None
        while(node_list):
            new_node_list = []
            for node in node_list:
                val_list.append(node.val)
                if node.left:
                    new_node_list.append(node.left)
                if node.right:
                    new_node_list.append(node.right)
            node_list = new_node_list
        return val_list