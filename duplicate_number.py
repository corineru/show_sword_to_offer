# 2018-04-29
# xinru
# file: 数组中重复的数字

class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        for i in numbers:
            if numbers.count(i)>1:
                duplication[0]=i
                return True
        return False