# 2018-04-29
# xinru
# file: 孩子们的游戏，围一圈报数，剩最后一个人

class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if not n or not m:
            return -1
        res = [i for i in range(n)]
        i = 0
        while(len(res)>1):
            i = (m+i-1)%(len(res))
            res.pop(i)
        return res[0]