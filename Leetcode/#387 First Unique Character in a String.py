# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 17:13:56 2019

@author: binxi
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(0,len(s),1):
            if s[i] not in s[:i]+s[i+1:]:
                return i
                break
        
        return -1