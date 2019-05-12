# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 09:37:24 2019

@author: binxi
"""

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        matrix = [[[[]] for j in range(0,k,1)] for i in range(0,n,1)]

        matrix[0][0] = [[1]]

        #k=1, n=i+1 situation
        for i in range(1,n,1):
            matrix[i][0] = matrix[i-1][0]+[[i+1]] 

        #i=
        for i in range(1,n,1):
            for j in range(1,k,1):
                matrix[i][j] = matrix[i-1][j]
                matrix[i][j] = matrix[i][j][:]
                for t in matrix[i-1][j-1]:
                    if t != []:
                        matrix[i][j].append(t+[i+1])
        
        if [] in matrix[n-1][k-1]:
            matrix[n-1][k-1].remove([])
            
        return matrix[n-1][k-1]