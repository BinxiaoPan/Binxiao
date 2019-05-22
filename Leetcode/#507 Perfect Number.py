# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:15:34 2019

@author: binxi
"""

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
            exit
        
        lst = [1]

        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                lst += [i, num // i]
        
        return sum(lst) == num