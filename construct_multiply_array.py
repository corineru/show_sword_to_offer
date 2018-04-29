# 2018-04-29
# xinru
# file: 构建乘积数组

class Solution:
    def multiply(self, A):
        # write code here
        if not A:
            return None
        B = []
        for i in range(len(A)):
            B.append(1)
            for j in range(i):
                B[i] = B[i]*A[j]
            for j in range(i+1,len(A)):
                B[i] = B[i]*A[j]
        return B