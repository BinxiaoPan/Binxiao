# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 21:46:27 2019

@author: binxi
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s)-1
        
        while i < j:
            t = s[i]
            s[i] = s[j]
            s[j] = t
            i += 1
            j -= 1
            
        return s