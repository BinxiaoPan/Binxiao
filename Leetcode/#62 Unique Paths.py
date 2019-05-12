# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 16:27:33 2019

@author: binxi
"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        path = [[None for i in range(n)] for i in range(m)]
        
        path[0] = [1 for i in range(n)]

        for i in range(1,m,1):
            path[i][0] = 1
            
        for i in range(1,m,1):
            for j in range(1,n,1):
                path[i][j] = path[i-1][j] + path[i][j-1]
        
        return path[m-1][n-1]
