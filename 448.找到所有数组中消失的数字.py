'''
Author: Moerjie
Data: Today
LastEditTime: 2023-08-24 21:01:28
FilePath: \python\448.找到所有数组中消失的数字.py
'''
#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        count = [0]*(len(nums)+1)
        for num in nums:
            count[num] += 1
        res = []
        for num in range(1, len(nums)+1):
            if count[num] == 0:
                res.append(num)
        return res

# @lc code=end
