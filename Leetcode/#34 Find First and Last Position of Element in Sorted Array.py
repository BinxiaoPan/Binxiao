# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 17:23:45 2019

@author: binxi
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target not in nums:
            return [-1,-1]
            exit
        first = nums.index(target)
        last = len(nums) - nums[::-1].index(target) -1
        return [first,last]