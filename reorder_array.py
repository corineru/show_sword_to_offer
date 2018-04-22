# 2018-04-22
# xinru
# file: 重新调整数组，奇数放前半部分，偶数放后半部分，并保持稳定

class solution:
    def reOrderArray(self, array):
        # write code here
        ordered_array = []
        for i in array:
            if i % 2 != 0:
                ordered_array.append(i)
        for i in array:
            if i % 2 == 0:
                ordered_array.append(i)
        return ordered_array