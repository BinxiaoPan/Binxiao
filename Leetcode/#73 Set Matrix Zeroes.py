# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 21:55:46 2019

@author: binxi
"""

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        indexlst=[]
        
        m,n = len(matrix), len(matrix[0])
        
        for i in range(0,m,1):
            for j in range(0,n,1):
                if matrix[i][j] == 0:
                    indexlst.append([i,j])
        
        for index in indexlst:
            x = index[0]
            y = index[1]
            for j in range(0,n,1):
                matrix[x][j] = 0
            for i in range(0,m,1):
                matrix[i][y] = 0