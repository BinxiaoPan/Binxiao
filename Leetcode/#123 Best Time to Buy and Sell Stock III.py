# -*- coding: utf-8 -*-
"""
Created on Wed May 22 09:38:04 2019

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
            
        dp1,buy = [0],prices[0]

        i = 1
        for i in range(1,len(prices)):
            buy = min(buy,prices[i])
            profit = prices[i] - buy
            dp1.append(max(dp1[-1],profit))

        dp2,sell = [0], prices[-1]

        for i in range(2,len(prices)+1):
            sell = max(sell,prices[-i])
            profit = sell - prices[-i]
            dp2.append(max(dp2[-1],profit))

        dp2 = dp2[::-1]

        lst = [dp2[i+1]+dp1[i] for i in range(len(dp1)-1)]
        lst.append(dp1[-1])

        return max(lst)