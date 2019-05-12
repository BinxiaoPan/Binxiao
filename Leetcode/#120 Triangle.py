# -*- coding: utf-8 -*-
"""
Created on Fri May  3 00:40:02 2019

@author: binxi
"""

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        path = []
        for i in triangle:
            path.append([None for j in range(len(i))])
        
        path[0][0] = triangle[0][0]
        
        for i in range(1,len(triangle),1):
            path[i][0] = path[i-1][0] + triangle[i][0]
            path[i][-1] = path[i-1][-1] + triangle[i][-1]
        
        for i in range(1,len(triangle),1):
            for j in range(1,len(triangle[i])-1,1):
                path[i][j] = min(path[i-1][j],path[i-1][j-1]) + triangle[i][j]
        
        return min(path[-1])