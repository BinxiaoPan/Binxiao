# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 08:36:39 2019

@author: binxi
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        if rowIndex == 0:
            return [1]
            exit
        
        last = self.getRow(rowIndex-1)
        
        new = [1]
        
        for i in range(0,(len(last)-1),1):
            new.append(last[i]+last[i+1])
        
        new.append(1)

        return new