'''
Author: Moerjie
Data: Today
LastEditTime: 2023-08-26 11:18:40
FilePath: \python\1346.检查整数及其两倍数是否存在.py
'''
#
# @lc app=leetcode.cn id=1346 lang=python3
#
# [1346] 检查整数及其两倍数是否存在
#

# @lc code=start


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        i = j = 0
        n = len(arr)
        for i in range(n):
            for j in range(n):
                if i != j and arr[i] == 2*arr[j]:
                    return True
        return False
# @lc code=end
