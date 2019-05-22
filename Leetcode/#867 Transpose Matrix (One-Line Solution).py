# -*- coding: utf-8 -*-
"""
Created on Mon May 20 21:06:42 2019

@author: binxi
"""

class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        
        return list(map(list,zip(*A)))