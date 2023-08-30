'''
Author: Moerjie
Data: Today
LastEditTime: 2023-08-26 16:56:00
FilePath: \python\1550.存在连续三个奇数的数组.py
'''
#
# @lc app=leetcode.cn id=1550 lang=python3
#
# [1550] 存在连续三个奇数的数组
#

# @lc code=start


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr)-2):
            if arr[i] % 2 != 0 and arr[i+1] % 2 != 0 and arr[i+2] % 2 != 0:
                return True
        return False
# @lc code=end
