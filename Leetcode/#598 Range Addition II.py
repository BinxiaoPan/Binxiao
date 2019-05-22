# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:53:20 2019

@author: binxi
"""

class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if ops == []:
            return m*n
        else:
            l = [x[0] for x in ops]
            w = [x[1] for x in ops]
            return min(l)*min(w)