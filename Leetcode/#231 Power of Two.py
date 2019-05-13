# -*- coding: utf-8 -*-
"""
Created on Mon May 13 00:26:53 2019

@author: binxi
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n < 1:
            return False
            exit
            
        while n % 2 == 0:
            n = n/2
        
        return n == 1