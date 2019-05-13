# -*- coding: utf-8 -*-
"""
Created on Sun May 12 23:52:47 2019

@author: binxi
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = s.split()[::-1]
        
        s1 = ''
        
        for i in lst:
            s1 += i + ' '
        
        return s1[:-1]