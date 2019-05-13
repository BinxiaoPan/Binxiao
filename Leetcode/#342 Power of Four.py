# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:17:18 2019

@author: binxi
"""

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
            exit
        
        while num % 4 == 0:
            num = num // 4
        
        return num == 1       