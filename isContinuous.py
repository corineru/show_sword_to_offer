# 2018-04-26
# xinru
# file: 判断是否是顺子

class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers or len(numbers)!=5:
            return False
        numbers = sorted(numbers)
        difference = 0
        for i in range(len(numbers)-1):
            if numbers[i]==0:
                continue
            else:
                if numbers.count(numbers[i])>1:
                    return False
                difference +=numbers[i+1]-numbers[i]
                if difference>4:
                    return False
        return True