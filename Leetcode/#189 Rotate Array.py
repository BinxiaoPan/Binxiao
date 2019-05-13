# -*- coding: utf-8 -*-
"""
Created on Mon May 13 00:58:50 2019

@author: binxi
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        
        nums[:] = nums[-k:] + nums[:-k]