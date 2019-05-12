# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 21:21:14 2019

@author: binxi
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1