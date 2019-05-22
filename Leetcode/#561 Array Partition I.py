# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:36:09 2019

@author: binxi
"""

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        nums = [nums[2*i] for i in range(len(nums)//2)]
        return sum(nums)