# -*- coding: utf-8 -*-
"""
Created on Mon May 20 23:35:15 2019

@author: binxi
"""

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        lo, hi = 0, 2**31
        
        while hi - lo >1:
            mid = (hi + lo) // 2
            coin = (1 + mid) * mid// 2
            if coin == n:
                return mid
                exit
            elif coin < n:
                lo = mid
            else:
                hi = mid
        
        return lo