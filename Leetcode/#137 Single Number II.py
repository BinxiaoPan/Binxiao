# -*- coding: utf-8 -*-
"""
Created on Sun May 12 23:28:44 2019

@author: binxi
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in set(nums):
            if nums.count(i) != 3:
                return i
                exit