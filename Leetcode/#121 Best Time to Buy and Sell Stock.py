# -*- coding: utf-8 -*-
"""
Created on Fri May  3 00:45:47 2019

@author: binxi
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
            exit
            
        sell = [0 for i in range(len(prices))]
        
        sell[-1] = prices[-1]
        
        for i in range(len(prices)-2,-1,-1):
            sell[i] = max(sell[i+1],prices[i])
        
        profit = 0
        for i in range(0,len(prices),1):
            if sell[i] - prices[i] > profit:
                profit = sell[i] - prices[i]
        
        return profit