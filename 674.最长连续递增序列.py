'''
Author: Moerjie
Data: Today
LastEditTime: 2023-08-25 21:43:39
FilePath: \python\674.最长连续递增序列.py
'''
#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#

# @lc code=start


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        count = 0
        result = 1
        for i in range(len(nums)):
            if nums[i-1] < nums[i]:
                count += 1
            else:
                count = 1
            if count > result:
                result = count
        return result

# @lc code=end
