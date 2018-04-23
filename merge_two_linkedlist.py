# 2018-04-23
# xinru
# file:  合并两个排序的链表

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1 and pHead2:
            return pHead2
        if not pHead2 and pHead1:
            return pHead1
        if not pHead1 and not pHead2:
            return None
        if pHead1.val < pHead2.val:
            pHead1.next = self.Merge(pHead2, pHead1.next)
            return pHead1
        else:
            pHead2.next = self.Merge(pHead1, pHead2.next)
            return pHead2