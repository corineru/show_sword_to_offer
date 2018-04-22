# 2018-04-22
# xinru
# file: 求链表的倒数第k个节点

class solution:
    def FindKthToTail(self，head, k):
        # write code here
        node_list = []
        while (head):
            node_list.append(head)
            head = head.next
        if k > len(node_list) or k == 0:
            return None
        return node_list[-k]