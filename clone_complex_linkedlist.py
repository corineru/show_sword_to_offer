# 2018-04-25
# xinru
# file: 复杂链表的复制

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        head = pHead
        new_head = None
        p_head = None

        random_dict = {}
        while (head):
            Node = RandomListNode(head.label)
            Node.random = head.random
            random_dict[head] = Node
            head = head.next

            if new_head:
                new_head.next = Node
                new_head = new_head.next
            else:
                new_head = Node
                p_head = Node
        new_head = p_head
        while (new_head):
            if new_head.random:
                new_head.random = random_dict[new_head.random]
            new_head = new_head.next
        return p_head