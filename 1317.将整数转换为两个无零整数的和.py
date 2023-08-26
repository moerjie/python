'''
Author: Moerjie
Data: Today
LastEditTime: 2023-08-26 11:02:12
FilePath: \python\1317.将整数转换为两个无零整数的和.py
'''
#
# @lc app=leetcode.cn id=1317 lang=python3
#
# [1317] 将整数转换为两个无零整数的和
#

# @lc code=start


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for a in range(1, n):
            b = n-a
            if '0' not in str(a) + str(b):
                return [a, b]
# @lc code=end
