# 2018-04-29
# xinru
# file: 链表中环的入口

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return None
        pfast = pHead.next.next
        pslow = pHead.next
        while(pfast!=pslow):
            pfast = pfast.next.next
            pslow = pslow.next
        p = pHead
        while(p!=pslow):
            p = p.next
            pslow = pslow.next
        return p