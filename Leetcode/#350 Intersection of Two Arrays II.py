# -*- coding: utf-8 -*-
"""
Created on Sun May 19 00:38:06 2019

@author: binxi
"""

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        lst = []
        for i in set(nums1+nums2):
            count = min(nums1.count(i),nums2.count(i))
            lst += [i] * count
        return lst