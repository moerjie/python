'''
Author: Moerjie
Data: Today
LastEditTime: 2023-08-24 10:23:25
FilePath: \python\231.2-的幂.py
'''
#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2 的幂
#

# @lc code=start


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n == 1:
            return True
        return (n & (n-1)) == 0
# @lc code=end
