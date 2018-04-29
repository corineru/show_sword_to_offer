# 2018-04-29
# xinru
# file: 滑动窗口的最大值

class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if not num:
            return None
        if size> len(num) or size==0:
            return []
        max_list = []
        for i in range(len(num)-size+1):
            max_list.append(max(num[i:i+size]))
        return max_list