'''
Author: Moerjie
Data: Do not edit
LastEditTime: 2023-08-29 17:38:58
FilePath: \python\905.按奇偶排序数组.py
'''
#
# @lc app=leetcode.cn id=905 lang=python3
#
# [905] 按奇偶排序数组
#

# @lc code=start


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return list(num for num in nums if num % 2 == 0)+list(num for num in nums if num % 2 == 1)
# @lc code=end
