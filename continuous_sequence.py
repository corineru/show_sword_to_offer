# 2018-04-26
# xinru
# file: 和为S的连续正数序列


class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum < 3:
            return []
        res = []
        for i in range(1, tsum):
            j = i
            t = 0
            while (t < tsum):
                t = t + j
                j += 1
                if t == tsum:
                    res.append(range(i, j))
        return res
