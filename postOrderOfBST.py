# 2018-04-23
# xinru
# file:  顺时针打印矩阵

class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        length = len(sequence)
        if length==0:
            return False
        if length==1 or length==2:
            return True
        for i in range(length-1):
            if sequence[i]>sequence[-1]:
                break
        if i==length-2:
            return True
        for j in range(i+1, length-1):
            if sequence[j]<sequence[-1]:
                return False
        return self.VerifySquenceOfBST(sequence[:i+1]) and self.VerifySquenceOfBST(sequence[i+1:-1])