# -*- coding: utf-8 -*-
"""
Created on Tue May 21 15:45:04 2019

@author: binxi
"""

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
            exit
        
        sign = num/abs(num)
        num = abs(num)
        
        lst = []
        while num != 0:
            lst.append(num % 7)
            num = num // 7
        
        lst = lst[::-1]
        
        lst[0] = lst[0] * sign
        
        lst = [str(x) for x in lst]
        
        return ''.join(lst)