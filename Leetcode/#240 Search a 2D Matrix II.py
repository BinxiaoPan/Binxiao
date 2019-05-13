# -*- coding: utf-8 -*-
"""
Created on Mon May 13 00:39:44 2019

@author: binxi
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        lst = []
        
        for i in matrix:
            lst += i
        
        return target in lst