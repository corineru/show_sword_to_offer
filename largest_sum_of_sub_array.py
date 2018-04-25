# 2018-04-25
# xinru
# file:  连续子数组的最大和

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        max_sum = -0xffffff
        temp_sum = -0xffffff

        for i in array:
            if temp_sum < 0:
                temp_sum = i
                if temp_sum > max_sum:
                    max_sum = temp_sum
            else:
                temp_sum += i
                if temp_sum > max_sum:
                    max_sum = temp_sum
        return max_sum