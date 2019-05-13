# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:13:54 2019

@author: binxi
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i
                exit
        return i+1