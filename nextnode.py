# 2018-04-29
# xinru
# file: 中序遍历的下一个节点

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return None
        #如果存在右节点，就去找右节点的左节点的左节点的左节点.....
        if pNode.right:
            nextNode = pNode.right
            while nextNode.left:
                nextNode = nextNode.left
            return nextNode
        #如果不存在，就去找作为左节点的父节点
        while pNode.next:
            tmp = pNode.next
            if tmp.left == pNode:
                return tmp
        return None