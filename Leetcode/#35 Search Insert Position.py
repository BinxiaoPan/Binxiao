# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 13:12:19 2019

@author: binxi
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        for i in range(0,len(nums),1):
            if target <= nums[i]:
                return i
                exit
        
        return len(nums)