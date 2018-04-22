# 2018-04-22
# xinru
# file: 二维数组中的查找


def Find(self, target, array):
    # write code here
    for i in array:
        if target in i:
            return True
    return False