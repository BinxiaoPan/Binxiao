# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 21:21:51 2019

@author: binxi
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:m+n] = nums2
        nums1[m+n:] = [2**31-1]*(len(nums1)-m-n)
        nums1.sort()
        
        return nums1