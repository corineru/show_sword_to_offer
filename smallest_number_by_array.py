# 2018-04-25
# xinru
# file:  把数组排成最小的数

class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ""
        lmd = lambda n1, n2 :int(str(n1)+str(n2)) - int(str(n2)+str(n1))
        array = sorted(numbers, cmp = lmd)
        return int(''.join([str(j) for j in array]))