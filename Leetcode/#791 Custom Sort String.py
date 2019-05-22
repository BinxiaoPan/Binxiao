# -*- coding: utf-8 -*-
"""
Created on Fri May 17 02:02:03 2019

@author: binxi
"""

class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """

        dic,index = {},0
        for i in S:
            if i not in dic:
                dic[i] = index
                index += 1
        for i in T:
            if i not in dic:
                dic[i] = index
                index += 1
            
        T = list(T)
        T.sort(key=lambda x:dic[x])
        
        T = ''.join(T)
        
        return T