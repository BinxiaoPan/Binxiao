# -*- coding: utf-8 -*-
"""
Created on Mon May 13 00:14:00 2019

@author: binxi
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = ''
        while n != 0:
            s += str(n % 2)
            n = n//2
        return s.count('1')