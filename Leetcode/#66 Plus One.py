# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 19:09:28 2019

@author: binxi
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        digits = [0] + digits
        
        digits[-1] +=1
        
        for i in range(len(digits)-1,0,-1):
            if digits[i]>9:
                digits [i] -= 10
                digits[i-1] += 1
        
        if digits[0] == 0:
            return digits[1:]
        else:
            return digits