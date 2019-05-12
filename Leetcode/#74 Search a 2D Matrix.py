# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 09:24:02 2019

@author: binxi
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [[]]:
            return False
            exit
            
        for i in matrix:
            if target in i:
                return True
                exit
            if i[0] > target:
                break
        
        return False