# -*- coding: utf-8 -*-
"""
Created on Fri May 17 02:08:54 2019

@author: binxi
"""

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        A.sort(key = lambda x: x%2)
        return A