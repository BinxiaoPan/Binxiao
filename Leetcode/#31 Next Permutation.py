# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 18:29:52 2019

@author: binxi
"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        k = len(nums)
        
        if k >1 :
            for i in range(k-2,-1,-1):
                if nums[i] < nums[i+1]:
                    break

            if nums[i] < nums[i+1]:
                for j in range(k-1,i,-1):
                    if nums[j] > nums[i]:
                        break
                x = nums[i]
                nums[i] = nums[j]
                nums[j] = x
            else:
                i = -1
            
            begin = i+1
            mid = int((i+k)/2)
            for j in range(begin,mid+1,1):
                x = nums[j]
                nums[j] = nums[begin+k-1-j]
                nums[begin+k-1-j] = x