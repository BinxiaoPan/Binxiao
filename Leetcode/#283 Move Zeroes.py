# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 20:11:18 2019

@author: binxi
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        
        for i in range(0,l,1):
            while nums[i]==0:
                if nums[i+1:] == [0]*(l-i-1):
                    break
                nums[i:-1] = nums[i+1:]
                nums[-1] = 0
        
        return nums