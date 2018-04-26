# 2018-04-26
# xinru
# file: 数组里出现一次的数字


class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        only_one = []
        for i in array:
            if array.count(i)==1:
                only_one.append(i)
        return only_one