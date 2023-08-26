'''
Author: Moerjie
Data: Today
LastEditTime: 2023-08-26 17:11:41
FilePath: \python\1929.数组串联.py
'''
#
# @lc app=leetcode.cn id=1929 lang=python3
#
# [1929] 数组串联
#

# @lc code=start


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        return nums
# @lc code=end
