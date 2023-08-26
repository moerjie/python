'''
Author: Moerjie
Data: Today
LastEditTime: 2023-08-26 17:06:46
FilePath: \python\1822.数组元素积的符号.py
'''
#
# @lc app=leetcode.cn id=1822 lang=python3
#
# [1822] 数组元素积的符号
#

# @lc code=start


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        '''
        res = 1
        for i in range(len(nums)):
            res *= nums[i]
        if res > 0:
            return 1
        elif res < 0:
            return -1
        else:
            return 0'''

        sign = 1
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                sign = -sign
        return sign


# @lc code=end
