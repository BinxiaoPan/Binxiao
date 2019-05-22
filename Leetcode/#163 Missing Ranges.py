# -*- coding: utf-8 -*-
"""
Created on Fri May 17 13:19:48 2019

@author: binxi
"""

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        nums = [lower-1] + nums + [upper+1]
        
        gap = []
        
        def gapper(lo,hi):
            if lo == hi:
                return str(lo)
            else:
                return str(lo) + '->' + str(hi)
        
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] >1:
                gap.append(gapper(nums[i]+1, nums[i+1]-1))
        
        return gap