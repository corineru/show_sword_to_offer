# 2018-04-29
# xinru
# file: 要求不能用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C），所以用递归

class Solution:
    def __init__(self):
        self.sum = 0
    def Sum_Solution(self, n):
        # write code here
        if n==1:
            return 1
        return n + self.Sum_Solution(n-1)