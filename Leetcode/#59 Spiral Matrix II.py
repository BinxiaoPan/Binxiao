# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 09:02:34 2019

@author: binxi
"""

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[None for i in range(n)] for j in range (n)]
        
        x1,y1 = 0,0
        x2,y2 = 0,n-1
        x3,y3 = n-1,n-1
        x4,y4 = n-1,0

        x=0

        while True:
            for i in range(y1,y2+1,1):
                x += 1
                matrix[x1][i] = x
            for i in range(x2+1,x3+1,1):
                x += 1
                matrix[i][y2] = x
            for i in range(y3-1,y4-1,-1):
                x += 1
                matrix[x3][i] = x
            for i in range(x4-1,x1,-1):
                x += 1
                matrix[i][y4] = x
            x1, y1 = x1+1, y1+1
            x2, y2 = x2+1, y2-1
            x3, y3 = x3-1, y3-1
            x4, y4 = x4-1, y4+1
            
            if (x1>x4)|(y1>y2):
                break
        
        return matrix