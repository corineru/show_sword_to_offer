# 2018-04-22
# xinru
# file: 替换空格


class solution:
    def replaceSpace(self, s):
    s_new = []
    for i in s:
        if i == ' ':
            s_new.append('%20')
        else:
            s_new.append(i)
    return ''.join(s_new)
