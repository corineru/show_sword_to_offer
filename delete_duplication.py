# 2018-04-29
# xinru
# file: 删除重复链表节点

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        p = pHead.next
        prev = pHead
        p_new_head = pHead
        while p:
            if p==p_new_head.next and p.val == p_new_head.val:
                while p.next and p.val == p.next.val:
                    p = p.next
                p = p.next
                p_new_head = p
                prev = p
                if p and p.next:
                    p = p.next
            else:
                if p.next and p.next.val==p.val:
                    while p.next and p.val == p.next.val:
                        p = p.next
                    p = p.next
                    prev.next = p
                elif not p.next:
                    return p_new_head
                else:
                    prev = p
                    p = p.next
        return p_new_head