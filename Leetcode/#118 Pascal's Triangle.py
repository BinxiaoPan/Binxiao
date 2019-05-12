# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 08:23:22 2019

@author: binxi
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        if numRows == 0:
            return []
            exit
        
        if numRows == 1:
            return [[1]]
            exit

        
        last = self.generate(numRows-1)
        
        last_last = [0] + last[-1] + [0]
        
        new = []
        
        for i in range(0,len(last_last)-1,1):
            new.append( (last_last[i] + last_last[i+1]) )
        
        last.append(new)


        return last