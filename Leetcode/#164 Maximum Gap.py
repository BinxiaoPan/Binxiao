# -*- coding: utf-8 -*-
"""
Created on Fri May 17 13:23:57 2019

@author: binxi
"""

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
            exit
            
        nums.sort()
        lst = []
        for i in range(len(nums)-1):
            lst.append(nums[i+1]-nums[i])
            
        return max(lst)