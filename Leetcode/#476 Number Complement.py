# -*- coding: utf-8 -*-
"""
Created on Tue May 21 11:40:51 2019

@author: binxi
"""

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        lst = []
        
        while num > 0:
            lst.append(num % 2)
            num = num // 2
        
        lst = [1 - x for x in lst]
        
        num = 0
        
        for i in lst[::-1]:
            num = num*2 + i
        
        return num