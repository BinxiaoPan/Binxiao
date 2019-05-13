# -*- coding: utf-8 -*-
"""
Created on Sun May 12 23:04:56 2019

@author: binxi
"""

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if s == '':
            return []
            exit
        
        lst = []
        
        for i in range(len(s)):
            if s[:i+1] == s[:i+1][::-1]:
                if i+1 == len(s):
                    lst.append([s])
                else:
                    for j in self.partition(s[i+1:]):
                        lst.append([s[:i+1]]+j)
        return lst