# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 23:07:07 2019

@author: binxi
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        for i in range(0,len(nums),1):
            if nums[i] == target:
                return(i)
                exit
        
        return(-1)