# -*- coding: utf-8 -*-
"""
Created on Fri May 17 02:10:22 2019

@author: binxi
"""

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        lst = []
        for i in matrix:
            lst += i
        lst.sort()
        return lst[k-1]