# -*- coding: utf-8 -*-
"""
Created on Sun May  5 00:49:48 2019

@author: binxi
"""

class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        for i in range(0,len(nums),1):
            nums[i] = a * nums[i]**2 + b * nums[i] + c
        
        nums.sort()
        
        return nums