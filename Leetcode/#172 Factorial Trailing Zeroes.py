# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 14:37:12 2019

@author: binxi
"""

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 0:
            return 0
            exit
            
        import math
        
        log5 = int(math.log(n,5))
        
        count = 0 
        
        for i in range(1,log5 +1, 1):
            x = 5**i
            count += int(n/x)
        
        return count