# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 16:46:36 2019

@author: binxi
"""


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        if (obstacleGrid[0][0] == 1)|(obstacleGrid[m-1][n-1] == 1):
            return 0
            exit
        
        path = [[0 for i in range(n)] for i in range(m)]
        
        path[0][0] = 1
        for i in range(1,n,1):
            if obstacleGrid[0][i-1] != 1:
                path[0][i] = path[0][i-1]

        for i in range(1,m,1):
            if obstacleGrid[i-1][0] != 1:
                path[i][0] = path[i-1][0] 
            
        for i in range(1,m,1):
            for j in range(1,n,1):
                if obstacleGrid[i][j-1] != 1:
                    path[i][j] += path[i][j-1]
                if obstacleGrid[i-1][j] != 1:
                    path[i][j] += path[i-1][j]
        
        return path[m-1][n-1]