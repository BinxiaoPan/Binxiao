# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 12:34:59 2019

@author: binxi
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        elements = list(set(nums))
        
        count = {}
        
        for i in elements:
            count[i] = 0
        
        for i in nums:
            count[i] += 1
        
        for i in nums:
            if count[i] > len(nums)/2:
                return i
                exit