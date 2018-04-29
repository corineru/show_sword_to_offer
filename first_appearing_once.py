# 2018-04-29
# xinru
# file: 字符流中第一个不重复的字符

class Solution:
    # 返回对应char
    l = ''

    def FirstAppearingOnce(self):
        # write code here
        first_letter = '#'
        moreThanOnelist = []
        for i in range(len(self.l)):
            letter = self.l[i]
            if letter in moreThanOnelist:
                continue
            if self.l.count(letter) > 1:
                moreThanOnelist.append(letter)
                continue
            if self.l.count(letter) == 1:
                first_letter = letter
                break
        return first_letter

    def Insert(self, char):
        # write code here
        self.l = self.l + char