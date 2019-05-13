# -*- coding: utf-8 -*-
"""
Created on Mon May 13 09:53:48 2019

@author: binxi
"""

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
            exit
        
        while n % 3 == 0:
            n = n // 3
        
        return n == 1