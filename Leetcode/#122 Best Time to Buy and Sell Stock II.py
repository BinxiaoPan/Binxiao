# -*- coding: utf-8 -*-
"""
Created on Fri May  3 00:49:08 2019

@author: binxi
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        
        for i in range(0,len(prices)-1,1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
        
        return profit