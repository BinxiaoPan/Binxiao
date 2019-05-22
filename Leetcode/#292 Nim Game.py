# -*- coding: utf-8 -*-
"""
Created on Sat May 18 23:59:06 2019

@author: binxi
"""

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0