'''
Author: Moerjie
Data: Today
LastEditTime: 2023-08-24 18:47:41
FilePath: \python\350.两个数组的交集-ii.py
'''
#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        vec=[]
        p1=p2=0
        while p1<len(nums1) and p2<len(nums2):
            if nums1[p1]<nums2[p2]:
                p1+=1
            elif nums1[p1]==nums2[p2]:
                vec.append(nums1[p1])
                p1+=1
                p2+=1
            else:
                p2+=1
        return vec
        
# @lc code=end

