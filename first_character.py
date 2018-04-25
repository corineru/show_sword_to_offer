# 2018-04-25
# xinru
# file:  第一个只出现一次的字符

class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        s_list = list(s)
        for i in s_list:
            if s_list.count(i)==1:
                return s_list.index(i)
        return -1