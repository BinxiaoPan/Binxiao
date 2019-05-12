# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:59:16 2019

@author: binxi
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x == 0:
            return 0
            exit
        
        negative = x<0

        if negative:
            x=-x
        
        while x%10 == 0:
            x = x/10

        reverse_str = str(x)[::-1]

        y = int(reverse_str)

        if negative:
            y = -y

        if (y > 2**31-1) | (y < -2**31):
            y = 0
        
        return y