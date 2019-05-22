# -*- coding: utf-8 -*-
"""
Created on Tue May 21 17:21:50 2019

@author: binxi
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        lst = []
        for i in range(32):
            lst.append(n%2)
            n = n // 2
        n = 0
        for i in lst:
            n = n*2 +i
        
        return n