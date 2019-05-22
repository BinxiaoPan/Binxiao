# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:18:59 2019

@author: binxi
"""

class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        if N <= 1 :
            return N
        else:
            a,b = 0,1
            for i in range(2,N+1):
                a,b = b, a+b
            return b