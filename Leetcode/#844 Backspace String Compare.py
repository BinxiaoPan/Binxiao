# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 21:54:37 2019

@author: binxi
"""

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def backed(t):
            while '#' in t:
                index = t.index('#')
                if index == 0:
                    t = t[1:]
                else: 
                    t = t[:index-1] + t[index+1:]
            return t
        
        return backed(S) == backed(T)