# -*- coding: utf-8 -*-
"""
Created on Tue May 21 17:07:43 2019

@author: binxi
"""

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums1 = sorted(nums)
        
        if nums1 == nums:
            return 0
            exit
            
        for i in range(len(nums)):
            if nums[i] != nums1[i]:
                break
        
        for j in reversed(range(len(nums))):
            if nums[j] != nums1[j]:
                break

        return j+1-i