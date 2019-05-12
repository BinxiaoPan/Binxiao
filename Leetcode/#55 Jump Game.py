# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 23:18:42 2019

@author: binxi
"""

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        jumpable = [False]*len(nums)
        jumpable = jumpable[:]
        jumpable[0] = True
        latest = 0
        
        for i in range(0,len(nums),1):
            if jumpable[i]:
                x = i+nums[i]
                if x>= len(nums)-1:
                    return True
                    exit
                elif x > latest:
                    for j in range(latest+1,min(x+1,len(nums)),1):
                        jumpable[j] = True
                    latest = x
            else:
                break
        
        return jumpable[-1]