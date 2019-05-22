# -*- coding: utf-8 -*-
"""
Created on Sun May 19 00:33:34 2019

@author: binxi
"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        lst = []
        for i in set(nums1):
            if i in nums2:
                lst.append(i)
                
        return lst