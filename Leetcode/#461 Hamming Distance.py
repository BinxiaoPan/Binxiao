# -*- coding: utf-8 -*-
"""
Created on Tue May 21 11:37:28 2019

@author: binxi
"""

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        lst1, lst2 = [], []
    
        for i in range(31):
            lst1.append(x % 2)
            x = x // 2
            lst2.append(y % 2)
            y = y // 2
        
        lst = [(lst1[i] != lst2[i]) for i in range(31)]

        return sum(lst)