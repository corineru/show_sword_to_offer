# 2018-04-29
# xinru
# file: 机器人的运动范围

class Solution:
    def __init__(self):
        self.vis = {}

    def movingCount(self, threshold, rows, cols):
        # write code here
        return self.moving(threshold, rows, cols, 0, 0)

    def moving(self, threshold, rows, cols, row, col):
        if row / 10 + row % 10 + col / 10 + col % 10 > threshold:
            return 0
        if row >= rows or col >= cols or row < 0 or col < 0:
            return 0
        if (row, col) in self.vis:
            return 0
        self.vis[(row, col)] = 1
        return 1 + self.moving(threshold, rows, cols, row + 1, col) + self.moving(threshold, rows, cols, row - 1,
                                                                                  col) + self.moving(threshold, rows,
                                                                                                     cols, row,
                                                                                                     col + 1) + self.moving(
            threshold, rows, cols, row, col - 1)
