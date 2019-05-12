# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 18:28:40 2019

@author: binxi
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l = len(nums)
        
        for i in range(1,l,1):
            nums[i] += max(nums[i-1],0)
        
        return max(nums)
                        