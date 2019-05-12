# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 10:14:50 2019

@author: binxi
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dup = []
        
        for i in set(nums):
            if nums.count(i) >2:
                dup.append(i)

        for i in dup:
            k = nums.count(i) - 2
            for j in range(0,k,1):
                nums.remove(i)