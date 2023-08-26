'''
Author: Moerjie
Data: Today
LastEditTime: 2023-08-26 11:07:47
FilePath: \python\1323.6-和-9-组成的最大数字.py
'''
#
# @lc app=leetcode.cn id=1323 lang=python3
#
# [1323] 6 和 9 组成的最大数字
#

# @lc code=start


class Solution:
    def maximum69Number(self, num: int) -> int:
        return int(str(num).replace('6', '9', 1))
# @lc code=end
