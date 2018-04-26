# 2018-04-26
# xinru
# file: 反转单词顺序

class Solution:
    def ReverseSentence(self, s):
        # write code here
        word_list = s.split(" ")
        word_list.reverse()
        return " ".join(word_list)
