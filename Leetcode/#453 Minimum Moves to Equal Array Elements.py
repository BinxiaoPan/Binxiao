# -*- coding: utf-8 -*-
"""
Created on Mon May 20 23:56:47 2019

@author: binxi
"""

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        
        lst = [nums[i+1] - nums[0] for i in range(len(nums)-1)]
        
        return sum(lst)