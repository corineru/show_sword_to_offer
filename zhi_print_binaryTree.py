# 2018-04-29
# xinru
# file: 按之字形打印二叉树

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        node_list = [pRoot]
        line_number = 0
        all_list = []
        while node_list:
            new_node_list = []
            val_list = []
            for node in node_list:
                if node.left:
                    new_node_list.append(node.left)
                if node.right:
                    new_node_list.append(node.right)
            if line_number%2==0:
                for node in node_list:
                    val_list.append(node.val)
            else:
                for node in node_list[::-1]:
                    val_list.append(node.val)
            all_list.append(val_list)
            node_list = new_node_list
            line_number += 1
        return all_list