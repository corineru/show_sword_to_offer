# 2018-04-29
# xinru
# file: 将一个字符串转换成一个整数

class Solution:
    def StrToInt(self, s):
        # write code here
        l = len(s)
        sign = 1
        a = 0
        for i in range(l):
            if l==0:
                return 0
            if s[i]!="+" and s[i]!="-" and s[i] not in "0123456789":
                return 0
            if s[i] == '+' and i==0:
                continue
            if s[i]== '+' and i!=0:
                return 0
            if s[i] == '-' and i==0:
                sign = -1
                continue
            if s[i] == '-' and i!=0:
                return 0
            if s[i]=='0' and l>1:
                return 0
            if s[i] == '0' and i==1 and l>=3:
                return 0
            a = a*10 + int(s[i])
        return sign*(a)