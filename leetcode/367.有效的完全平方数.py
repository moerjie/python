'''
Author: Moerjie
Data: Today
LastEditTime: 2023-08-24 18:56:07
FilePath: \python\367.有效的完全平方数.py
'''
#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i=1
        squ=1
        while squ<=num:
            if squ==num:
                return True
            i+=1
            squ=i*i
        return False

# @lc code=end

