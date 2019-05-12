# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 13:17:16 2019

@author: binxi
"""

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        
        for i in range(0,int(n/2),1):
            x1,y1 = i,i
            x2,y2 = i,n-1-i
            x3,y3 = n-1-i,n-1-i
            x4,y4 = n-1-i,i
            while y1 < n-1-i:
                a = matrix[x4][y4]
                matrix[x4][y4] = matrix[x3][y3]
                matrix[x3][y3] = matrix[x2][y2]
                matrix[x2][y2] = matrix[x1][y1]
                matrix[x1][y1] = a
                y1 += 1
                x2 += 1
                y3 -= 1
                x4 -= 1