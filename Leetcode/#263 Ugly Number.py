# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 17:50:38 2019

@author: binxi
"""

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <=0 :
            return False
            exit
        
        if num == 1:
            return True
            exit
        
        if num % 2 == 0:
            return self.isUgly(num/2)
        elif num%3 == 0:
            return self.isUgly(num/3)
        elif num%5 == 0:
            return self.isUgly(num/5)
        else:
            return False
