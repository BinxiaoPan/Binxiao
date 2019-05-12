# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 10:01:32 2019

@author: binxi
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(set(nums))*2 - sum(nums)