# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 23:44:48 2019

@author: binxi
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        l = [None] * len(height)

        r = [None] * len(height)
        
        l_max = - 2**30
        
        for i in range(0,len(height),1):
            l_max = max(height[i], l_max)
            l[i] = l_max
        
        r_max = -2**30
        
        for i in range(len(height)-1,-1,-1):
            r_max = max(height[i], r_max)
            r[i] = r_max
        
        trap = 0
        
        for i in range(0,len(height),1):
            trap += min(l[i],r[i]) - height[i]
        
        return trap