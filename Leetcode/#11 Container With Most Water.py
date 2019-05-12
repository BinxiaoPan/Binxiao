# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 19:29:37 2019

@author: binxi
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l=[]
        r=[]

        lh = height.index(max(height))
        rh = height[::-1].index(max(height))
        rh = len(height)-rh-1

        h=0

        for i in range(0,lh+1,1):
            if height[i]>h:
                l.append(i)
                h = height[i]
        h=0

        for i in range(len(height)-1,rh-1,-1):
            if height[i]>h:
                r.append(i)
                h = height[i]
        benchmark = 0

        for i in l:
            for j in r:
                area = min(height[i],height[j])*(j-i)
                benchmark = max(area , benchmark)

        return benchmark