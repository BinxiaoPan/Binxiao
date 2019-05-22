# -*- coding: utf-8 -*-
"""
Created on Fri May 17 01:33:27 2019

@author: binxi
"""

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

#########solution i
        nums1 = list(set(nums))*2
        
        for i in nums:
            nums1.remove(i)
        
        return nums1[0]
    
#########solution ii
        l = len(nums)
        
        for i in range(l//2):
            if nums[2*i] != nums[2*i+1]:
                return nums[2*i]
                exit
        
        return nums[-1]