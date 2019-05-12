# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 23:38:23 2019

@author: binxi
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1, t1 = list(s), list(t)
        s1.sort()
        t1.sort()
        
        return s1 == t1