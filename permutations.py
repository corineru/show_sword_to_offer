# 2018-04-25
# xinru
# file:  字符串的排列

import itertools
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        else:
            return sorted(set(list(map(''.join, itertools.permutations(ss)))))