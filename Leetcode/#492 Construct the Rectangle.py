# -*- coding: utf-8 -*-
"""
Created on Tue May 21 15:39:25 2019

@author: binxi
"""

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        for i in reversed(range(int(area**0.5)+1)):
            if area % i == 0:
                return [area // i, i]
                exit