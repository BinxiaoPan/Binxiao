# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 23:25:42 2019

@author: binxi
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()

        missing = 1
        
        for i in nums:
            if i == missing:
                missing += 1
        
        return missing
