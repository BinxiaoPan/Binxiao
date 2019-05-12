# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 15:35:55 2019

@author: binxi
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        done = False
        for i in range(0,len(nums)-1,1):
            for j in range(i+1,len(nums),1):
                if nums[i]+nums[j] == target:
                    done=True
                if done:
                    break
            if done:
                break
        
        return [i,j]