'''
Author: Moerjie
Data: Today
LastEditTime: 2023-08-25 21:36:15
FilePath: \python\643.子数组最大平均数-i.py
'''
#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#

# @lc code=start


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxTotal = total = sum(nums[:k])
        n = len(nums)

        for i in range(k, n):
            total = total+nums[i]-nums[i-k]
            maxTotal = max(maxTotal, total)

        return maxTotal/k
# @lc code=end
