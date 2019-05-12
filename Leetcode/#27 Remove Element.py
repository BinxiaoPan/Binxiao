# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 21:20:10 2019

@author: binxi
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        tail = 0
        
        for i in range(0,len(nums),1):
            if nums[i] != val:
                nums[tail] = nums[i]
                tail +=1
        
        return tail