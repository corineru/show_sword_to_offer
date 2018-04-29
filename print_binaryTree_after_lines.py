# 2018-04-29
# xinru
# file: 把二叉树打印成多行

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        node_list = [pRoot]
        all_list = []
        while node_list:
            new_node_list = []
            val_list = []
            for node in node_list:
                val_list.append(node.val)
                if node.left:
                    new_node_list.append(node.left)
                if node.right:
                    new_node_list.append(node.right)
            all_list.append(val_list)
            node_list = new_node_list
        return all_list