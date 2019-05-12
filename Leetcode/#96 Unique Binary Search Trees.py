# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 20:11:49 2019

@author: binxi
"""

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        unique = [0 for i in range(n+1)]
        
        unique[0],unique[1] = 1,1
        
        for i in range(2,n+1,1):
            for j in range(0,i,1):
                unique[i] += unique[j]*unique[i-1-j]
        
        return unique[n]