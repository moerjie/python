'''
Author: Moerjie
Data: Today
LastEditTime: 2023-08-24 10:31:27
FilePath: \python\258.各位相加.py
'''
#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#

# @lc code=start


class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9
# @lc code=end
