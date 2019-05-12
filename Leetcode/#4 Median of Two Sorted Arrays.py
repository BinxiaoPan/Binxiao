# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 15:38:13 2019

@author: binxi
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        import numpy as np
        nums = np.append(nums1,nums2)
        nums.sort()
        length = len(nums)
        if length % 2 == 1:
            return nums[(length+1)/2-1]
        else:
            return np.mean(nums[(int(length/2)-1):int(length/2)+1])