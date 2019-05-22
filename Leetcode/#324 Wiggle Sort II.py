# -*- coding: utf-8 -*-
"""
Created on Fri May 17 01:41:10 2019

@author: binxi
"""

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        nums1 = nums[:]
        nums1.sort()
        l = len(nums1)
        nums2 = nums1[:(l+1)//2][::-1]
        nums3 = nums1[(l+1)//2:][::-1]
        
        for i in range(l):
            if i % 2 == 0:
                nums[i] = nums2[i // 2]
            else:
                nums[i] = nums3[i // 2]        