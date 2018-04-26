# 2018-04-26
# xinru
# file: 左旋字符串


class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if not s or n<0 or n>len(s):
            return ""
        if n==0:
            return s
        return ''.join(s[n:] + s[:n])