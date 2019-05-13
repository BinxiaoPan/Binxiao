# -*- coding: utf-8 -*-
"""
Created on Mon May 13 14:53:46 2019

@author: binxi
"""

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted(list(map(lambda x: x**2, A)))