# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 00:30:00 2019

@author: binxi
"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        
        solution = []
        
        for i in range(0,len(nums)-3,1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2,1):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l, r = j+1, len(nums)-1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]

                    if s < target:
                        l +=1 
                    elif s > target:
                        r -= 1
                    else:
                        solution.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1; r -= 1                       
                        
        return solution