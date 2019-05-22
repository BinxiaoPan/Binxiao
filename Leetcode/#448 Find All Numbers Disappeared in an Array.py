# -*- coding: utf-8 -*-
"""
Created on Mon May 20 23:43:37 2019

@author: binxi
"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        lst = list(set(range(1,len(nums)+1))-set(nums))
        
        return lst