'''
Author: Moerjie
Data: Today
LastEditTime: 2023-08-26 17:16:41
FilePath: \python\1984.学生分数的最小差值.py
'''
#
# @lc app=leetcode.cn id=1984 lang=python3
#
# [1984] 学生分数的最小差值
#

# @lc code=start


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        return min(nums[i+k-1]-nums[i] for i in range(len(nums)-k+1))
# @lc code=end
