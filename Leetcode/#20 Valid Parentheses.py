# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 14:48:46 2019

@author: binxi
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        while (('[]' in s) | ('{}' in s) | ('()' in s) ):
            s = s.replace('[]','')
            s = s.replace('{}','')
            s = s.replace('()','')
        
        return s == ''