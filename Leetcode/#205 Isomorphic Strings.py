# -*- coding: utf-8 -*-
"""
Created on Fri May 17 23:56:33 2019

@author: binxi
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic1 = {}
        index = 0
        for i in s:
            if i not in dic1:
                dic1[i] = index
                index += 1
        lst1 = [dic1[i] for i in s]
        
        dic2 = {}
        index = 0
        for i in t:
            if i not in dic2:
                dic2[i] = index
                index += 1
        lst2 = [dic2[i] for i in t]
        
        return lst1 == lst2