# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 19:49:10 2019

@author: binxi
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n <= 1:
            return 1
            exit
        
        a = 1
        
        b = 1
        
        for i in range(2,n+1,1):
            a,b = b, a+b
            
        return b