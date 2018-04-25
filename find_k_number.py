# 2018-04-25
# xinru
# file:  找到最小的k个数

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput:
            return []
        if k>len(tinput):
            return []
        tinput.sort()
        return tinput[:k]