# -*- coding: utf-8 -*-
"""
Created on Mon May 13 15:13:53 2019

@author: binxi
"""

class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if A == []:
            return []
            exit
            
        B = [[None for j in range(len(A))] for i in range(len(A[0]))]
        
        for i in range(len(B)):
            for j in range(len(B[0])):
                B[i][j] = A[j][i]
        
        return B