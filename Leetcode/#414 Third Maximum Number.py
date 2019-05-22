# -*- coding: utf-8 -*-
"""
Created on Sun May 19 00:42:16 2019

@author: binxi
"""

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        nums.sort()
        if len(nums) < 3:
            return nums[-1]
        else:
            return nums[-3]