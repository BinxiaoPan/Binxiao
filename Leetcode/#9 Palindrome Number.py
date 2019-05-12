# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 19:15:34 2019

@author: binxi
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        return x == x[::-1]