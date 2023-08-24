'''
Author: Moerjie
Data: Today
LastEditTime: 2023-08-24 10:50:23
FilePath: \python\326.3-的幂.py
'''
#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] 3 的幂
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        while n>0 and n%3==0:
            n/=3
        return n==1
# @lc code=end

