# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 23:18:13 2019

@author: binxi
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
            exit
            
        m,n = len(matrix), len(matrix[0])

        spiral = []
        x1,y1 = 0,0
        x2,y2 = 0,n-1
        x3,y3 = m-1,n-1
        x4,y4 = m-1,0
        
        while True:
            if [x1,y1] == [x2,y2]:
                for i in range(x1,x3+1,1):
                    spiral.append(matrix[i][y1])
                break
            elif [x1,y1] == [x4,y4]:
                for i in range(y1,y2+1,1):
                    spiral.append(matrix[x1][i])
                break
            else:
                for i in range(y1,y2+1,1):
                    spiral.append(matrix[x1][i])
                for i in range(x2+1,x3+1,1):
                    spiral.append(matrix[i][y2])
                for i in range(y3-1,y4-1,-1):
                    spiral.append(matrix[x3][i])
                for i in range(x4-1,x1,-1):
                    spiral.append(matrix[i][y4])
                x1, y1 = x1+1, y1+1
                x2, y2 = x2+1, y2-1
                x3, y3 = x3-1, y3-1
                x4, y4 = x4-1, y4+1
                
                if (x1>x4)|(y1>y2):
                    break
            
        return spiral