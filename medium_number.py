# 2018-04-29
# xinru
# file: 数据流的中位数

class Solution:
    def __init__(self):
        self.data=[]
    def Insert(self, num):
        # write code here
        self.data.append(num)
        self.data.sort()
    def GetMedian(self, data):
        # write code here
        N = len(self.data)
        if not N:
            return None
        if(N%2==0):
            return (self.data[N/2]+self.data[N/2-1])/2.0
        else:
            return self.data[N/2]