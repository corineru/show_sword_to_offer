# 2018-04-25
# xinru
# file:  数组中出现超过一半的数字

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        for i in numbers:
            if numbers.count(i)>len(numbers)/2:
                return i
        return 0