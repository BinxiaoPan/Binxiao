# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:30:30 2019

@author: binxi
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        if numRows == 1:
            return s
            exit
        
        row=[]
        
        for i in range(1,numRows+1,1):
            row.append('')
    
        position = 0
        direction = 1
        
        while s != '':
            row[position] += s[0]
            s = s[1:]
            if direction == 1:
                if position != numRows-1:
                    position +=1
                else:
                    position -=1
                    direction =0
            else:
                if position != 0:
                    position -=1
                else:
                    position +=1
                    direction =1
            
        for i in row:
            s += i
        
        return s


