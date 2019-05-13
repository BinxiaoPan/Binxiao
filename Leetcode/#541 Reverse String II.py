# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:55:40 2019

@author: binxi
"""

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        lst = []
        
        while s != '':
            if len(s) > k:
                lst.append(s[:k])
                s = s[k:]
            else:
                lst.append(s)
                s = ''
        
        for i in range(len(lst)):
            if i % 2 == 0:
                lst[i] = lst[i][::-1]
        
        return ''.join(lst)