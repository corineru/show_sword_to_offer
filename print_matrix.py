# 2018-04-23
# xinru
# file:  顺时针打印矩阵


# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        list = []
        cycle = min(m,n)/ 2
        if m==1:
            list = [matrix[0][j] for j in xrange(0,n)]
            return list
        if n ==1:
            list = [matrix[i][0] for i in xrange(0,m)]
            return list
        for t in xrange(cycle):
        # First line
            for j in xrange(t, n - t - 1):
                list.append(matrix[t][j])
        # First colome
            for i in xrange(t, m - t - 1):
                list.append(matrix[i][n - t - 1])
        # Second line
            for j in xrange(n - t - 1,t, -1):
                list.append(matrix[m - t - 1][j])
        # Second colome
            for i in xrange(m - t - 1,t, -1):
                list.append(matrix[i][t])
        if min(m, n) % 2 != 0:
            if min(m, n) == m and m != n:
                for j in xrange(m / 2, n - m / 2):
                    list.append(matrix[m / 2][j])
            if min(m, n) == n:
                for i in xrange(n / 2, m - n / 2):
                    list.append(matrix[i][n / 2])
        return list

