# -*- coding: utf-8 -*-
"""
Created on Mon May 13 00:43:41 2019

@author: binxi
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        return not len(nums) == len(set(nums))