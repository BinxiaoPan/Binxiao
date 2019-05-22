# -*- coding: utf-8 -*-
"""
Created on Sat May 18 00:28:25 2019

@author: binxi
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        
        count = {}
        
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        lst = []
        for i in count:
            if count[i] > n/3:
                lst.append(i)
        
        return lst