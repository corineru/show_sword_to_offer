# 2018-04-29
# xinru
# file:序列化和反序列化二叉树

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Serialize(self, root):
        # write code here
        if not root:
            return []
        node_list = [root]
        node_list_all = [node_list]
        while (1):
            new_node_list = []
            for node in node_list:
                if not node:
                    new_node_list.extend([None, None])
                    continue
                if not node.left:
                    new_node_list.append(None)
                else:
                    new_node_list.append(node.left)
                if not node.right:
                    new_node_list.append(None)
                else:
                    new_node_list.append(node.right)
            node_list = new_node_list
            number = 0
            for node in node_list:
                if node == None:
                    number += 1
            if number == len(node_list):
                break
            node_list_all.append(node_list)
        return node_list_all

    def Deserialize(self, s):
        # write code here
        if s == []:
            return None
        for i in range(len(s) - 1):
            for j in range(len(s[i])):
                if s[i][j]:
                    s[i][j].left = s[i + 1][2 * j]
                    s[i][j].righy = s[i + 1][2 * j + 1]
        return s[0][0]