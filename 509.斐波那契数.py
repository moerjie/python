'''
Author: Moerjie
Data: Today
LastEditTime: 2023-08-24 21:25:02
FilePath: \python\509.斐波那契数.py
'''
#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start


class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        dp_i_1 = 1
        dp_i_2 = 0
        for i in range(2, n+1):
            dp_i = dp_i_1+dp_i_2
            dp_i_2 = dp_i_1
            dp_i_1 = dp_i
        return dp_i_1
# @lc code=end
