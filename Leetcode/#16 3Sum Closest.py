# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 00:46:38 2019

@author: binxi
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        
        solution = 2**30
        
        for i in xrange(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if abs(s - target) < abs(solution - target):
                    solution = s
                
                if s < target:
                    l +=1 
                elif s > target:
                    r -= 1
                else:
                    return s
                    exit
        
        return solution