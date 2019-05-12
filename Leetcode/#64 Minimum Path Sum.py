# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 08:26:52 2019

@author: binxi
"""

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n = len(grid), len(grid[0])
        path = [[2**31 for i in range(n)] for j in range(m)]
        
        path[0][0] = grid[0][0]
        
        while True:
            perfect = True
            for i in range(0,m):
                for j in range(0,n):
                    if i > 0:
                        if path[i-1][j] + grid[i][j] < path[i][j]:
                            path[i][j] = path[i-1][j] + grid[i][j]
                            perfect = False

                    if j > 0:
                        if path[i][j-1] + grid[i][j] < path[i][j]:
                            path[i][j] = path[i][j-1] + grid[i][j]
                            perfect = False
            if perfect:
                break
        
        return path[m-1][n-1]