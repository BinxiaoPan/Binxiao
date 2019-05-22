# -*- coding: utf-8 -*-
"""
Created on Wed May 15 23:59:38 2019

@author: binxi
"""

class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """

        lo, hi = -1, 10000
        
        while lo < hi:
            mid = (lo + hi) // 2
            x = reader.get(mid)
            if x == target:
                return mid
                exit
            elif x > target:
                if hi == mid:
                    break
                else:
                    hi = mid
            else:
                if lo == mid:
                    break
                else:
                    lo = mid
        
        return -1