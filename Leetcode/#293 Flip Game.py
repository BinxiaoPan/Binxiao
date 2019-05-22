# -*- coding: utf-8 -*-
"""
Created on Sun May 19 00:10:12 2019

@author: binxi
"""

class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        lst = []
        
        for i in range(len(s)-1):
            if s[i:i+2] == '++':
                lst.append(s[:i] + '--' + s[i+2:])
        
        return lst