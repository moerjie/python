'''
Author: Moerjie
Data: Today
LastEditTime: 2023-08-24 10:48:15
FilePath: \python\292.nim-游戏.py
'''
#
# @lc app=leetcode.cn id=292 lang=python3
#
# [292] Nim 游戏
#

# @lc code=start
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n%4!=0
# @lc code=end

