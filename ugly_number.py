# 2018-04-25
# xinru
# file:  丑数

class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index<=0:
            return 0
        if index==1:
            return 1
        f2, f3, f5=0,0,0
        ugly = [1]
        for i in range(index-1):
            number = min([ugly[f2]*2, ugly[f3]*3, ugly[f5]*5])
            ugly.append(number)
            if number==ugly[f2]*2:
                f2+=1
            if number==ugly[f3]*3:
                f3+=1
            if number==ugly[f5]*5:
                f5+=1
        return number