# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 13:03:38 2019

@author: binxi
"""

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]
            exit
        
        permutation = []
        
        for i in set(nums):
            copy = nums[:]
            copy.remove(i)
            for j in self.permuteUnique(copy):
                if ([i]+j) not in permutation:
                    permutation.append([i]+j)
        
        return permutation