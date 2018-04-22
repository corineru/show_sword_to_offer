# 2018-04-22
# xinru
# file: fibonacci数列


class Solution:
    def Fibonacci(self, n):
        if n==0:
            return 0
        elif n==1:
            return 1
        a, b= 0, 1
        for i in xrange(2, n+1):
            a, b = b, a+b
        return b