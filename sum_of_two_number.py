# 2018-04-26
# xinru
# file: 和为S的两个数字

class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        smallest = 0xffffff
        final = []
        if not array or len(array)==1:
            return []
        for i in range(len(array)-1):
            if tsum-array[i] in array[i+1:]:
                produit = array[i] * (tsum-array[i])
                if produit<smallest:
                    smallest = produit
                    final = [array[i], tsum-array[i]]
        return final