# 2018-04-22
# xinru
# file: 从尾到头打印链表


def printListFromTailToHead(self, listNode):
    value_list = []
    while (listNode):
        value_list.append(listNode.val)
        listNode = listNode.next
    if not value_list:
        return []
    value_list.reverse()
    return value_list