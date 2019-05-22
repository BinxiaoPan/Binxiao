# -*- coding: utf-8 -*-
"""
Created on Sat May 18 23:44:50 2019

@author: binxi
"""

class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        n = 0
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i] + nums[j] + nums[k] < target:
                        n += 1
        
        return n