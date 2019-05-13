# -*- coding: utf-8 -*-
"""
Created on Mon May 13 11:51:33 2019

@author: binxi
"""

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        parameter = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if i == 0:
                        parameter += 1
                    else:
                        if grid[i-1][j] == 0:
                            parameter += 1

                    if j == 0:
                        parameter += 1
                    else:
                        if grid[i][j-1] == 0:
                            parameter += 1

                    if i == len(grid)-1:
                        parameter += 1
                    else:
                        if grid[i+1][j] == 0:
                            parameter += 1
                            
                    if j == len(grid[0])-1:
                        parameter += 1
                    else:
                        if grid[i][j+1] == 0:
                            parameter += 1

        return parameter