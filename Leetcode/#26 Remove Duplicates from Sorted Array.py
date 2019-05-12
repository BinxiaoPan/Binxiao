# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 19:52:06 2019

@author: binxi
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if nums == []:
            return 0
            exit
        
        tail = 0
        
        for i in range(1,len(nums),1):
            if nums[i] != nums[tail]:
                tail += 1
                nums[tail] = nums[i]
        
        return tail+1