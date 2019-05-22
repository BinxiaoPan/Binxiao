# -*- coding: utf-8 -*-
"""
Created on Tue May 21 16:38:48 2019

@author: binxi
"""

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return min(len(set(candies)),len(candies)//2)