'''
Author: Moerjie
Data: Today
LastEditTime: 2023-08-26 11:24:23
FilePath: \python\1491.去掉最低工资和最高工资后的工资平均值.py
'''
#
# @lc app=leetcode.cn id=1491 lang=python3
#
# [1491] 去掉最低工资和最高工资后的工资平均值
#

# @lc code=start


class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary)
        salary.sort()
        salary.pop(n-1)
        salary.pop(0)
        return sum(salary)/(n-2)
# @lc code=end
