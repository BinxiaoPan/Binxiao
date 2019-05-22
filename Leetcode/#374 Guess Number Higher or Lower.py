# -*- coding: utf-8 -*-
"""
Created on Wed May 15 18:02:37 2019

@author: binxi
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        lo = 1
        hi = n
        
        while True:
            med = (lo + hi) // 2
            check = guess(med)
            if check == 0:
                return med
                exit
            elif check == 1:
                lo = med + 1
            else:
                hi = med - 1
        
        return med