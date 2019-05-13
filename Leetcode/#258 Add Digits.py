# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:01:43 2019

@author: binxi
"""

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            s = list(str(num))
            s = map(lambda x: int(x), s)
            num = sum(s)
        
        return num