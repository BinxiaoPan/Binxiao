# -*- coding: utf-8 -*-
"""
Created on Tue May 21 17:11:06 2019

@author: binxi
"""

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x = sum(nums) - sum(set(nums))
        y = sum(set(range(1,len(nums)+1)) - set(nums))
        return [x,y]