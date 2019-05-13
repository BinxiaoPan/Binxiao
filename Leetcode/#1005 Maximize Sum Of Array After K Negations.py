# -*- coding: utf-8 -*-
"""
Created on Mon May 13 14:57:49 2019

@author: binxi
"""

class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        for i in range(K):
            A.sort()
            A[0] = -A[0]
        
        return sum(A)