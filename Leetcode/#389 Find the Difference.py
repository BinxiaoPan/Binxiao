# -*- coding: utf-8 -*-
"""
Created on Wed May 15 18:17:26 2019

@author: binxi
"""

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s, t = list(s), list(t)
        s.sort()
        t.sort()
        
        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]
                exit
        
        return t[-1]