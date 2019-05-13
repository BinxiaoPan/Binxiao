# -*- coding: utf-8 -*-
"""
Created on Mon May 13 00:03:30 2019

@author: binxi
"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return nums.index(max(nums))